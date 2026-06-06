#!/usr/bin/env python3
# ============================================
# GUIDE D'UTILISATION - Framework Pentest Mobile v2.0
# ============================================

"""
GUIDE COMPLET D'UTILISATION

Ce fichier explique comment utiliser le framework dans différents scénarios.
"""

def scenario_1_decouvrir():
    """Scénario 1: Découvrir le framework (2 minutes)"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ SCÉNARIO 1: DÉCOUVRIR LE FRAMEWORK (2 minutes)                ║
╚════════════════════════════════════════════════════════════════╝

ÉTAPE 1: Lancer la démo
    Command: python code1.py
    Résultat:
        ✓ Analyse statique avec APK simulé
        ✓ Reverse engineering
        ✓ Hooking dynamique (Frida)
        ✓ Intégration MobSF
        ✓ Scanner vulnérabilités
        ✓ Rapport généré automatiquement
    Durée: ~2 secondes
    Rapport: rapport_pentest_YYYYMMDD_HHMMSS.txt

ÉTAPE 2: Voir le rapport
    Command: cat rapport_pentest_*.txt
    ou
    Command: python utilitaires.py [2]

RÉSULTAT:
    ✓ Vous comprenez l'architecture
    ✓ Vous voyez tous les modules
    ✓ Vous avez un exemple de rapport
""")

def scenario_2_explorer():
    """Scénario 2: Explorer le menu (5 minutes)"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ SCÉNARIO 2: EXPLORER LE MENU (5 minutes)                      ║
╚════════════════════════════════════════════════════════════════╝

ÉTAPE 1: Lancer le menu principal
    Command: python run_pentest.py
    
ÉTAPE 2: Tester chaque option
    [1] Mode STATIQUE
        ✓ Analyse rapide
        ✓ Permissions, secrets, URLs
        ✓ Temps: ~1 seconde
    
    [2] Mode DYNAMIQUE
        ✓ Hooking avec Frida
        ✓ Interception données sensibles
        ✓ Temps: ~1 seconde
    
    [3] Mode HYBRIDE
        ✓ Tous les modes combinés
        ✓ Rapport complet
        ✓ Temps: ~2 secondes

ÉTAPE 3: Quitter (Ctrl+C)

RÉSULTAT:
    ✓ Vous connaissez les modes
    ✓ Vous savez sélectionner un APK
    ✓ Vous pouvez configurer le package name
""")

def scenario_3_analyser_apk_reel():
    """Scénario 3: Analyser un APK réel"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ SCÉNARIO 3: ANALYSER UN APK RÉEL (10-15 minutes)              ║
╚════════════════════════════════════════════════════════════════╝

ÉTAPE 1: Préparer l'APK
    1. Obtenir un APK (ou créer un test)
    2. Placer mon_app.apk dans le dossier du projet
    3. Note: Si androguard/MobSF réels installés, intégrer

ÉTAPE 2: Configurer (optionnel)
    Command: python utilitaires.py
    Choisir: [4] Générer config.json
    Éditer config.json selon besoins:
        - Type d'analyse par défaut
        - Timeouts
        - Hooks Frida
        - URL MobSF
        - Format rapport

ÉTAPE 3: Lancer l'analyse
    Command: python run_pentest.py
    
    Actions:
        ✓ Sélectionner mon_app.apk
        ✓ Entrer package name (ex: com.example.app)
        ✓ Choisir mode (Hybride recommandé)
        ✓ Attendre résultats

ÉTAPE 4: Examiner les résultats
    Fichiers générés:
        ✓ rapport_pentest_*.txt
        ✓ frida_hook_script.js
    
    Consulter:
        Command: python utilitaires.py [2]
        ou
        Command: less rapport_pentest_*.txt

RÉSULTAT:
    ✓ Audit complet de votre APK
    ✓ Rapport avec vulnérabilités identifiées
    ✓ Score de risque
    ✓ Recommandations de sécurité
""")

def scenario_4_personnaliser():
    """Scénario 4: Personnaliser le framework"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ SCÉNARIO 4: PERSONNALISER (Avancé)                            ║
╚════════════════════════════════════════════════════════════════╝

OPTION A: Ajouter des hooks Frida
    1. Éditer code1.py
    2. Classe HookingDynamique
    3. Ajouter méthode: creer_hook_XXX()
    4. Ajouter dans executer_hooks()

OPTION B: Étendre le scanner
    1. Éditer code1.py
    2. Classe ScannerVulnerabilites
    3. Ajouter méthode: _verifier_XXX()
    4. Ajouter dans scanner()

OPTION C: Intégrer androguard réel
    1. Installer androguard: pip install androguard
    2. Remplacer _extraire_permissions() statique
    3. Implémenter décompilation réelle
    4. Améliorer détection secrets

OPTION D: Intégrer MobSF API
    1. Installer MobSF localement
    2. Remplacer IntegrationMobSF
    3. Utiliser vraie API MobSF
    4. Récupérer vrais résultats

OPTION E: Ajouter new type de rapport
    1. Étendre RapportPFA
    2. Ajouter méthode export_pdf()
    3. Ou export_html()
    4. Ou export_json()

RÉSULTAT:
    ✓ Framework personnalisé
    ✓ Intégrations réelles possibles
    ✓ Extensible facilement
""")

