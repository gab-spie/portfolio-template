# Quelle IA utiliser, et quoi lui écrire

[English version below](#english)

Choisis ton IA dans la liste, puis copie le message qui va avec. Chaque message est adapté à ce que l'outil sait faire.

Avant tout : télécharge le template. Sur la page GitHub, bouton vert **Code**, puis **Download ZIP**.

| Ton outil | Ce qu'il fait seul | Mise en ligne |
|---|---|---|
| **Claude Code** (application Claude pour ordinateur, onglet Code, ou terminal) | Tout : fichiers, aperçu, synchronisation | Peut créer le dépôt GitHub et lancer Vercel avec ton accord |
| **ChatGPT pour ordinateur, mode Codex** | Tout : fichiers, aperçu, synchronisation | Peut déployer avec le plugin Vercel, avec ton accord |
| **Claude Cowork** (application Claude pour ordinateur) | Modifie les fichiers de ton dossier | Il te guide, tu cliques |
| **Claude.ai** (site ou application, gratuit ou payant) | Ouvre le ZIP et te rend un ZIP terminé | Il te guide, tu cliques |
| **ChatGPT** (site ou application, gratuit ou payant) | Ouvre le ZIP et te rend un ZIP terminé | Il te guide, tu cliques |
| **Gemini, Cursor, autre** | Selon l'outil | Il te guide, tu cliques |

Le plus confortable : **Claude Code** ou **ChatGPT pour ordinateur en mode Codex**, car ils travaillent directement dans ton dossier. Le plus simple à lancer : **Claude.ai** ou **ChatGPT** dans le navigateur.

## 1. Claude.ai (site ou application)

**Avant** : dans Claude, ouvre **Paramètres**, puis **Capacités**, et active la création et la modification de fichiers (exécution de code). C'est disponible aussi en gratuit.

Envoie le ZIP en pièce jointe avec ce message :

```
Voici le ZIP d'un modèle de portfolio. Je veux que tu l'adaptes à moi.

1. Ouvre le ZIP avec ton outil de code, puis lis en entier le fichier INSTRUCTIONS-IA.md et suis-le à la lettre.
2. Commence par me dire ce que tu peux faire ici et ce qu'il me faudra pour la mise en ligne.
3. Montre-moi à quoi ressemble le portfolio (images du dossier apercu/), puis pose-moi les questions par petites parties.
4. Après chaque modification de contenu.json, lance python3 sync-contenu.py.
5. À la fin, rends-moi le dossier complet en un seul ZIP, avec index.html à la racine, puis guide-moi pour la mise en ligne, une étape à la fois.

Je ne suis pas développeur : explique-moi simplement chaque étape.
```

Si Claude ne peut pas ouvrir le ZIP : envoie à la place `INSTRUCTIONS-IA.md` et `contenu.json` (dans le dossier décompressé), avec le message du point 6.

## 2. ChatGPT (site ou application)

En gratuit, ChatGPT n'accepte que quelques fichiers par jour : envoie un seul fichier, le ZIP. Il n'y a rien à connecter.

```
Voici le ZIP d'un modèle de portfolio. Je veux que tu l'adaptes à moi.

1. Ouvre le ZIP avec Python, puis lis en entier le fichier INSTRUCTIONS-IA.md et suis-le à la lettre.
2. Commence par me dire ce que tu peux faire ici et ce qu'il me faudra pour la mise en ligne.
3. Montre-moi à quoi ressemble le portfolio (images du dossier apercu/), puis pose-moi les questions par petites parties.
4. Après chaque modification de contenu.json, lance python3 sync-contenu.py.
5. À la fin, rends-moi le dossier complet en un seul ZIP téléchargeable, avec index.html à la racine, puis guide-moi pour la mise en ligne, une étape à la fois.

Je ne suis pas développeur : explique-moi simplement chaque étape.
```

Si ChatGPT ne peut pas ouvrir le ZIP : envoie à la place `INSTRUCTIONS-IA.md` et `contenu.json`, avec le message du point 6.

## 3. Claude Code (application Claude pour ordinateur, onglet Code, ou terminal)

Décompresse le ZIP, puis ouvre le dossier dans Claude Code. Il lit les consignes tout seul. Écris simplement :

```
Adapte ce portfolio à moi.
```

## 4. ChatGPT pour ordinateur, mode Codex

Décompresse le ZIP. Dans l'application ChatGPT pour ordinateur, choisis **Codex**, ouvre le dossier, puis écris :

```
Lis AGENTS.md et INSTRUCTIONS-IA.md en entier, puis adapte ce portfolio à moi en suivant ces consignes à la lettre.
```

## 5. Claude Cowork, Gemini, Cursor ou une autre IA qui ouvre un dossier

Décompresse le ZIP, donne le dossier à l'IA, puis écris :

```
Lis INSTRUCTIONS-IA.md en entier, puis adapte ce portfolio à moi en suivant ces consignes à la lettre. Je ne suis pas développeur : explique-moi simplement chaque étape.
```

## 6. Si l'IA ne peut ouvrir aucun fichier

Envoie `INSTRUCTIONS-IA.md` et `contenu.json` (ou colle leur contenu), puis :

```
Voici les consignes (INSTRUCTIONS-IA.md) et le fichier de contenu (contenu.json) d'un modèle de portfolio. Suis les consignes à la lettre, section « Mode conversation seule » : pose-moi les questions par petites parties, puis rends-moi le contenu.json complet et la liste des images à ajouter. Je ne suis pas développeur : explique-moi simplement chaque étape.
```

Remplace ensuite `contenu.json` dans ton dossier par celui qu'elle te rend, ajoute tes images dans `img/`, et double-clique sur `synchroniser.bat` (Windows) ou `synchroniser.command` (Mac).

## Pour mettre en ligne

L'IA te guide. Deux chemins, détaillés dans [GUIDE.md](GUIDE.md#vercel) :
- **GitHub puis Vercel** (recommandé) : environ 10 minutes, et ensuite ton site se met à jour chaque fois que tu renvoies tes fichiers sur GitHub.
- **Vercel Drop**, le plus rapide : sur [vercel.com/drop](https://vercel.com/drop), tu glisses ton dossier et c'est en ligne. Pour une mise à jour, il faut recommencer (voir le guide).

<a id="english"></a>

# Which AI to use, and what to write (English)

Download the template first: green **Code** button, then **Download ZIP**.

- **Claude.ai** (website or app): in **Settings**, **Capabilities**, turn on file creation (code execution). Attach the ZIP and write: *"Here is the ZIP of a portfolio template. Adapt it to me. Open the ZIP with your code tool, read INSTRUCTIONS-IA.md in full and follow it exactly. First tell me what you can do here and what I will need to publish. Show me the portfolio (images in apercu/), then ask me the questions in small groups. Run python3 sync-contenu.py after each change to contenu.json. At the end, give me the whole folder as one ZIP with index.html at the root, then guide me to publish it, one step at a time. I am not a developer: explain each step simply."*
- **ChatGPT** (website or app): send only the ZIP (the free plan allows few files per day) with the same message, replacing "your code tool" with "Python". Nothing to connect.
- **Claude Code**: unzip, open the folder, write *"Adapt this portfolio to me."*
- **ChatGPT desktop, Codex mode**: unzip, open the folder, write *"Read AGENTS.md and INSTRUCTIONS-IA.md in full, then adapt this portfolio to me following them exactly."*
- **Claude Cowork, Gemini, Cursor or any AI that opens a folder**: *"Read INSTRUCTIONS-IA.md in full, then adapt this portfolio to me following it exactly."*
- **An AI that cannot open files**: send INSTRUCTIONS-IA.md and contenu.json, and ask it to follow the "Mode conversation seule" section.

To publish: GitHub then Vercel (recommended, updates automatically), or [Vercel Drop](https://vercel.com/drop) (fastest: drag your folder). Details in [GUIDE.md](GUIDE.md#vercel-en).
