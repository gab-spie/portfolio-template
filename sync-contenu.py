#!/usr/bin/env python3
"""Synchronise le site avec contenu.json.

À lancer après chaque modification de contenu.json :
    python3 sync-contenu.py

Ce script :
  1. vérifie que contenu.json est un JSON valide et signale les oublis courants ;
  2. regénère contenu.js (copie des données, utilisée quand la page est ouverte
     directement sans serveur) ;
  3. remplit les balises de partage (title, description, og:*) dans index.html,
     pour que LinkedIn, WhatsApp, Slack... affichent le bon aperçu.
"""
import html
import json
import os
import re
import sys
import tempfile
from urllib.parse import unquote

ICI = os.path.dirname(os.path.abspath(__file__))


def texte(v):
    # même règle que fr() dans index.html : la clé "fr" si elle existe, sinon "en"
    if v is None:
        return ""
    if isinstance(v, dict):
        v = v.get("fr") if v.get("fr") is not None else v.get("en")
        return "" if v is None or isinstance(v, (dict, list)) else str(v)
    return str(v)


def dico(v):
    return v if isinstance(v, dict) else {}


def verifier(c):
    avis = []
    ident = dico(c.get("identite"))
    if not ident.get("prenom") and not ident.get("nom"):
        avis.append("identite.prenom et identite.nom sont vides")
    site = dico(c.get("site"))
    if not texte(site.get("description")):
        avis.append("site.description est vide (aperçu de partage)")
    if not site.get("imagePartage"):
        avis.append("site.imagePartage est vide (image d'aperçu 1200x630)")
    url = texte(site.get("url")).strip()
    if not url:
        avis.append("site.url est vide (les aperçus de partage ont besoin de l'adresse finale)")
    elif not re.match(r"^https?://", url):
        avis.append("site.url doit commencer par https:// (" + url + ")")
    chemins = []

    def parcourir(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("src", "logo", "imagePartage") and isinstance(v, str) and v.strip() \
                        and not re.match(r"^([a-z][a-z0-9+.-]*:|//)", v.strip(), re.I):
                    chemins.append(v.strip())
                parcourir(v)
        elif isinstance(x, list):
            for v in x:
                parcourir(v)

    parcourir(c)
    for p in sorted(set(chemins)):
        # sans ?v=2 ni #ancre, %20 décodé, "/img/x.jpg" lu depuis la racine du site
        f = unquote(re.split(r"[?#]", p)[0]).lstrip("/")
        if not f or not os.path.isfile(os.path.join(ICI, f)):
            avis.append("image introuvable : " + p)
    return avis


def bloc_meta(c):
    site = dico(c.get("site"))
    ident = dico(c.get("identite"))
    nom = (texte(ident.get("prenom")) + " " + texte(ident.get("nom"))).strip()
    titre = texte(site.get("titre")) or " · ".join(x for x in (nom, texte(ident.get("etiquette")) or "Portfolio") if x)
    desc = texte(site.get("description"))
    base = texte(site.get("url")).strip().rstrip("/")
    base = base + "/" if base else ""
    img = texte(site.get("imagePartage")).strip()
    if img and not re.match(r"^https?:", img):
        img = base + re.sub(r"^\.?/", "", img)
    e = lambda s: html.escape(s, quote=True)
    lignes = ["<title>%s</title>" % html.escape(titre)]
    if desc:
        lignes.append('<meta name="description" content="%s">' % e(desc))
    lignes.append('<meta property="og:title" content="%s">' % e(titre))
    if desc:
        lignes.append('<meta property="og:description" content="%s">' % e(desc))
    lignes.append('<meta property="og:type" content="website">')
    if base:
        lignes.append('<meta property="og:url" content="%s">' % e(base))
    if img:
        lignes.append('<meta property="og:image" content="%s">' % e(img))
        lignes.append('<meta property="og:image:width" content="1200">')
        lignes.append('<meta property="og:image:height" content="630">')
        lignes.append('<meta name="twitter:image" content="%s">' % e(img))
        lignes.append('<meta name="twitter:card" content="summary_large_image">')
    couleur = texte(site.get("couleurNavigateur"))
    if couleur:
        lignes.append('<meta name="theme-color" content="%s">' % e(couleur))
    return "\n".join(lignes)


def ecrire(chemin, texte_):
    # écriture dans un fichier temporaire puis remplacement : jamais de fichier vide ou à moitié écrit
    fd, tmp = tempfile.mkstemp(dir=ICI, prefix=".sync-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(texte_)
        os.chmod(tmp, os.stat(chemin).st_mode & 0o777 if os.path.exists(chemin) else 0o644)
        os.replace(tmp, chemin)
    except BaseException:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def erreur(msg):
    print(msg + " Rien n'a été modifié.", file=sys.stderr)
    sys.exit(1)


def refuser_constante(nom):
    raise ValueError(nom + " n'est pas accepté en JSON (le navigateur refuserait le fichier)")


def main():
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(errors="replace")  # console Windows : pas de plantage sur un caractère accentué
        except (AttributeError, ValueError):
            pass
    chemin = os.path.join(ICI, "contenu.json")
    try:
        with open(chemin, encoding="utf-8-sig") as f:  # -sig : accepte un fichier enregistré avec BOM (Bloc-notes)
            c = json.load(f, parse_constant=refuser_constante)
    except FileNotFoundError:
        erreur("contenu.json introuvable à côté de sync-contenu.py.")
    except json.JSONDecodeError as err:
        erreur("contenu.json n'est pas un JSON valide : ligne %d, colonne %d : %s." % (err.lineno, err.colno, err.msg))
    except UnicodeDecodeError:
        erreur("contenu.json doit être enregistré en UTF-8.")
    except ValueError as err:
        erreur("contenu.json n'est pas un JSON valide : %s." % err)
    if not isinstance(c, dict):
        erreur("contenu.json doit contenir un objet { ... }.")

    index = os.path.join(ICI, "index.html")
    try:
        with open(index, encoding="utf-8", newline="") as f:  # newline="" : garde les fins de ligne d'origine
            src = f.read()
    except FileNotFoundError:
        erreur("index.html introuvable à côté de sync-contenu.py.")
    except UnicodeDecodeError:
        erreur("index.html doit être enregistré en UTF-8.")
    neuf, n = re.subn(r"<!-- meta:start -->.*?<!-- meta:end -->",
                      lambda m: "<!-- meta:start -->\n" + bloc_meta(c) + "\n<!-- meta:end -->", src, flags=re.S)
    if n != 1:
        erreur("Les repères <!-- meta:start --> et <!-- meta:end --> doivent apparaître une seule fois dans index.html (trouvés : %d)." % n)

    for a in verifier(c):
        print("Attention :", a)

    ecrire(os.path.join(ICI, "contenu.js"),
           "// Fichier généré par sync-contenu.py à partir de contenu.json. Ne le modifie pas à la main.\n"
           "window.CONTENU = " + json.dumps(c, ensure_ascii=False, indent=2) + ";\n")
    if neuf != src:
        ecrire(index, neuf)
    print("OK : contenu.js et les balises de partage sont à jour.")


if __name__ == "__main__":
    main()
