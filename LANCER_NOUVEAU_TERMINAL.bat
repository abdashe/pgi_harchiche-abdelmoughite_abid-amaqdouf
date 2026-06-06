@echo off
REM ============================================
REM LANCEUR - Framework Pentest Mobile v2.0
REM Ouvre une NOUVELLE fenêtre de terminal
REM ============================================

REM Aller au répertoire courant
cd /d "%~dp0"

REM Ouvrir une nouvelle fenêtre PowerShell avec le titre personnalisé
title Framework Pentest Mobile v2.0
start powershell -NoExit -Command "cd '$PSScriptRoot'; & python code1.py; Write-Host ''; Write-Host '============================================'; Write-Host 'Analyse terminée ! Appuyez sur Entrée...'; Read-Host"