def scenario_5_developper():
    """Scénario 5: Développer avec le framework"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ SCÉNARIO 5: DÉVELOPPER EN PYTHON (Script personnalisé)        ║
╚════════════════════════════════════════════════════════════════╝

EXEMPLE 1: Analyse simple
    
    from code1 import ApplicationPFA, TipoAnalyse
    
    app = ApplicationPFA("app.apk", "com.example.app")
    rapport = app.executer()
    print(f"Rapport: {rapport}")

EXEMPLE 2: Mode spécifique
    
    from code1 import ApplicationPFA, TipoAnalyse
    
    app = ApplicationPFA(
        "app.apk",
        "com.example.app",
        TipoAnalyse.STATIQUE  # Ou DYNAMIQUE ou HYBRIDE
    )
    rapport = app.executer()

EXEMPLE 3: Avec utilitaires
    
    from utilitaires import UtilitairesPentest
    
    # Hash fichier
    hash_md5 = UtilitairesPentest.calculer_hash_fichier("app.apk")
    hashes = UtilitairesPentest.calculer_hashes_multiples("app.apk")
    
    # Infos APK
    infos = UtilitairesPentest.analyser_apk_info("app.apk")
    
    # Rapports
    UtilitairesPentest.afficher_rapports()
    
    # Scripts Frida
    script = UtilitairesPentest.generer_script_frida_avance("com.example")
    
    # Nettoyage
    UtilitairesPentest.nettoyer_fichiers_temp()

EXEMPLE 4: Avec configuration
    
    from config import CONFIG
    
    # Afficher config
    CONFIG.afficher()
    
    # Obtenir valeur
    timeout = CONFIG.obtenir("analyse.timeout_frida")
    
    # Définir valeur
    CONFIG.definir("frida.enabled", True)
    
    # Sauvegarder
    CONFIG.sauvegarder()

RÉSULTAT:
    ✓ Scripts personnalisés possibles
    ✓ Intégration dans autres outils
    ✓ Automatisation avancée
""")

def troubleshooting():
    """Guide dépannage"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║ DÉPANNAGE - ERREURS COURANTES                                 ║
╚════════════════════════════════════════════════════════════════╝

ERREUR 1: ModuleNotFoundError: No module named 'code1'
    SOLUTION: Assurez-vous que code1.py est dans le même dossier
    ou ajoutez le chemin: sys.path.insert(0, '/chemin/vers/dossier')

ERREUR 2: FileNotFoundError: app.apk not found
    SOLUTION: Vérifiez que l'APK existe et que le chemin est correct

ERREUR 3: UnicodeDecodeError en lisant le rapport
    SOLUTION: Utiliser encoding='utf-8' quand lire fichiers

ERREUR 4: Permission denied (rapport)
    SOLUTION: Vérifier permissions fichier
    Command: chmod 644 rapport_*.txt

ERREUR 5: Script Frida ne génère pas
    SOLUTION: Vérifier que les classes sont bien créées
    ou exécuter: python code1.py

ERREUR 6: Config.json non trouvé
    SOLUTION: Générer via:
    python utilitaires.py [4]
    ou directement: CONFIG.creer_fichier_default()

CONSEIL:
    ✓ Utiliser encoding='utf-8' systématiquement
    ✓ Vérifier chemins fichiers
    ✓ Tester avec code1.py d'abord
    ✓ Consulter logs d'exécution
""")

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "=" * 70)
    print("📖 GUIDE D'UTILISATION - Framework Pentest Mobile v2.0")
    print("=" * 70)
    print("\n[1] 🎓 Scénario 1: Découvrir le framework (2 min)")
    print("[2] 🎮 Scénario 2: Explorer le menu (5 min)")
    print("[3] 🔍 Scénario 3: Analyser un APK réel (10 min)")
    print("[4] 🔧 Scénario 4: Personnaliser (Avancé)")
    print("[5] 💻 Scénario 5: Développer en Python")
    print("[6] ⚠️ Dépannage - Erreurs courantes")
    print("[7] 👋 Quitter\n")

def main():
    """Menu principal"""
    while True:
        afficher_menu()
        choix = input("👉 Votre choix: ").strip()
        
        if choix == "1":
            scenario_1_decouvrir()
        elif choix == "2":
            scenario_2_explorer()
        elif choix == "3":
            scenario_3_analyser_apk_reel()
        elif choix == "4":
            scenario_4_personnaliser()
        elif choix == "5":
            scenario_5_developper()
        elif choix == "6":
            troubleshooting()
        elif choix == "7":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("\n❌ Choix invalide")
        
        input("\n[Appuyez sur Entrée pour continuer...]")

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("BIENVENUE - GUIDE D'UTILISATION")
    print("=" * 70)
    main()
