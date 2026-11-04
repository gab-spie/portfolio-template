# Guide complet

[English version below](#english-guide)

Ce guide explique tout, pas à pas : récupérer le template, le remplir, le tester, le mettre en ligne avec Vercel et l'exporter en PDF.

## 0. Avant de commencer : ce qu'il te faut

- **Une IA** : Claude, ChatGPT, Gemini ou une autre. Si elle peut lire des fichiers (tu lui envoies le ZIP), c'est plus simple.
- **Pour la mise en ligne**, deux comptes gratuits. Tu peux les créer maintenant, pendant l'entretien ou à la fin :
  - **GitHub** (github.com) : l'endroit où les fichiers de ton site sont rangés ;
  - **Vercel** (vercel.com) : le service qui met ton site sur Internet. Tu t'y inscris avec **Continue with GitHub**, sans nouveau mot de passe.
- **Les connecteurs : facultatifs.** Certaines applications d'IA (par exemple Claude) peuvent se connecter à ton GitHub et à ton Vercel. L'IA peut alors mettre le site en ligne elle-même, avec ton accord. Tu les actives dans les paramètres de l'application, rubrique des connecteurs, puis **GitHub** et **Vercel**. **Sans connecteur, tout marche aussi** : l'IA te guide clic par clic (section 8).
- **Python** : seulement pour la synchronisation (section 4). Si ton IA peut lancer des commandes, elle s'en occupe.


Ce portfolio est un dossier de fichiers. **Tout ton contenu est dans un seul fichier : `contenu.json`**. Tes images sont dans `img/`. Tu ne touches jamais au code : le design, les animations, le thème clair/sombre et le FR/EN sont déjà prêts.

<a id="recuperer"></a>

## 2. Récupérer le template

GitHub est l'endroit où le template est stocké. Quelle que soit la méthode, tu obtiens **un dossier sur ton ordinateur** : c'est là que tu fabriques ton portfolio.

| Méthode | Ce que tu fais | Quand la choisir |
|---|---|---|
| **Use this template** (recommandé) | Sur la page GitHub du template, bouton vert **Use this template**, puis **Create a new repository**. Tu obtiens ton propre dépôt, sans lien avec le template. Récupère-le sur ton ordinateur : `git clone https://github.com/ton-compte/ton-portfolio.git`, ou avec GitHub Desktop. | Tu veux mettre en ligne facilement, avec mise à jour automatique. |
| **Télécharger le ZIP** | Bouton **Code**, puis **Download ZIP**. Tu décompresses : tu as un dossier. | Tu ne connais pas Git. Pour Vercel, tu créeras plus tard un dépôt GitHub et tu y déposeras les fichiers (**Add file**, puis **Upload files**). |
| **Cloner directement** | `git clone https://github.com/gab-spie/portfolio-template.git mon-portfolio`, puis `git remote remove origin`. Tu relieras ensuite le dossier à ton propre dépôt. | Tu connais Git. |

Déroulé : tu récupères le dossier, tu l'ouvres avec ton IA ou un éditeur, tu remplis `contenu.json` et `img/`, tu testes, puis tu mets en ligne.

## 3. Remplir le contenu

### Option A : avec une IA (le plus simple)

Fonctionne avec Claude Code, ChatGPT (Codex ou conversation), Gemini, Cursor ou toute autre IA.

1. Ouvre le dossier avec l'IA.
2. Dis : « adapte ce portfolio à moi ».
3. Elle lit `INSTRUCTIONS-IA.md`, te montre d'abord à quoi ressemble le portfolio, puis te pose des questions, par petits groupes :
   - **Ton contexte** : qui tu es, ta situation, ton objectif (stage, emploi, clients...), qui va lire ton site, les langues.
   - **Ta page d'accueil** : ta phrase d'accroche (tu proposes la tienne ; si tu n'en as pas, elle t'en propose 3), le texte à côté de la photo, tes logos.
   - **Chaque projet** : ce que c'est, ton rôle, le résultat, les points clés, les outils, les captures. **Uniquement des chiffres réels.**
   - **Les couleurs de chaque projet** : fond, texte, accent. Sans avis de ta part, elle propose 3 palettes et vérifie que le texte reste lisible.
   - **La grande phrase qui s'allume** : tu proposes la tienne ; sinon elle propose 3 versions fondées sur tes vrais projets.
   - **Les options** : schéma en étapes, outils, autres projets, contact.
   - **La mise en ligne et le PDF** : Vercel, adresse du site, PDF à télécharger.
4. Elle remplit `contenu.json`, prépare les images, supprime le contenu d'exemple, lance la synchronisation et te montre le rendu sur ordinateur et mobile.

**ChatGPT dans le navigateur (sans accès aux fichiers) :**
1. Colle-lui `INSTRUCTIONS-IA.md`, puis ton `contenu.json`.
2. Réponds à ses questions.
3. Il te rend un `contenu.json` complet : remplace le contenu du fichier.
4. Il te donne la liste des images à déposer dans `img/`. Floute toi-même ce qui est confidentiel avant de les ajouter.
5. Lance `python3 sync-contenu.py`.

### Option B : à la main

1. Ouvre `contenu.json` et remplace les textes fictifs.
2. Remplace les images dans `img/` et mets leur nom dans `src`.
3. Lance la synchronisation (étape 4).

## 4. La règle à retenir

Après **chaque** modification de `contenu.json` :

```bash
python3 sync-contenu.py
```

Ce script vérifie ton JSON, signale les images introuvables, met à jour `contenu.js` (pour l'ouverture directe du fichier) et remplit les balises de partage (l'aperçu qui s'affiche sur LinkedIn, WhatsApp, Slack). Sans lui, l'aperçu de partage reste celui de l'exemple.

Sans ligne de commande : **Windows**, double-clique sur `synchroniser.bat`. **Mac**, double-clique sur `synchroniser.command` (la première fois, clic droit, puis **Ouvrir**, car le Mac demande une confirmation). Une fenêtre s'ouvre, affiche « OK » et attend que tu appuies sur une touche.

Il faut Python 3 ([python.org](https://www.python.org/downloads/)). Sous Windows, coche « Add python.exe to PATH » pendant l'installation. En ligne de commande, la commande s'appelle parfois `python` ou `py` au lieu de `python3`.

**Pourquoi cette étape ?** Le contenu est dans `contenu.json`, mais un navigateur refuse de lire un fichier voisin quand tu ouvres `index.html` par double-clic. La page lit alors `contenu.js`, une copie, que la synchronisation met à jour. Sur Vercel, ou avec `python3 -m http.server`, la page lit `contenu.json` directement : la synchronisation ne sert plus qu'à mettre à jour l'aperçu de partage (LinkedIn, WhatsApp...).

## 5. Comment les champs fonctionnent

- **Texte bilingue** : `{ "fr": "...", "en": "..." }`. Une simple chaîne vaut pour les deux langues.
- **Mise en forme** : seules les balises `<b>`, `<strong>`, `<em>`, `<i>` et `<br>` sont gardées. Dans un titre de projet, `<em>` met le mot en couleur d'accent.
- **Tout est optionnel** : un champ vide ou une section supprimée disparaît sans casser la page.
- **Projets** : autant que tu veux (1 à 4 conseillé). Chacun a ses couleurs : `fond`, `texte`, `accent`, et `fondSombre` en option. Prends un fond sombre et un texte clair.
- **Captures** : la première est la grande, les suivantes flottent autour. `"type": "mobile"` donne un cadre vertical. `"ouvrable": false` empêche de l'ouvrir en grand. `"bande": false` la retire de la bande d'images.
- **Outils** : tu définis un `catalogue` (nom, logo), puis tu écris juste `"Python"` dans les listes.
- **Sections optionnelles** : `phrase`, `schema`, `outils`, `autres`, `contact`. Retire la clé pour supprimer la section.
- **Crédit** : `site.credit.afficher: false` retire la mention « Template fait par... ».

Tous les champs sont décrits dans le [README](README.md#champs).

## 6. Les images

- Dépose-les dans `img/`, avec des noms courts, en minuscules, sans espaces.
- Captures : JPG ou WebP, 2000 px de large au maximum, idéalement moins de 400 Ko.
- Photo : rapport 4:5 (par exemple 720 × 900). Image de partage : `img/og.jpg`, 1200 × 630.
- **Floute les informations confidentielles avant** de les ajouter (noms de clients, mails, prix, visages).
- Renseigne `largeur` et `hauteur` : la page se charge mieux.
- Supprime les images d'exemple que tu n'utilises plus, y compris `img/og.jpg`, `img/profil.jpg` et les logos `ecole-exemple.svg` et `entreprise-exemple.svg` si tu ne les as pas remplacés.

## 7. Tester chez toi

```bash
python3 -m http.server 8000
```

Ouvre `http://localhost:8000`. Teste aussi `?lang=en`, le thème clair/sombre (boutons en haut à droite) et le rendu mobile (outils de développement du navigateur). Tu peux aussi double-cliquer sur `index.html` : la page lit alors `contenu.js`.

<a id="vercel"></a>

## 8. Mettre en ligne avec Vercel (fortement recommandé)

### C'est quoi ?

**Vercel est un hébergeur de sites web.** Ton portfolio est un dossier sur ton ordinateur : personne d'autre ne peut le voir. Vercel met ces fichiers sur des serveurs connectés à Internet et te donne une adresse (par exemple `prenom-nom-portfolio.vercel.app`). Un recruteur clique dessus et voit ton site.

### Pourquoi le choisir

- **Gratuit** pour un portfolio personnel (offre Hobby, usage non commercial).
- **Le plus simple** : aucune commande à lancer, le site est statique. Le template est prêt pour Vercel.
- **Mise à jour automatique** : tu modifies ton dépôt GitHub, le site se met à jour en environ une minute.
- **HTTPS inclus** (le cadenas), sans configuration.
- **Aperçu à chaque modification** : chaque changement peut être vérifié avant d'être publié.
- **Domaine personnalisé** possible (`prenom-nom.fr`), à brancher dans les réglages.

### Comment faire

Sans connaître Git, en 10 minutes environ :

1. **Crée un compte GitHub** sur [github.com](https://github.com) (**Sign up**), si tu n'en as pas.
2. **Crée un dépôt** : bouton **+** en haut à droite, puis **New repository**. Nom : `prenom-nom-portfolio`. Coche **Public**, puis **Create repository**.
3. **Envoie tes fichiers** : sur la page du dépôt vide, clique sur **uploading an existing file**. Ouvre ton dossier, sélectionne **tout son contenu** (fichiers et dossiers `img`, `fonts`, `apercu`), pas le dossier lui-même, et fais-le glisser dans la page. Attends la fin du chargement, puis **Commit changes**. `index.html` doit apparaître directement dans la liste, pas dans un sous-dossier.
4. **Crée ton compte Vercel** sur [vercel.com](https://vercel.com) : **Sign Up**, offre gratuite **Hobby**, puis **Continue with GitHub**.
5. **Importe le dépôt** : **Add New**, puis **Project**, puis **Import** à côté de `prenom-nom-portfolio`. S'il n'apparaît pas, clique sur le lien qui règle l'accès de Vercel à GitHub et autorise ce dépôt.
6. **Déploie** : ne change aucun réglage (pas de commande de build) et clique sur **Deploy**. Environ une minute après, Vercel te donne l'adresse de ton site.
7. **Finalise** : mets cette adresse dans `site.url` de `contenu.json`, synchronise (section 4), puis renvoie `contenu.json`, `contenu.js` et `index.html` sur GitHub (**Add file**, puis **Upload files** : ils remplacent les anciens). Les aperçus de partage seront alors corrects.

**Pour modifier ton site ensuite** : change tes fichiers, synchronise, renvoie-les sur GitHub de la même façon. Vercel met le site à jour tout seul en une minute.

Si tu connais Git : `git push` ou GitHub Desktop remplacent les étapes 2 et 3.

**Le nom de l'adresse.** Nom conseillé : `prenom-nom-portfolio`, pour obtenir `prenom-nom-portfolio.vercel.app`. Écris-le en minuscules, sans accents ni espaces, mots séparés par des tirets (par exemple `lea-verdier-portfolio`). L'adresse vient de ce nom : le plus simple est de le donner à ton dépôt GitHub (par exemple lors de **Use this template**) ou au projet Vercel à l'import (étape 3). Si l'adresse est déjà prise, Vercel ajoute des lettres au hasard : ajoute alors une adresse libre dans le projet Vercel, **Settings**, puis **Domains** (par exemple `prenom-nom-portfolio.vercel.app` ou une variante). Mets ensuite cette adresse dans `site.url` et synchronise (étape 6).

Le bouton **Deploy with Vercel** du README fait autre chose : il crée dans ton GitHub une copie neuve du template (avec le contenu d'exemple) et la met en ligne. C'est un raccourci si tu pars de zéro. Si tu as déjà ton dépôt, importe-le comme ci-dessus.

### Les alternatives

Si tu ne veux vraiment pas de Vercel, tout fonctionne aussi ailleurs : c'est un site statique, sans serveur à gérer. Mais Vercel reste le plus simple.

| Hébergeur | Prix | Atouts | Limites |
|---|---|---|---|
| **GitHub Pages** | Gratuit | Déjà dans GitHub. Adresse `ton-compte.github.io/ton-portfolio`. | Dépôt public sur l'offre gratuite. Réglage à activer dans **Settings**, puis **Pages**. |
| **Netlify** | Gratuit | Très proche de Vercel. Netlify Drop permet de glisser le dossier sans GitHub. | Réglages un peu différents. |
| **Cloudflare Pages** | Gratuit | Très rapide, trafic généreux. | Interface plus technique. |
| **Hébergement classique** (OVH, Hostinger...) | Payant | Domaine et hébergement au même endroit. | Envoi des fichiers à la main (FTP), pas de mise à jour automatique. |

Quel que soit l'hébergeur : pas de commande de build, et lance `python3 sync-contenu.py` **avant** d'envoyer tes fichiers.

## 9. Exporter en PDF

- **Sans rien installer** : ouvre le site, `Ctrl/Cmd + P`, « Enregistrer au format PDF », active les graphiques d'arrière-plan.
- **Avec le script** : `npm i playwright`, `npx playwright install chromium`, puis `node exporter-pdf.js`. Il crée `portfolio-fr.pdf` et `portfolio-en.pdf`. Le script lit `contenu.js` : lance `python3 sync-contenu.py` avant.
- Pour proposer le PDF en téléchargement sur le site, mets les fichiers à la racine et renseigne `contact.pdf`.

## 10. Erreurs fréquentes

| Symptôme | Cause et solution |
|---|---|
| Message « Erreur dans contenu.json » | JSON invalide (virgule finale, guillemet manquant). Lance `python3 sync-contenu.py` : il indique la ligne. |
| Message « contenu.json introuvable » | Le fichier n'est pas à côté de `index.html`, ou la page est ouverte directement sans `contenu.js` : lance `python3 sync-contenu.py`. |
| Image cassée | Mauvais chemin dans `src`. Le script le signale. |
| Aperçu de partage faux | Tu n'as pas relancé `sync-contenu.py`, ou `site.url` est vide. |
| Contenu pas à jour en ouvrant le fichier directement | `contenu.js` est périmé : relance `sync-contenu.py`. |
| Texte d'exemple qui reste | Cherche `Verdier`, `Orbite`, `Atelier Lune`, `Cartable`, `Nordwind`, `Horizon`, `mars 2027`, `exemple.com`, `example.com`, `votre-profil`, `portfolio-spie` dans le dossier. |

---

<a id="english-guide"></a>

# Complete guide (English)

## 0. Before you start: what you need

- **An AI assistant**: Claude, ChatGPT, Gemini or another. It is easier if it can read files (send it the ZIP).
- **To publish**, two free accounts, which you can create now, during the interview or at the end: **GitHub** (github.com), where your site's files are stored, and **Vercel** (vercel.com), which puts the site online. Sign up to Vercel with **Continue with GitHub**.
- **Connectors are optional.** Some AI apps (Claude, for example) can connect to your GitHub and Vercel, and then publish the site for you, with your approval. Turn them on in the app settings, connectors section. **Without connectors everything still works**: the AI guides you click by click (section 7).
- **Python**: only for the sync (section 4). If your AI can run commands, it handles it.


The portfolio is a folder of files. **All your content lives in one file: `contenu.json`**. Your images live in `img/`. You never touch the code: design, animations, light/dark theme and FR/EN are ready.

<a id="get-template"></a>

## 2. Get the template

GitHub is where the template is stored. Whichever way you choose, you end up with **a folder on your computer**: that folder becomes your portfolio.

- **Use this template** (recommended): click the green **Use this template** button on the template's GitHub page, then **Create a new repository**. You get your own repository, independent from the template. Get it onto your computer with `git clone` or GitHub Desktop.
- **Download ZIP**: **Code**, then **Download ZIP**, then unzip. To publish with Vercel later, create a GitHub repository and upload the files (**Add file**, then **Upload files**).
- **Clone directly**: `git clone https://github.com/gab-spie/portfolio-template.git my-portfolio`, then `git remote remove origin`, and link the folder to your own repository.

## 3. Fill in the content

**With an AI assistant** (Claude Code, ChatGPT/Codex, Gemini, Cursor or any other): open the folder and say "adapt this portfolio to me". It reads `INSTRUCTIONS-IA.md`, first shows you what the portfolio looks like, then interviews you step by step: your context and goal, your tagline, each project (real figures only), **the colours of each project**, the sentence that lights up on scroll, optional sections, publishing and PDF. You propose your own tagline and sentence; if you have none, it suggests three versions. It then fills `contenu.json`, prepares the images, removes the example content, runs the sync and shows you the result.

With ChatGPT in the browser (no file access): paste `INSTRUCTIONS-IA.md`, then your `contenu.json`, answer its questions, and paste back the `contenu.json` it returns. Add the listed images to `img/` (blur confidential details yourself first), then run `python3 sync-contenu.py`.

**By hand**: edit `contenu.json`, replace the images in `img/`, then run the sync.

## 4. The one rule

After **every** change to `contenu.json`:

```bash
python3 sync-contenu.py
```

It validates your JSON, flags missing images, refreshes `contenu.js` (used when you open the file directly) and fills the share tags (the preview shown on LinkedIn, WhatsApp, Slack).

No command line needed: on **Windows** double-click `synchroniser.bat`; on **Mac** double-click `synchroniser.command` (the first time, right-click, then **Open**). **Why this step?** The content lives in `contenu.json`, but a browser refuses to read a neighbouring file when you open `index.html` by double-click, so the page reads `contenu.js`, a copy that the sync refreshes. On Vercel or with `python3 -m http.server`, the page reads `contenu.json` directly and the sync only refreshes the share preview. Without it, the share preview stays the example one.

You need Python 3 ([python.org](https://www.python.org/downloads/)). On Windows, the command is sometimes `python` or `py` instead of `python3`.

## 5. Fields and images

All fields are described in the [README](README.md#fields). In short: texts are strings or `{ "fr", "en" }`, every field is optional, each project has its own colours (dark background, light text), `"ouvrable": false` stops an image from opening full size, and removing a key removes its section. Put images in `img/` (JPG or WebP, under about 400 KB), blur confidential details first, and delete unused example images, including `img/og.jpg`, `img/profil.jpg` and the example school and company logos.

## 6. Test locally

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

Also try `?lang=en`, the theme buttons (top right) and a mobile view. Double-clicking `index.html` works too: the page then reads `contenu.js`.

<a id="vercel-en"></a>

## 7. Publish with Vercel (strongly recommended)

**Vercel is a web hosting service.** Your portfolio is just files on your computer. Vercel puts them on servers connected to the internet and gives you an address such as `firstname-lastname-portfolio.vercel.app`.

Why we recommend it:
- **Free** for a personal portfolio (Hobby plan, non-commercial use).
- **The simplest option**: no command to run, the template is a static site.
- **Automatic updates**: push to GitHub and the site updates in about a minute.
- **HTTPS included**, no configuration.
- **A preview for every change**, before it goes live.
- **Custom domain** supported.

How to, without Git (about 10 minutes):
1. **Create a GitHub account** at [github.com](https://github.com) (**Sign up**) if you have none.
2. **Create a repository**: **+** at the top right, **New repository**, name `firstname-lastname-portfolio`, **Public**, **Create repository**.
3. **Upload your files**: on the empty repository page, click **uploading an existing file**, select **everything inside** your folder (files and the `img`, `fonts`, `apercu` folders), not the folder itself, drag it into the page, wait, then **Commit changes**. `index.html` must appear directly in the list.
4. **Create your Vercel account** at [vercel.com](https://vercel.com): **Sign Up**, free **Hobby** plan, **Continue with GitHub**.
5. **Import**: **Add New**, **Project**, **Import** next to your repository. If it is missing, use the link that adjusts Vercel's access to GitHub and allow this repository.
6. **Deploy**: change nothing (no build command), click **Deploy**. About a minute later you get your address.
7. **Finish**: put the address in `site.url`, sync (section 4), and upload `contenu.json`, `contenu.js` and `index.html` again (**Add file**, **Upload files**: they replace the old ones).

To update the site later: edit, sync, upload the changed files the same way. Vercel updates the site in about a minute. If you know Git, `git push` or GitHub Desktop replace steps 2 and 3.

**The address name.** Suggested name: `firstname-lastname-portfolio`, to get `firstname-lastname-portfolio.vercel.app`. Write it in lowercase, without accents or spaces, words separated by hyphens (for example `lea-verdier-portfolio`). The address comes from this name: the simplest is to give it to your GitHub repository (for example with **Use this template**) or to the Vercel project when importing (step 3). If the address is already taken, Vercel adds random letters: then add a free address in the Vercel project, **Settings**, then **Domains** (for example `firstname-lastname-portfolio.vercel.app` or a variant). Then put this address in `site.url` and sync (step 6).

Note: the **Deploy with Vercel** button in the README does something else. It creates a fresh copy of the template (with the example content) in your GitHub and deploys it. Use it as a shortcut when starting from scratch. If you already have your repository, import it as above.

Alternatives, if you really do not want Vercel (it is a static site, so it works anywhere):
- **GitHub Pages**: free, built into GitHub, public repository on the free plan. Turn it on in **Settings**, then **Pages**.
- **Netlify**: free and very similar. Netlify Drop lets you drag the folder in without GitHub.
- **Cloudflare Pages**: free and fast, with a more technical interface.
- **Classic hosting** (OVH, Hostinger...): paid, files uploaded by hand over FTP, no automatic updates.

Vercel remains the simplest. Whatever you pick: no build command, and run `python3 sync-contenu.py` before uploading.

## 8. Export a PDF

Open the site and print to PDF (enable background graphics). Or run `npm i playwright`, `npx playwright install chromium`, then `node exporter-pdf.js` to get `portfolio-fr.pdf` and `portfolio-en.pdf`. The script reads `contenu.js`, so run `python3 sync-contenu.py` first. To offer the PDF on the site, put the files at the root and fill in `contact.pdf`.

## 9. Common problems

- **"Erreur dans contenu.json" message**: invalid JSON (trailing comma, missing quote). Run `python3 sync-contenu.py`: it tells you the line.
- **"contenu.json introuvable" message**: the file is not next to `index.html`, or the page is opened directly without `contenu.js`. Run `python3 sync-contenu.py`.
- **Broken image**: wrong path in `src`. The script flags it.
- **Wrong share preview**: you did not run `sync-contenu.py`, or `site.url` is empty.
- **Direct file opening shows old content**: `contenu.js` is stale. Run the sync.
- **Example text left**: search the folder for `Verdier`, `Orbite`, `Atelier Lune`, `Cartable`, `Nordwind`, `Horizon`, `mars 2027`, `exemple.com`, `example.com`, `votre-profil`, `portfolio-spie`.
