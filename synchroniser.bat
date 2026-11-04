@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Synchroniser le portfolio
echo.
echo  Synchronisation du portfolio avec contenu.json...
echo.
set PY=
where py >nul 2>nul && set PY=py
if not defined PY where python >nul 2>nul && set PY=python
if not defined PY where python3 >nul 2>nul && set PY=python3
if not defined PY goto nopython
%PY% sync-contenu.py
goto fin
:nopython
echo  Python n'est pas installe sur cet ordinateur.
echo  Installe-le gratuitement sur https://www.python.org/downloads/
echo  (coche "Add python.exe to PATH" pendant l'installation), puis relance ce fichier.
:fin
echo.
pause
