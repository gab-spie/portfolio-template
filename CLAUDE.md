# Adapter ce portfolio à l'utilisateur

Quand l'utilisateur dit « adapte ce portfolio à moi » (ou équivalent), suis **à la lettre** le fichier [INSTRUCTIONS-IA.md](INSTRUCTIONS-IA.md). Lis-le en entier d'abord.

Résumé :
- Commence par un entretien ouvert et sans a priori : contexte, objectif, public, puis projets, **couleurs de chaque projet** (avec contraste vérifié), phrase d'accroche et phrase qui s'allume proposées d'abord par l'utilisateur, sections optionnelles. Tu ne connais pas cette personne : ne suppose rien, et ne prends pas l'exemple comme modèle.
- Tu modifies seulement `contenu.json` et `img/`. Jamais `index.html` sans demande explicite (le script de synchronisation met à jour seul ses balises de partage).
- Chiffres réels uniquement. Captures confidentielles à flouter avant de les ajouter.
- Efface tout le contenu d'exemple (Léa Verdier, Orbite, Atelier Lune, Cartable, Nordwind Labs, Institut Horizon), y compris les images et logos d'exemple.
- Après chaque changement : `python3 sync-contenu.py`.
- Vérifie le rendu sur ordinateur et mobile, en clair et en sombre, en FR et en EN, puis montre des captures.
- Recommande Vercel pour la mise en ligne. Ne pousse et ne publie rien sans accord.
