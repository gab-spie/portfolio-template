#!/bin/bash
# Double-clic sur Mac : lance la synchronisation du portfolio avec contenu.json.
cd "$(dirname "$0")" || exit 1
echo
echo " Synchronisation du portfolio avec contenu.json..."
echo
if command -v python3 >/dev/null 2>&1; then
  python3 sync-contenu.py
elif command -v python >/dev/null 2>&1; then
  python sync-contenu.py
else
  echo " Python n'est pas installe sur cet ordinateur."
  echo " Installe-le gratuitement sur https://www.python.org/downloads/ puis relance ce fichier."
fi
echo
read -n 1 -s -r -p " Appuie sur une touche pour fermer cette fenetre..."
echo
