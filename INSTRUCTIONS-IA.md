# Consignes pour l'IA : adapter ce portfolio à la personne

Ce fichier est écrit pour n'importe quelle IA : Claude Code, ChatGPT (Codex ou conversation), Gemini, Cursor, etc.
Lis-le en entier avant de faire quoi que ce soit. Parle à la personne en français, sauf si elle écrit dans une autre langue : réponds alors dans sa langue.

## Ce qu'est ce dossier

Un portfolio dont **tout le contenu** est dans un seul fichier : `contenu.json`. La page se construit toute seule à partir de ce fichier.
La personne n'a jamais à toucher au code. Toi non plus.

Tu peux modifier : `contenu.json` et le dossier `img/` (dont `img/logos/`).
Tu ne modifies **pas** `index.html` (design et animations), sauf si la personne le demande explicitement.
Après chaque modification de `contenu.json`, lance `python3 sync-contenu.py`. Ce script régénère `contenu.js` et réécrit seul les balises de partage entre `<!-- meta:start -->` et `<!-- meta:end -->` dans `index.html`. C'est normal : ne fais pas ces changements à la main.

Le contenu d'exemple (Léa Verdier, Orbite, Atelier Lune, Cartable, Nordwind Labs, Institut Horizon) est **100 % fictif**.
Il doit disparaître entièrement : textes, images, logos d'exemple, chiffres d'exemple. Il ne reste rien de lui à la fin.

## Règle d'or : tu ne connais pas cette personne

Le template sert à n'importe qui : étudiant, salarié, freelance, designer, développeur, chercheur, artisan, responsable marketing, juriste, enseignant...
Ne suppose rien : ni le métier, ni le niveau technique, ni que les projets sont des projets web ou d'IA.
L'exemple (une étudiante en gestion qui fait des outils web) n'est pas un modèle. N'en reprends ni le ton, ni la structure des projets, ni les outils.
Un « projet » peut être un site, une étude, un mémoire, une campagne, un événement, une création, un produit, une mission de stage.
**Commence par montrer l'aperçu (étape 0), puis pose des questions.** Ne remplis rien avant d'avoir compris le contexte.
N'invente jamais un chiffre, un nom, un résultat, un diplôme ou un client. Si la personne n'a pas de chiffre, n'en mets pas.

## Étape 0. Montre d'abord à quoi ressemble le portfolio

La personne ne connaît pas le résultat. Avant toute question, **montre-lui le portfolio**, sinon elle répond à l'aveugle.

1. **Si tu peux lancer des commandes et ouvrir un navigateur** : lance `python3 -m http.server 8000` dans le dossier, ouvre `http://localhost:8000` et dis-lui de faire défiler la page. Si tu ne peux pas ouvrir de navigateur, prends des captures (Playwright, par exemple) et montre-les, ou dis-lui d'ouvrir `index.html` par double-clic.
2. **Si tu ne peux pas lancer de commandes** (conversation seule) : montre les images du dossier `apercu/` si tu peux les afficher (`accueil.jpg`, `projet-1.jpg`, `projet-2.jpg`, `projet-3.jpg`, `outils.jpg`, `accueil-sombre.jpg`, `mobile.jpg`). Sinon, donne le lien de l'aperçu : https://github.com/gab-spie/portfolio-template#readme, et demande-lui de l'ouvrir avant de continuer.
3. **Décris ce qu'elle voit**, en mots simples, section par section :
   - **L'accueil** : son nom en très grand, une phrase d'accroche, une photo, des logos (école, entreprise), un bouton vers les projets.
   - **Une bande d'images** qui défile en dessous, avec des captures de ses projets.
   - **Une grande phrase** qui s'allume mot par mot quand on descend.
   - **Les projets** : une grande carte par projet, chacune avec sa propre couleur. La page entière change de couleur à chaque projet.
   - **Un schéma en étapes** (optionnel) : un fonctionnement présenté en 2 à 4 étapes.
   - **Ses outils** : un clavier où chaque touche affiche une explication, et deux bandes d'outils qui défilent.
   - **D'autres projets** plus petits (optionnel), puis **un contact**.
   - Le site existe en **clair, sombre ou automatique**, en **français et en anglais**, et sur mobile.
4. **Précise que tout ce qu'elle voit est fictif** (la personne, les projets, les chiffres) : ce sera remplacé par son contenu.
5. **Demande-lui** si ce style lui convient et quelles sections elle veut garder (schéma, outils, autres projets, contact). Le design et les animations ne changent pas : seul le contenu change. Puis passe à l'étape 1.

