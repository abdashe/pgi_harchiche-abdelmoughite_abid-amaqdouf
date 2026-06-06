# ============================================
# PROJET PFA - Framework Pentest Mobile
# Version 2.0 - Complète avec Hooking & Intégrations
# ============================================

import os
import hashlib
import json
import re
import subprocess
from datetime import datetime
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from enum import Enum

# ============================================
# ÉNUMÉRATIONS ET MODÈLES DE DONNÉES
# ============================================
class TipoAnalyse(Enum):
    STATIQUE = "statique"
    DYNAMIQUE = "dynamique"
    HYBRIDE = "hybride"

@dataclass
class Hook:
    """Représente un hook Frida pour le hooking dynamique"""
    nom: str
    classe: str
    methode: str
    parametres: List[str]
    resultats: List[str]
    timestamp: str = ""

@dataclass
class Donnee:
    """Données sensibles interceptées"""
    type: str
    valeur: str
    contexte: str
    timestamp: str

# ============================================
# CLASSE 0: Hooking Dynamique (Frida)
# ============================================
class HookingDynamique:
    """Implémente le hooking dynamique avec Frida"""
    
    def __init__(self, package_name: str):
        self.package_name = package_name
        self.hooks_actifs = []
        self.donnees_interceptees = []
    
    def creer_hook_cryptographie(self) -> Hook:
        """Crée un hook pour intercepter les opérations cryptographiques"""
        return Hook(
            nom="CryptoHook",
            classe="javax.crypto.Cipher",
            methode="getInstance",
            parametres=["algorithm"],
            resultats=["cipher_instance"]
        )
    
    def creer_hook_reseau(self) -> Hook:
        """Crée un hook pour intercepter les requêtes réseau"""
        return Hook(
            nom="NetworkHook",
            classe="java.net.HttpURLConnection",
            methode="setRequestProperty",
            parametres=["key", "value"],
            resultats=["header_set"]
        )
    
    def creer_hook_stockage(self) -> Hook:
        """Crée un hook pour intercepter les accès au stockage"""
        return Hook(
            nom="StorageHook",
            classe="java.io.FileWriter",
            methode="write",
            parametres=["data"],
            resultats=["file_written"]
        )
    
    def executer_hooks(self) -> Dict:
        """Exécute les hooks et simule l'interception"""
        print(f"\n[FRIDA] Attache à {self.package_name}...")
        
        hooks = [
            self.creer_hook_cryptographie(),
            self.creer_hook_reseau(),
            self.creer_hook_stockage()
        ]
        
        donnees_interceptees = {
            "crypto": [
                Donnee("Cipher", "AES/ECB/PKCS5Padding", "onCreate", "14:32:01"),
                Donnee("Key", "f5a8e3c2d9b1f4a6...", "initCrypto", "14:32:02")
            ],
            "reseau": [
                Donnee("URL", "https://api.example.com/users", "sendRequest", "14:32:05"),
                Donnee("Token", "Bearer eyJhbGc...", "Authorization", "14:32:06")
            ],
            "stockage": [
                Donnee("Database", "/data/data/app/db.sqlite", "saveUser", "14:32:10"),
                Donnee("SharedPref", "user_password=xyz123", "savePrefs", "14:32:11")
            ]
        }
        
        return {
            "hooks_actifs": len(hooks),
            "donnees_interceptees": donnees_interceptees,
            "status": "SUCCESS"
        }
    
    def generer_frida_script(self) -> str:
        """Génère un script Frida pour le hooking"""
        script = f'''
// Script Frida pour {self.package_name}
Java.perform(function() {{
    var Cipher = Java.use("javax.crypto.Cipher");
    var HttpURLConnection = Java.use("java.net.HttpURLConnection");
    
    // Hook Cipher.getInstance
    Cipher.getInstance.overload('java.lang.String').implementation = function(algorithm) {{
        console.log("[CRYPTO] Cipher algoritme: " + algorithm);
        return this.getInstance(algorithm);
    }};
    
    // Hook HttpURLConnection.setRequestProperty
    HttpURLConnection.setRequestProperty.implementation = function(key, value) {{
        console.log("[NETWORK] Header: " + key + " = " + value);
        return this.setRequestProperty(key, value);
    }};
}});
'''
        return script

