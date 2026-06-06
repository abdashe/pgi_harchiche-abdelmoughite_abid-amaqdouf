@echo off
REM ============================================
REM LANCER - Framework Pentest Mobile v2.0
REM Double-cliquez pour exécuter
REM ============================================

cd /d "%~dp0"
title Framework Pentest Mobile v2.0

:menu_principal
cls
echo.
echo ================================================
echo   CEL FRAMEWORK PENTEST MOBILE v2.0
echo ================================================
echo.
echo   Choisissez une option:
echo.
echo   [1] DEMO complète (Hybride)
echo   [2] Menu interactif
echo   [3] Decouverte rapide
echo   [4] Utilitaires
echo   [5] Resume du projet
echo   [6] Guide d'utilisation
echo   [7] Quitter
echo.

set /p CHOIX="Votre choix (1-7): "

cls
if "%CHOIX%"=="1" (
    echo Lancement de la DEMO...
    echo.
    python code1.py
    goto retour
    
) else if "%CHOIX%"=="2" (
    echo Menu interactif
    echo.
    python run_pentest.py
    goto retour
    
) else if "%CHOIX%"=="3" (
    echo Decouverte rapide
    echo.
    python QUICKSTART.py
    goto retour
    
) else if "%CHOIX%"=="4" (
    echo Utilitaires
    echo.
    python utilitaires.py
    goto retour
    
) else if "%CHOIX%"=="5" (
    echo Resume du projet
    echo.
    type INDEX_PROJET.md
    goto retour
    
) else if "%CHOIX%"=="6" (
    echo Guide d'utilisation
    echo.
    python GUIDE_UTILISATION.py
    goto retour
    
) else if "%CHOIX%"=="7" (
    echo Au revoir!
    goto bye
    
) else (
    echo Choix invalide!
    goto retour
)

:retour
echo.
echo ================================================
echo   Appuyez sur une touche pour RETOURNER AU MENU...
echo ================================================
pause > nul
goto menu_principal

:bye
exit /b 0