## Étape 1. L'entretien

**Rythme, à respecter strictement :**
- **Au début de l'entretien, annonce le déroulé** en deux phrases : les parties à venir (A. toi, B. accueil, C. projets, D. phrase de synthèse, E. sections optionnelles, F. mise en ligne), le temps approximatif (20 à 30 minutes), et qu'à la fin le site sera prêt à être mis en ligne.
- Ne montre **jamais** la liste complète des questions. Pose **3 questions au plus par message**, puis **attends les réponses** avant de continuer.
- Avance partie par partie : A, B, C, D, E, F.
- Pour les projets (partie C), traite **un projet à la fois** : d'abord de quoi il s'agit et son rôle, puis le résultat et les points clés, puis les images et les couleurs.
- Reformule ce que tu as compris avant de passer à la suite.
- Si la personne a rempli [QUESTIONNAIRE.md](QUESTIONNAIRE.md), lis-le d'abord. Ne repose pas ce qu'elle a déjà répondu : pose seulement les questions restantes, puis propose les phrases et les palettes de couleurs.
Pose des questions ouvertes. Ne glisse pas de réponse dans la question (« tu as sûrement utilisé Python ? »). Ne pousse pas vers un secteur, un outil ou un style. Si une réponse est floue, demande un exemple concret.

### A. Contexte
1. Prénom et nom, tels qu'ils doivent apparaître.
2. Situation actuelle : étudiant (quelle formation), en poste, en recherche, indépendant... Domaine ou métier visé.
3. Pourquoi ce portfolio : trouver un stage, un emploi, des clients, être admis dans une école, présenter un travail ? Qui va le lire (recruteurs, clients, jury) ?
4. Langues du site : français et anglais, ou une seule ? Langue par défaut ?
5. Un ton souhaité : sobre, chaleureux, direct, créatif ?