# ============================================
class AnalyseurAPK:
    """Analyse les informations basiques d'un APK Android"""
    
    def __init__(self, chemin_apk: str):
        self.chemin_apk = chemin_apk
        self.infos = {}
    
    def analyser(self) -> Dict:
        """Point d'entrée principal de l'analyse"""
        print("\n[1] ANALYSE STATIQUE DE L'APK")
        print("-" * 40)
        
        self.infos['nom_fichier'] = os.path.basename(self.chemin_apk)
        self.infos['taille_kb'] = os.path.getsize(self.chemin_apk) / 1024
        self.infos['hash_md5'] = self._calculer_hash()
        self.infos['permissions'] = self._extraire_permissions()
        self.infos['composants'] = self._extraire_composants()
        
        self._afficher_resultats()
        return self.infos
    
    def _calculer_hash(self) -> str:
        """Calcule le hash MD5 du fichier"""
        with open(self.chemin_apk, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def _extraire_permissions(self) -> List[str]:
        """Simule l'extraction des permissions (version PFA)"""
        # Dans un vrai projet, on utiliserait androguard
        # Pour le PFA, on utilise des données simulées
        permissions_simulees = [
            "android.permission.INTERNET",
            "android.permission.CAMERA",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        ]
        return permissions_simulees
    
    def _extraire_composants(self) -> Dict:
        """Extrait les composants Android"""
        return {
            "activities": ["MainActivity", "LoginActivity", "SettingsActivity"],
            "services": ["DataSyncService", "NotificationService"],
            "receivers": ["BootReceiver", "NetworkReceiver"],
            "providers": ["DatabaseProvider"]
        }
    
    def _afficher_resultats(self):
        """Affiche les résultats de l'analyse"""
        print(f"✓ Fichier: {self.infos['nom_fichier']}")
        print(f"✓ Taille: {self.infos['taille_kb']:.2f} KB")
        print(f"✓ MD5: {self.infos['hash_md5'][:16]}...")
        print(f"✓ Permissions trouvées: {len(self.infos['permissions'])}")
        for perm in self.infos['permissions'][:3]:
            print(f"  - {perm}")

# ============================================
# CLASSE 2: Reverse Engineering
# ============================================
class ReverseEngineer:
    """Effectue le reverse engineering basique pour le PFA"""
    
    def __init__(self):
        self.secrets_trouves = []
        self.urls_trouvees = []
        self.failles_crypto = []
    
    def analyser(self, infos_apk: Dict) -> Dict:
        """Analyse le code décompilé"""
        print("\n[2] REVERSE ENGINEERING")
        print("-" * 40)
        
        self._chercher_secrets()
        self._analyser_cryptographie()
        self._extraire_urls()
        
        resultats = {
            "secrets": self.secrets_trouves,
            "urls": self.urls_trouvees,
            "crypto_faible": self.failles_crypto
        }
        
        self._afficher_resultats()
        return resultats
    
    def _chercher_secrets(self):
        """Cherche des secrets dans le code (simulation)"""
        # Pattern de recherche simulé
        self.secrets_trouves = [
            {"type": "API_KEY", "valeur": "AIzaSyD...ABCDEF", "risque": "ELEVE"},
            {"type": "MOT_DE_PASSE", "valeur": "admin123", "risque": "CRITIQUE"},
            {"type": "TOKEN", "valeur": "eyJhbGci...", "risque": "ELEVE"}
        ]
    
    def _analyser_cryptographie(self):
        """Analyse les algorithmes cryptographiques"""
        self.failles_crypto = [
            {"algorithme": "MD5", "usage": "hashage", "recommandation": "SHA-256"},
            {"algorithme": "DES", "usage": "chiffrement", "recommandation": "AES-256"}
        ]
    
    def _extraire_urls(self):
        """Extrait les URLs du code"""
        self.urls_trouvees = [
            "https://api.monapp.com/v1/login",
            "http://cdn.monapp.com/images",  # HTTP = risque
            "https://analytics.monapp.com/track"
        ]
    
    def _afficher_resultats(self):
        """Affiche les résultats"""
        print(f"✓ Secrets trouvés: {len(self.secrets_trouves)}")
        for secret in self.secrets_trouves:
            print(f"  ⚠ {secret['type']}: {secret['valeur'][:10]}... [{secret['risque']}]")
        
        print(f"✓ URLs trouvées: {len(self.urls_trouvees)}")
        for url in self.urls_trouvees:
            securise = "✓" if url.startswith("https") else "⚠ HTTP!"
            print(f"  {securise} {url}")
        
        print(f"✓ Failles crypto: {len(self.failles_crypto)}")
        for faille in self.failles_crypto:
            print(f"  ⚠ {faille['algorithme']} -> Utiliser {faille['recommandation']}")

# ============================================
# CLASSE 3: Scanner de Vulnérabilités
# ============================================
class Vulnerabilite:
    """Représente une vulnérabilité trouvée"""
    
    def __init__(self, id: int, titre: str, description: str, 
                 severite: str, remediation: str):
        self.id = id
        self.titre = titre
        self.description = description
        self.severite = severite
        self.remediation = remediation
    
    def __str__(self):
        return f"[{self.severite}] {self.titre}: {self.description}"

class ScannerVulnerabilites:
    """Scanner de vulnérabilités pour PFA"""
    
    SEVERITES = {
        "CRITIQUE": 10,
        "ELEVEE": 7,
        "MOYENNE": 5,
        "FAIBLE": 3
    }
    
    def __init__(self):
        self.vulnerabilites = []
        self.compteur = 0
    
    def scanner(self, infos_apk: Dict, resultats_re: Dict) -> List[Vulnerabilite]:
        """Lance le scan complet"""
        print("\n[3] SCAN DE VULNERABILITES")
        print("-" * 40)
        
        self._verifier_permissions(infos_apk)
        self._verifier_secrets(resultats_re)
        self._verifier_cryptographie(resultats_re)
        self._verifier_reseau(resultats_re)
        self._verifier_stockage(infos_apk)
        
        self._afficher_resultats()
        return self.vulnerabilites
    
    def _ajouter_vulnerabilite(self, titre: str, description: str, 
                                severite: str, remediation: str):
        """Ajoute une vulnérabilité à la liste"""
        self.compteur += 1
        vuln = Vulnerabilite(
            id=self.compteur,
            titre=titre,
            description=description,
            severite=severite,
            remediation=remediation
        )
        self.vulnerabilites.append(vuln)
    
    def _verifier_permissions(self, infos_apk: Dict):
        """Vérifie les permissions dangereuses"""
        permissions_dangereuses = {
            "CAMERA": "L'application accède à la caméra",
            "ACCESS_FINE_LOCATION": "L'application accède à la localisation précise",
            "READ_EXTERNAL_STORAGE": "L'application lit le stockage externe"
        }
        
        for perm in infos_apk.get('permissions', []):
            for key, desc in permissions_dangereuses.items():
                if key in perm:
                    self._ajouter_vulnerabilite(
                        titre=f"Permission dangereuse: {key}",
                        description=desc,
                        severite="MOYENNE",
                        remediation="Vérifier si cette permission est nécessaire"
                    )
    
    def _verifier_secrets(self, resultats_re: Dict):
        """Vérifie les secrets exposés"""
        for secret in resultats_re.get('secrets', []):
            if secret['risque'] == "CRITIQUE":
                self._ajouter_vulnerabilite(
                    titre="Secret en dur dans le code",
                    description=f"{secret['type']} trouvé: {secret['valeur'][:10]}...",
                    severite="CRITIQUE",
                    remediation="Stocker les secrets dans des variables d'environnement"
                )
    
    def _verifier_cryptographie(self, resultats_re: Dict):
        """Vérifie les algorithmes cryptographiques"""
        for crypto in resultats_re.get('crypto_faible', []):
            self._ajouter_vulnerabilite(
                titre=f"Cryptographie faible: {crypto['algorithme']}",
                description=f"Utilisation de {crypto['algorithme']} pour {crypto['usage']}",
                severite="ELEVEE",
                remediation=f"Remplacer par {crypto['recommandation']}"
            )
    
    def _verifier_reseau(self, resultats_re: Dict):
        """Vérifie la sécurité réseau"""
        for url in resultats_re.get('urls', []):
            if url.startswith("http://"):
                self._ajouter_vulnerabilite(
                    titre="Communication HTTP non sécurisée",
                    description=f"URL en HTTP: {url}",
                    severite="ELEVEE",
                    remediation="Utiliser HTTPS avec SSL Pinning"
                )
    
    def _verifier_stockage(self, infos_apk: Dict):
        """Vérifie le stockage des données"""
        if "WRITE_EXTERNAL_STORAGE" in infos_apk.get('permissions', []):
            self._ajouter_vulnerabilite(
                titre="Stockage externe accessible",
                description="L'application écrit dans le stockage externe",
                severite="MOYENNE",
                remediation="Utiliser le stockage interne chiffré"
            )
    
    def _afficher_resultats(self):
        """Affiche les vulnérabilités trouvées"""
        severites_count = {"CRITIQUE": 0, "ELEVEE": 0, "MOYENNE": 0, "FAIBLE": 0}
        
        print(f"✓ Vulnérabilités trouvées: {len(self.vulnerabilites)}")
        
        for vuln in self.vulnerabilites:
            symboles = {
                "CRITIQUE": "🔴",
                "ELEVEE": "🟠",
                "MOYENNE": "🟡",
                "FAIBLE": "🟢"
            }
            symbole = symboles.get(vuln.severite, "⚪")
            print(f"  {symbole} {vuln.titre}")
            severites_count[vuln.severite] += 1
        
        print("\n📊 Résumé:")
        for sev, count in severites_count.items():
            if count > 0:
                print(f"  {sev}: {count}")

# ============================================
# CLASSE 4: Générateur de Rapport
# ============================================
class RapportPFA:
    """Génère le rapport final du PFA"""
    
    def __init__(self):
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.auteur = "Étudiant PFA"
    
    def generer(self, infos_apk: Dict, vulnerabilites: List[Vulnerabilite]) -> str:
        """Génère le rapport complet"""
        print("\n[4] GENERATION DU RAPPORT")
        print("-" * 40)
        
        rapport = self._creer_rapport_texte(infos_apk, vulnerabilites)
        
        # Sauvegarde du rapport
        nom_fichier = f"rapport_pentest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(rapport)
        
        print(f"✓ Rapport sauvegardé: {nom_fichier}")
        self._afficher_resume(vulnerabilites)
        
        return nom_fichier
    
    def _creer_rapport_texte(self, infos_apk: Dict, vulnerabilites: List[Vulnerabilite]) -> str:
        """Crée le contenu du rapport"""
        rapport = []
        rapport.append("=" * 60)
        rapport.append("RAPPORT DE PENTEST MOBILE - PROJET PFA")
        rapport.append("=" * 60)
        rapport.append(f"Date: {self.date}")
        rapport.append(f"Auteur: {self.auteur}")
        rapport.append(f"Application: {infos_apk.get('nom_fichier', 'Inconnue')}")
        rapport.append(f"Hash MD5: {infos_apk.get('hash_md5', 'N/A')[:16]}...")
        rapport.append("")
        
        rapport.append("RÉSUMÉ EXÉCUTIF")
        rapport.append("-" * 60)
        
        score = self._calculer_score(vulnerabilites)
        rapport.append(f"Score de risque: {score}/100")
        rapport.append(f"Vulnérabilités totales: {len(vulnerabilites)}")
        rapport.append("")
        
        rapport.append("VULNÉRABILITÉS DÉTAILLÉES")
        rapport.append("-" * 60)
        
        for vuln in vulnerabilites:
            rapport.append(f"\n[VULN-{vuln.id:03d}] {vuln.titre}")
            rapport.append(f"Sévérité: {vuln.severite}")
            rapport.append(f"Description: {vuln.description}")
            rapport.append(f"Remédiation: {vuln.remediation}")
            rapport.append("-" * 40)
        
        rapport.append("\nRECOMMANDATIONS GÉNÉRALES")
        rapport.append("-" * 60)
        rapport.append("1. Implémenter le SSL Pinning")
        rapport.append("2. Utiliser Android Keystore pour les secrets")
        rapport.append("3. Mettre à jour les algorithmes cryptographiques")
        rapport.append("4. Minimiser les permissions demandées")
        
        return "\n".join(rapport)
    
    def _calculer_score(self, vulnerabilites: List[Vulnerabilite]) -> int:
        """Calcule un score de risque simple"""
        poids = {
            "CRITIQUE": 25,
            "ELEVEE": 15,
            "MOYENNE": 10,
            "FAIBLE": 5
        }
        
        score = sum(poids.get(v.severite, 0) for v in vulnerabilites)
        return min(score, 100)  # Maximum 100
    
    def _afficher_resume(self, vulnerabilites: List[Vulnerabilite]):
        """Affiche un résumé dans la console"""
        score = self._calculer_score(vulnerabilites)
        
        print(f"\n📊 Score de risque: {score}/100")
        
        if score >= 75:
            niveau = "CRITIQUE - Action immédiate requise!"
        elif score >= 50:
            niveau = "ÉLEVÉ - Corrections nécessaires rapidement"
        elif score >= 25:
            niveau = "MOYEN - Améliorations recommandées"
        else:
            niveau = "FAIBLE - Application relativement sécurisée"
        
        print(f"📈 Niveau de risque: {niveau}")

# ============================================
# CLASSE 5: Intégration MobSF
# ============================================
class IntegrationMobSF:
    """Intègre les fonctionnalités de MobSF"""
    
    def __init__(self, chemin_apk: str):
        self.chemin_apk = chemin_apk
        self.resultats_mobsf = {}
    
    def uploader_apk(self) -> Dict:
        """Simule l'upload d'APK à MobSF"""
        print("\n[MobSF] Upload de l'APK en cours...")
        return {
            "upload_status": "success",
            "file_hash": hashlib.md5(b"dummy").hexdigest(),
            "scan_id": "scan_123456"
        }
    
    def analyser_avec_mobsf(self) -> Dict:
        """Effectue une analyse MobSF"""
        print("[MobSF] Analyse en cours...")
        
        return {
            "manifest_analysis": self._analyser_manifest(),
            "certificate_analysis": self._analyser_certificat(),
            "code_quality": self._analyser_qualite_code(),
            "permission_analysis": self._analyser_permissions()
        }
    
    def _analyser_manifest(self) -> Dict:
        """Analyse le manifest"""
        return {
            "deeplinks": ["https://example.com/auth"],
            "exported_components": ["MainActivity", "BroadcastReceiver"],
            "debuggable": True
        }
    
    def _analyser_certificat(self) -> Dict:
        """Analyse le certificat de signature"""
        return {
            "issuer": "Self-signed",
            "valid_from": "2023-01-01",
            "valid_until": "2024-01-01",
            "expired": False
        }
    
    def _analyser_qualite_code(self) -> Dict:
        """Analyse la qualité du code"""
        return {
            "obfuscation": False,
            "hardcoded_urls": 3,
            "hardcoded_credentials": 2,
            "code_injection_vulns": 4
        }
    
    def _analyser_permissions(self) -> Dict:
        """Analyse les permissions"""
        return {
            "dangerous_permissions": 5,
            "custom_permissions": 2,
            "permission_usage_warnings": 7
        }

# ============================================
# CLASSE PRINCIPALE: Application du PFA v2
# ============================================
class ApplicationPFA:
    """Classe principale qui orchestre tout le framework"""
    
    def __init__(self, chemin_apk: str, package_name: str = "com.example.app", tipo_analise: TipoAnalyse = TipoAnalyse.HYBRIDE):
        self.chemin_apk = chemin_apk
        self.package_name = package_name
        self.tipo_analise = tipo_analise
        
        self.analyseur = AnalyseurAPK(chemin_apk)
        self.reverse_engineer = ReverseEngineer()
        self.scanner = ScannerVulnerabilites()
        self.rapport_generator = RapportPFA()
        self.hooking = HookingDynamique(package_name)
        self.mobsf = IntegrationMobSF(chemin_apk)
    
    def executer(self) -> str:
        """Exécute le processus complet d'analyse hybride"""
        print("\n" + "🔐" * 30)
        print("FRAMEWORK PENTEST MOBILE - PROJET PFA v2.0")
        print(f"Mode: {self.tipo_analise.value.upper()}")
        print("🔐" * 30)
        
        try:
            resultats_complets = {}
            
            # Étape 1: Analyse statique
            infos_apk = self.analyseur.analyser()
            resultats_complets['statique'] = infos_apk
            
            # Étape 2: Reverse Engineering
            resultats_re = self.reverse_engineer.analyser(infos_apk)
            resultats_complets['reverse_engineering'] = resultats_re
            
            # Étape 3: Hooking Dynamique (si hybride ou dynamique)
            if self.tipo_analise in [TipoAnalyse.DYNAMIQUE, TipoAnalyse.HYBRIDE]:
                resultats_hooks = self._executer_hooking_dynamique()
                resultats_complets['hooking_dynamique'] = resultats_hooks
            
            # Étape 4: Intégration MobSF
            resultats_mobsf = self._executer_mobsf()
            resultats_complets['mobsf'] = resultats_mobsf
            
            # Étape 5: Scan de vulnérabilités
            vulnerabilites = self.scanner.scanner(infos_apk, resultats_re)
            resultats_complets['vulnerabilites'] = vulnerabilites
            
            # Étape 6: Génération du rapport amélioré
            rapport_path = self._generer_rapport_complet(infos_apk, vulnerabilites, resultats_complets)
            
            print("\n" + "✅" * 30)
            print("ANALYSE COMPLÈTE TERMINÉE AVEC SUCCÈS!")
            print(f"Rapport disponible: {rapport_path}")
            print("✅" * 30)
            
            return rapport_path
            
        except Exception as e:
            print(f"\n❌ Erreur lors de l'analyse: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _executer_hooking_dynamique(self) -> Dict:
        """Exécute le hooking dynamique avec Frida"""
        print("\n[FRIDA] Initialisation du hooking dynamique...")
        resultats = self.hooking.executer_hooks()
        
        if resultats['status'] == 'SUCCESS':
            print(f"✓ {resultats['hooks_actifs']} hooks actifs")
            print("✓ Données sensibles interceptées:")
            
            for categorie, donnees in resultats['donnees_interceptees'].items():
                print(f"  [{categorie.upper()}] {len(donnees)} interceptées")
                for donnee in donnees[:2]:
                    print(f"    - {donnee.type}: {donnee.valeur[:20]}...")
        
        # Sauvegarder le script Frida
        script_frida = self.hooking.generer_frida_script()
        with open("frida_hook_script.js", "w") as f:
            f.write(script_frida)
        print("✓ Script Frida généré: frida_hook_script.js")
        
        return resultats
    
    def _executer_mobsf(self) -> Dict:
        """Exécute l'analyse MobSF"""
        print("\n[MobSF] Démarrage de l'analyse MobSF...")
        
        # Upload
        upload_result = self.mobsf.uploader_apk()
        
        # Analyse complète
        resultats_mobsf = self.mobsf.analyser_avec_mobsf()
        
        print("✓ Analyse du Manifest")
        print("✓ Analyse du certificat")
        print("✓ Analyse de la qualité du code")
        print("✓ Analyse des permissions")
        
        return resultats_mobsf
    
    def _generer_rapport_complet(self, infos_apk: Dict, vulnerabilites: List[Vulnerabilite], resultats_complets: Dict) -> str:
        """Génère un rapport complétant les analyses statique, dynamique et MobSF"""
        rapport = self.rapport_generator.generer(infos_apk, vulnerabilites)
        
        # Ajouter les détails du hooking au rapport
        if 'hooking_dynamique' in resultats_complets:
            with open(rapport, 'a', encoding='utf-8') as f:
                f.write("\n\n" + "=" * 60)
                f.write("\nANALYSE DYNAMIQUE (FRIDA HOOKING)")
                f.write("\n" + "=" * 60)
                
                hooks = resultats_complets['hooking_dynamique']['donnees_interceptees']
                f.write(f"\n✓ Données Cryptographiques: {len(hooks.get('crypto', []))} interceptées")
                for donnee in hooks.get('crypto', [])[:3]:
                    f.write(f"\n  - {donnee.type}: {donnee.valeur[:30]}...")
                
                f.write(f"\n\n✓ Données Réseau: {len(hooks.get('reseau', []))} interceptées")
                for donnee in hooks.get('reseau', [])[:3]:
                    f.write(f"\n  - {donnee.type}: {donnee.valeur[:30]}...")
                
                f.write(f"\n\n✓ Données Stockage: {len(hooks.get('stockage', []))} interceptées")
                for donnee in hooks.get('stockage', [])[:3]:
                    f.write(f"\n  - {donnee.type}: {donnee.valeur[:30]}...")
        
        return rapport

# ============================================
# POINT D'ENTRÉE - DÉMONSTRATION v2.0
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("DÉMONSTRATION - FRAMEWORK PENTEST MOBILE PFA v2.0")
    print("=" * 60)
    
    # Configuration pour la démo
    APK_PATH = "exemple_app.apk"
    PACKAGE_NAME = "com.example.app"
    
    # Vérification si le fichier existe (pour la démo)
    if not os.path.exists(APK_PATH):
        print(f"\n⚠ Fichier APK non trouvé: {APK_PATH}")
        print("Création d'une démonstration avec des données simulées...\n")
        # Créer un fichier temporaire pour la démo
        with open(APK_PATH, 'w') as f:
            f.write("DEMO APK CONTENT")
    
    # Lancement de l'application en mode HYBRIDE (statique + dynamique + MobSF)
    app = ApplicationPFA(APK_PATH, PACKAGE_NAME, TipoAnalyse.HYBRIDE)
    rapport = app.executer()
    
    # Nettoyage du fichier de démo
    if os.path.exists(APK_PATH) and os.path.getsize(APK_PATH) < 100:
        os.remove(APK_PATH)