@echo off
REM ============================================
REM LANCER SIMPLE - Framework Pentest Mobile v2.0
REM Version simple - Lance l'option puis s'arrête
REM ============================================

cd /d "%~dp0"
title Framework Pentest Mobile v2.0

cls
echo.
echo ================================================
echo   FRAMEWORK PENTEST MOBILE v2.0
echo ================================================
echo.
echo   Choisissez une option:
echo.
echo   [1] DEMO complete
echo   [2] Menu interactif (sélectionner APK)
echo   [3] Guide découverte
echo   [4] Quitter
echo.

set /p CHOIX="Votre choix (1-4): "

cls
if "%CHOIX%"=="1" (
    python code1.py
    
) else if "%CHOIX%"=="2" (
    python run_pentest.py
    
) else if "%CHOIX%"=="3" (
    python QUICKSTART.py
    
) else if "%CHOIX%"=="4" (
    echo Au revoir!
    exit /b 0
    
) else (
    echo Choix invalide!
)

echo.
echo Fin de l'exécution
pause