### B. Page d'accueil
6. La phrase d'accroche (`identite.accroche`, sous le nom). Demande d'abord à la personne d'écrire la sienne, même maladroite, puis aide-la à la resserrer. Si elle n'en a pas, propose 3 versions courtes fondées sur ses réponses, et laisse-la choisir ou corriger. Si la phrase parle d'IA, entoure le mot de doubles crochets : `[[IA]]` en français, `[[AI]]` en anglais (un seul par langue). Au survol des lettres i et a du nom, une flèche rouge relie ces lettres au mot. Sans marqueur, la flèche écrit « IA » à la main près du nom. Explique-le à la personne en une phrase.
7. Un court texte à côté de la photo (`identite.texte` : formation, poste actuel). Une photo : oui ou non ? (portrait 4:5 recommandé). **Dis tout de suite où la déposer** : dans le dossier `img/`, par exemple `img/profil.jpg` (elle remplace la photo d'exemple).
8. Logos d'école ou d'entreprise à afficher (`identite.logos`) ? Ils doivent être fournis par la personne (SVG ou PNG transparent). Optionnel. **Dis où les déposer** : dans `img/logos/`, un fichier par logo.
9. Faut-il afficher « mis à jour le... » ? Si oui, mets la date du jour dans `site.miseAJour` (`AAAA-MM-JJ`). Sinon, retire la clé.

### C. Les projets principaux
10. Combien de projets veut-elle mettre en avant ? Conseille 1 à 4 pour garder un site lisible, mais n'en limite pas le nombre : le site s'adapte (1 seul est possible, davantage aussi).
11. Pour **chaque** projet :
    - Nom court (`nom`, sert dans la bande d'images).
    - De quoi s'agit-il, pour qui, dans quel contexte (école, entreprise, projet personnel, client) ?
    - Quel était son rôle exact ?
    - Le résultat (`resultat`) : une phrase forte. **Chiffres réels uniquement**, avec leur période de mesure. Sinon, un résultat qualitatif honnête.
    - 2 à 5 points clés (`points` : ce qui a été fait, concrètement).
    - Ce qu'elle a appris (`appris`, une phrase, optionnel).
    - Outils ou méthodes utilisés (`outils`, optionnel).
    - Captures ou visuels disponibles. **Dis où les déposer** : dans le dossier `img/`, avec un nom court sans espaces (`nom-du-projet-accueil.jpg`), et demande-lui de te donner les noms de fichiers. Sont-ils confidentiels ? Faut-il flouter des noms, des prix, des visages, des données clients ?
    - Une image doit-elle rester non ouvrable en grand ? (`"ouvrable": false`)
    - Un logo ou un nom de marque pour la carte (`marque`) ? Soit un logo fourni, soit un petit mot-symbole en texte, soit rien.
12. **Les couleurs de chaque projet** (`couleurs`, à demander projet par projet). **Quand tu poses la question, rappelle toujours que le fond doit être sombre** (le texte est clair) et explique en une phrase à quoi servent les trois couleurs : le fond de la page quand on arrive sur ce projet, le texte, et l'accent (titres, puces, chiffres). Si la personne n'a aucune idée, ne lui laisse pas chercher : propose-lui tout de suite 3 palettes.
    - `fond` : couleur de fond. Elle doit être sombre : sur une carte, l'interface passe en mode sombre et les logos noirs s'inversent en blanc.
    - `texte` : couleur du texte, claire.
    - `accent` : couleur d'accent (résultat, mots en `<em>` du titre, chiffres, traits).
    - `fondSombre` (option) : un fond un peu différent pour le thème sombre.
    Demande d'abord si la personne a des couleurs en tête (sa marque, celle du client, une couleur qu'elle aime). Si elle n'a pas d'avis, propose 3 palettes cohérentes avec l'univers du projet, chacune décrite en mots (« bleu nuit avec un accent vert ») et avec ses trois codes `#rrggbb` (fond, texte, accent). Varie-les d'un projet à l'autre et n'en reprends pas les couleurs de l'exemple. Laisse-la choisir ou ajuster.
    Vérifie le contraste : au moins 4,5 pour 1 entre `texte` et `fond`, au moins 3 pour 1 entre `accent` et `fond` (et `fondSombre` s'il existe). Si une couleur demandée ne passe pas, dis-le et propose la teinte la plus proche qui passe. Deux projets voisins ne doivent pas avoir la même couleur de fond.

### D. La phrase qui s'allume au défilement
13. Cette grande phrase (`phrase`) résume en une ligne le fil rouge des projets, par exemple « un problème, une solution » ou « trois situations, trois outils ». Elle doit venir du parcours **réel** de la personne. C'est du texte brut : pas de balises.
    Demande d'abord à la personne de proposer sa propre phrase, même maladroite. Si elle n'en a pas, propose 3 versions à partir de ses projets, laisse-la choisir ou corriger. N'en garde pas une générique.

### E. Sections optionnelles (une section sans contenu disparaît)
14. **Schéma en étapes** (`schema`) : un fonctionnement en 2 à 4 étapes (une méthode, une chaîne d'outils, un processus de travail). Utile si la personne a un dispositif à expliquer. Sinon, supprime la clé `schema`.
15. **Outils** (`outils`) : 6 à 20 outils, logiciels ou compétences réellement utilisés, avec pour chacun une catégorie courte (`categorie`) et une phrase sur l'usage (`texte`). Ce peut être des outils de design, de gestion, de recherche, de code... Pour afficher un logo, ajoute l'outil dans `catalogue` avec le chemin du logo. Quelques logos sont déjà dans `img/logos/`. Sans logo, le nom s'affiche seul. Sinon, supprime la clé `outils`.
16. **Autres projets** (`autres`) : projets plus petits, avec ou sans image, avec `taille` et `miseEnPage` au choix (voir le README). Sinon, supprime la clé `autres`.
17. **Contact** (`contact`) : e-mail, LinkedIn, autres liens. La grande phrase du bloc contact va dans `contact.titre`. **Elle dépend de l'objectif donné en partie A** : ne reprends jamais celle de l'exemple (un stage de 6 mois à partir de mars 2027). Demande à la personne ce qu'elle veut dire aux visiteurs, et propose-lui une phrase adaptée si elle n'a pas d'idée, par exemple « Disponible pour un CDI à partir de septembre », « Ouvert aux missions en freelance », « À la recherche d'une alternance en marketing », « Une idée de projet ? Écrivez-moi. ». S'il n'y a ni date ni recherche en cours, ne mets pas de date. Un PDF du portfolio ? (`contact.pdf`, voir le README pour l'exporter)
18. Adresse finale du site si elle la connaît (`site.url`), pour les aperçus de partage. Remplace dans tous les cas l'adresse de la démo du template (`portfolio-spie.vercel.app`) : par la sienne, ou par une chaîne vide si elle ne la connaît pas encore.
19. Mention « Template fait par... » en bas de page (`site.credit`) : la laisser, ou la retirer avec `"afficher": false`.

### F. Mise en ligne et PDF
20. Veux-tu mettre le site en ligne, avec une adresse que tu peux donner à des recruteurs ou des clients ? Explique en deux phrases ce qu'est Vercel (un hébergeur gratuit pour un portfolio, sans commande, qui met le site à jour à chaque modification) et recommande-le. Demande si elle a déjà un compte GitHub (gratuit, nécessaire pour Vercel). Précise que tu ne créeras aucun compte et ne publieras rien sans son accord.
21. Veux-tu un nom de domaine à toi (`prenom-nom.fr`, payant) ou une adresse en `.vercel.app` (gratuite) ? Pour l'adresse gratuite, recommande le nom `prenom-nom-portfolio` (en minuscules, sans accents ni espaces, mots séparés par des tirets, par exemple `lea-verdier-portfolio`), pour obtenir `prenom-nom-portfolio.vercel.app`.
22. Veux-tu aussi un PDF du portfolio, en français et en anglais, à proposer en téléchargement sur le site ? Si oui, renvoie vers « Exporter en PDF » dans le README.

## Étape 2. Remplir `contenu.json`

- Garde exactement la structure du fichier d'exemple. Les champs sont décrits dans le [README](README.md#champs).
- Chaque texte est soit une chaîne, soit `{ "fr": "...", "en": "..." }`. Traduis toi-même vers l'autre langue si la personne le veut, et fais-lui relire.
- Site dans une seule langue : écris de simples chaînes, mets `site.langueParDefaut` sur cette langue (`"fr"` ou `"en"`) et `site.boutonLangue` sur `false`.
- Remplis aussi `site.titre`, `site.description` et `site.imagePartage` : ils servent aux aperçus de partage.
- Dans les textes, seules ces balises sont gardées : `<b>`, `<strong>`, `<em>`, `<i>`, `<br>`. Dans un titre de projet, `<em>` met le mot en couleur d'accent. Dans `appris`, écris le libellé toi-même (`<b>Ce que j'ai appris :</b> ...`).
- Écris court et concret. Pas de formules creuses (« passionné », « dynamique », « solutions innovantes »). Une phrase, une idée.
- Le nombre de projets, de points, de captures et d'outils est libre. Supprime les éléments d'exemple en trop, ne les laisse pas.
- Supprime les clés des sections inutilisées plutôt que de laisser des textes d'exemple. Retire du `catalogue` les outils que la personne n'utilise pas.
- Les chiffres : uniquement ceux fournis par la personne. Ajoute la période ou la source dans `noteChiffres`. Retire la note d'exemple « Chiffres d'exemple ».
- Garde le JSON valide (guillemets doubles, pas de virgule finale).

## Étape 3. Les images

- Les images vont dans `img/`. Noms courts en minuscules, sans espaces : `mon-projet-accueil.jpg`.
- Formats : JPG ou WebP pour les captures (qualité 80, 2000 px de large maximum, moins de 400 Ko si possible), SVG ou PNG transparent pour les logos.
- Renseigne `largeur` et `hauteur` en pixels quand tu les connais : la page se charge mieux.
- Portrait : rapport 4:5 (par exemple 720 × 900). Image de partage : `img/og.jpg`, 1200 × 630.
- La première capture d'un projet est la grande : ne la mets pas en `"type": "mobile"`. Une capture mobile suivante s'indique avec `"type": "mobile"` (cadre vertical).
- Floute ce qui est confidentiel (noms de clients, mails, prix, données personnelles, visages) **avant** de mettre l'image dans `img/`. Montre le résultat à la personne. Si tu ne peux pas modifier d'images, dis-lui précisément quoi flouter.
- Mets `"ouvrable": false` sur les images qui ne doivent pas être agrandies ou téléchargées facilement.
- Si la personne n'a pas encore d'images : utilise un visuel neutre qu'elle remplacera, et dis-le-lui clairement. Ne garde jamais les captures d'exemple.
- À la fin, supprime de `img/` toutes les images d'exemple qui ne sont plus utilisées (y compris `og.jpg` et `profil.jpg` s'ils n'ont pas été remplacés), et de `img/logos/` les logos inutiles (dont `ecole-exemple.svg` et `entreprise-exemple.svg`).

## Étape 4. Vérifier

1. `python3 sync-contenu.py` doit répondre « OK » sans aucune ligne « Attention ». Corrige chaque avertissement.
2. Lance un serveur local : `python3 -m http.server 8000`, puis ouvre `http://localhost:8000`.
3. Si tu as un navigateur ou Playwright, prends des captures : ordinateur (1440 × 900), mobile (390 × 844), thème clair et sombre, `?lang=en`. Vérifie : aucune erreur dans la console, aucun débordement horizontal, aucune image cassée, pas de texte coupé. Sans navigateur, dis-le et demande à la personne de vérifier ces points.
4. Fais défiler les cartes projets : la couleur de la page doit suivre chaque projet, et le texte doit rester lisible.
5. Recherche dans le dossier tout reste du contenu d'exemple : `Verdier`, `Léa`, `Orbite`, `Atelier Lune`, `Cartable`, `Nordwind`, `Horizon`, `exemple.com`, `example.com`, `votre-profil`, `portfolio-spie`, `Chiffres d'exemple`, `mars 2027`. Il ne doit rien rester dans `contenu.json`, `contenu.js`, les balises de partage d'`index.html` ni `img/`.
6. Relis chaque chiffre avec la personne : il doit venir d'elle.
7. Montre les captures à la personne et propose des ajustements.

## Étape 5. Mise en ligne

Recommande fortement Vercel et explique-le en quelques phrases : c'est un hébergeur qui met le site sur Internet avec une adresse `prenom-nom-portfolio.vercel.app`, gratuit pour un portfolio personnel, sans commande, et mis à jour à chaque envoi sur GitHub.
Marche à suivre : mettre le dossier dans un dépôt GitHub, puis sur vercel.com, **Add New**, **Project**, choisir ce dépôt, **Deploy**. Ensuite, mettre l'adresse obtenue dans `site.url` et relancer `python3 sync-contenu.py`.
Nom de l'adresse : recommande `prenom-nom-portfolio` (minuscules, sans accents ni espaces, mots séparés par des tirets). L'adresse vient de ce nom : le plus simple est de nommer ainsi le dépôt GitHub (par exemple lors de **Use this template**) ou le projet Vercel à l'import. Si l'adresse est déjà prise, Vercel ajoute des lettres au hasard : on peut alors ajouter une adresse libre dans le projet Vercel, **Settings**, puis **Domains** (par exemple `prenom-nom-portfolio.vercel.app` ou une variante). Puis mettre cette adresse dans `site.url` et synchroniser.
Si la personne ne veut pas de Vercel, cite les alternatives : GitHub Pages, Netlify, Cloudflare Pages, ou un hébergement classique (OVH, Hostinger...). Détails dans [GUIDE.md](GUIDE.md#vercel).
Rappelle de relancer `python3 sync-contenu.py` avant chaque envoi.
Explique à la personne qu'après chaque modification de `contenu.json` elle doit synchroniser : double-clic sur `synchroniser.bat` (Windows) ou `synchroniser.command` (Mac), ou `python3 sync-contenu.py`. Sans cela, une page ouverte par double-clic affiche l'ancien contenu.
**Ne publie rien, ne pousse rien et ne crée aucun compte sans l'accord explicite de la personne.**

## Mode « conversation seule » (ChatGPT web et assimilés, sans accès aux fichiers)

Si tu ne peux pas lire ni écrire de fichiers :
1. Si la personne ne t'a pas collé le `contenu.json` d'origine, demande-le-lui avant de commencer : tu en as besoin pour respecter la structure.
2. Fais l'entretien de l'étape 1, avec les mêmes règles (questions ouvertes, couleurs par projet, phrases proposées par la personne, chiffres réels seulement).
3. Produis **un seul bloc de code JSON** : le `contenu.json` complet, valide, copiable tel quel, sans aucun reste de l'exemple. S'il est trop long pour une seule réponse, découpe-le en parties clairement numérotées et dis comment les recoller.
4. Donne la liste exacte des images à préparer : nom de fichier, dimensions, et ce qu'il faut flouter. Elles vont dans `img/`.
5. Explique en quelques lignes : remplacer le contenu de `contenu.json`, déposer les images dans `img/`, supprimer les images d'exemple, lancer `python3 sync-contenu.py`. Sans ce script, les aperçus de partage et `contenu.js` restent ceux de l'exemple.
6. Termine par la mise en ligne (étape 5) et la liste de vérification de l'étape 4, que la personne fera elle-même.

## À ne jamais faire

- Inventer des chiffres, des clients, des diplômes ou des témoignages.
- Écrire à la place de la personne son accroche ou sa grande phrase sans lui avoir d'abord demandé la sienne.
- Garder du contenu d'exemple (textes, images, logos, chiffres).
- Modifier le design ou le code sans demande explicite.
- Mettre en ligne des images confidentielles non floutées.
- Publier, pousser ou envoyer quoi que ce soit sans l'accord de la personne.
