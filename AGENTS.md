# Instructions pour les agents (Codex, ChatGPT, Gemini, Cursor et autres)

Ce dossier est un template de portfolio piloté par un seul fichier de contenu : `contenu.json`.

Si l'utilisateur demande d'adapter ce portfolio à lui, lis en entier [INSTRUCTIONS-IA.md](INSTRUCTIONS-IA.md) et suis-le : entretien d'abord (contexte, objectif, projets, couleurs par projet avec contraste vérifié, phrase d'accroche et phrase qui s'allume proposées d'abord par la personne), puis remplissage de `contenu.json`, préparation des images dans `img/`, `python3 sync-contenu.py`, vérification du rendu.
Sans accès aux fichiers, suis la section « Mode conversation seule » de ce même fichier.

Règles essentielles :
- Ne modifie que `contenu.json` et `img/`. Pas `index.html` sans demande explicite (le script de synchronisation met à jour seul ses balises de partage).
- Chiffres réels uniquement. Rien d'inventé.
- Floute les informations confidentielles des captures avant de les ajouter.
- Supprime tout le contenu d'exemple (Léa Verdier, Orbite, Atelier Lune, Cartable, Nordwind Labs, Institut Horizon), y compris les images et logos d'exemple.
- Recommande Vercel pour la mise en ligne. Ne publie et ne pousse rien sans l'accord de l'utilisateur.
