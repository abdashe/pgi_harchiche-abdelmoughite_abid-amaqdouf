#!/usr/bin/env python3
# ============================================
# GUIDE DE DÉMARRAGE RAPIDE
# Framework Pentest Mobile v2.0
# ============================================

"""
QUICK START GUIDE - 5 MINUTES POUR COMMENCER

Choose one:
1. Démo automatique
2. Menu interactif
3. Script personnalisé
"""

def demo_automatique():
    """Lance la démo automatique"""
    print("\n🚀 Démo Automatique\n")
    print("Exécute dans le terminal:")
    print("  python code1.py\n")
    print("✓ Analyse complète avec APK simulé")
    print("✓ Affiche tous les modules")
    print("✓ Génère rapport d'audit")
    print("✓ Durée: ~2 secondes\n")

def menu_interactif():
    """Lance le menu interactif"""
    print("\n🎮 Menu Interactif\n")
    print("Exécute dans le terminal:")
    print("  python run_pentest.py\n")
    print("✓ Sélectionner type d'analyse")
    print("✓ Choisir l'APK à analyser")
    print("✓ Configurer le package name")
    print("✓ Lancer l'analyse\n")

def script_personnalise():
    """Exemple de script personnalisé"""
    print("\n🔧 Script Personnalisé\n")
    print("""
# Créer un fichier analyse_custom.py:

from code1 import ApplicationPFA, TipoAnalyse

# Paramètres
APK = "mon_app.apk"
PACKAGE = "com.example.app"
MODE = TipoAnalyse.HYBRIDE

# Lancer
app = ApplicationPFA(APK, PACKAGE, MODE)
rapport = app.executer()

# Résultat
print(f"Rapport: {rapport}")
""")
    print("\nExécute:")
    print("  python analyse_custom.py\n")

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "=" * 60)
    print("🔐 FRAMEWORK PENTEST MOBILE - QUICK START")
    print("=" * 60)
    print("\n[1] 📺 Voir démo automatique (2 sec)")
    print("[2] 🎮 Utiliser menu interactif")
    print("[3] 🔧 Voir exemple script personnalisé")
    print("[4] 📖 Lire documentation complète")
    print("[5] 🛠️ Ouvrir utilitaires")
    print("[6] ℹ️ Infos du projet")
    print("[7] 👋 Quitter\n")

def documentation():
    """Affiche les ressources doc"""
    print("\n📚 Documentation Disponible\n")
    print("[1] readme.md")
    print("    Cahier des charges original\n")
    print("[2] README_COMPLET.md")
    print("    Documentation détaillée du framework\n")
    print("[3] RESUMÉ_AMELIORATIONS.md")
    print("    Résumé des changements et améliorations\n")
    print("[4] INDEX_PROJET.md")
    print("    Structure et fichiers du projet\n")

def infos_projet():
    """Affiche les infos du projet"""
    print("\n" + "=" * 60)
    print("ℹ️  INFORMATIONS DU PROJET")
    print("=" * 60)
    
    info = {
        "Nom": "Framework Pentest Mobile",
        "Version": "2.0",
        "Type": "Projet PFA",
        "Langage": "Python 3.7+",
        "Status": "✅ Complet et testé",
        "Livrables": "Framework + Scripts + Rapports",
        "Fichiers": "4 modules Python + documentation",
        "Lignes de code": "~1170",
        "Modes": "Statique / Dynamique / Hybride"
    }
    
    for cle, valeur in info.items():
        print(f"  {cle:20} : {valeur}")
    
    print("\n📦 Fichiers Principaux:")
    print("  • code1.py (700+ lignes)")
    print("  • run_pentest.py (menu interactif)")
    print("  • config.py (gestion configuration)")
    print("  • utilitaires.py (outils helpers)")
    print("\n📚 Documentation:")
    print("  • readme.md")
    print("  • README_COMPLET.md")
    print("  • RESUMÉ_AMELIORATIONS.md")
    print("  • INDEX_PROJET.md")

def commandes_utiles():
    """Affiche les commandes utiles"""
    print("\n" + "=" * 60)
    print("💻 COMMANDES UTILES")
    print("=" * 60)
    
    commandes = {
        "Démo automatique": "python code1.py",
        "Menu principal": "python run_pentest.py",
        "Utilitaires": "python utilitaires.py",
        "Voir rapports": "python utilitaires.py [2]",
        "Infos APK": "python utilitaires.py [3]",
        "Config": "python utilitaires.py [4]",
        "Frida avancé": "python utilitaires.py [7]",
    }
    
    print("\n")
    for nom, cmd in commandes.items():
        print(f"  {nom:20} → {cmd}")
    print()

def mode_analyse_statique():
    """Explication mode statique"""
    print("\n" + "=" * 60)
    print("📊 MODE STATIQUE")
    print("=" * 60)
    print("""
✓ Analyse rapide et basique
✓ Extraction des infos:
  - Permissions
  - Secrets en dur
  - Failles cryptographiques
  - URLs
  - Hash MD5

⏱️ Durée: ~1 seconde
💾 Taille rapport: ~5KB
""")

def mode_analyse_dynamique():
    """Explication mode dynamique"""
    print("\n" + "=" * 60)
    print("🎯 MODE DYNAMIQUE")
    print("=" * 60)
    print("""
✓ Hooking avec Frida
✓ Interception:
  - Opérations cryptographiques
  - Requêtes réseau
  - Accès au stockage

⏱️ Durée: ~1 seconde (simulation)
📊 Données interceptées: Crypto, Réseau, Stockage
""")

def mode_analyse_hybride():
    """Explication mode hybride"""
    print("\n" + "=" * 60)
    print("🔐 MODE HYBRIDE (Recommandé)")
    print("=" * 60)
    print("""
✓ Combine tous les modes:
  - Analyse statique (complète)
  - Hooking dynamique (Frida)
  - Intégration MobSF

✓ Résultats complets:
  - Permissions & secrets
  - Vulnérabilités détaillées
  - Données interceptées
  - Score de risque
  - Recommandations

⏱️ Durée: ~2 secondes
💾 Taille rapport: ~15KB
""")

def premiere_utilisation():
    """Guide première utilisation"""
    print("\n" + "=" * 60)
    print("🎓 PREMIÈRE UTILISATION")
    print("=" * 60)
    print("""
ÉTAPE 1: Découvrir le framework
  Command: python code1.py
  Résultat: Démo avec APK simulé

ÉTAPE 2: Comprendre les options
  Command: python run_pentest.py
  Action: Explorer le menu
  Quitter: Appuyer sur Ctrl+C

ÉTAPE 3: Analyser un APK réel
  1. Placer mon_app.apk dans le dossier
  2. Exécuter: python run_pentest.py
  3. Sélectionner l'APK
  4. Choisir mode (Recommandé: Hybride)
  5. Attendre les résultats

ÉTAPE 4: Consulter le rapport
  Location: rapport_pentest_*.txt
  Voir aussi: python utilitaires.py [2]

ÉTAPE 5: Configurer (optionnel)
  Command: python utilitaires.py [4]
  Puis éditer: config.json
""")

def main():
    """Menu principal"""
    while True:
        afficher_menu()
        choix = input("👉 Votre choix: ").strip()
        
        if choix == "1":
            demo_automatique()
        elif choix == "2":
            menu_interactif()
        elif choix == "3":
            script_personnalise()
        elif choix == "4":
            documentation()
        elif choix == "5":
            commandes_utiles()
        elif choix == "6":
            infos_projet()
        elif choix == "7":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("\n❌ Choix invalide")
        
        input("\n[Appuyez sur Entrée pour continuer...]")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BIENVENUE DANS LE FRAMEWORK PENTEST MOBILE v2.0")
    print("=" * 60)
    main()
