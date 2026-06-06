#!/usr/bin/env python3
# ============================================
# UTILITAIRES - Framework Pentest Mobile
# ============================================

import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

class UtilitairesPentest:
    """Classe regroupant des utilitaires pour le pentest"""
    
    @staticmethod
    def calculer_hash_fichier(chemin: str, algo: str = "md5") -> str:
        """Calcule le hash d'un fichier"""
        algo_obj = hashlib.new(algo)
        
        with open(chemin, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                algo_obj.update(chunk)
        
        return algo_obj.hexdigest()
    
    @staticmethod
    def calculer_hashes_multiples(chemin: str) -> Dict[str, str]:
        """Calcule plusieurs hashes d'un fichier"""
        return {
            "md5": UtilitairesPentest.calculer_hash_fichier(chemin, "md5"),
            "sha1": UtilitairesPentest.calculer_hash_fichier(chemin, "sha1"),
            "sha256": UtilitairesPentest.calculer_hash_fichier(chemin, "sha256")
        }
    
    @staticmethod
    def lister_rapports() -> List[Path]:
        """Liste tous les rapports générés"""
        return list(Path(".").glob("rapport_pentest_*.txt"))
    
    @staticmethod
    def afficher_rapports():
        """Affiche les rapports disponibles"""
        rapports = UtilitairesPentest.lister_rapports()
        
        if not rapports:
            print("❌ Aucun rapport trouvé")
            return
        
        print("\n📊 Rapports disponibles:")
        for i, rapport in enumerate(rapports, 1):
            taille = rapport.stat().st_size / 1024
            date_modif = datetime.fromtimestamp(rapport.stat().st_mtime)
            print(f"  [{i}] {rapport.name}")
            print(f"      Taille: {taille:.2f} KB | Modifié: {date_modif}")
    
    @staticmethod
    def afficher_rapport(num: int = 0):
        """Affiche le contenu d'un rapport"""
        rapports = UtilitairesPentest.lister_rapports()
        
        if not rapports:
            print("❌ Aucun rapport trouvé")
            return
        
        # Dernier rapport par défaut
        rapport = rapports[num if num < len(rapports) else -1]
        
        print(f"\n📄 Contenu du rapport: {rapport.name}\n")
        print("=" * 60)
        
        with open(rapport, 'r', encoding='utf-8') as f:
            print(f.read())
    
    @staticmethod
    def nettoyer_fichiers_temp():
        """Nettoie les fichiers temporaires"""
        fichiers_temp = [
            "exemple_app.apk",
            "frida_hook_script.js",
            "*.pyc",
            "__pycache__"
        ]
        
        count = 0
        for pattern in fichiers_temp:
            for fichier in Path(".").glob(pattern):
                try:
                    if fichier.is_file():
                        os.remove(fichier)
                        print(f"✓ Supprimé: {fichier}")
                        count += 1
                    elif fichier.is_dir():
                        import shutil
                        shutil.rmtree(fichier)
                        print(f"✓ Supprimé: {fichier}/")
                        count += 1
                except Exception as e:
                    print(f"❌ Erreur: {e}")
        
        print(f"\n✓ {count} fichier(s) supprimé(s)")
    
    @staticmethod
    def generer_config_json():
        """Génère le fichier config.json"""
        from config import CONFIG
        CONFIG.creer_fichier_default()
    
    @staticmethod
    def afficher_infos_systeme():
        """Affiche les infos système"""
        print("\n📊 Informations Système:")
        print(f"  Python: {__import__('sys').version}")
        print(f"  OS: {__import__('platform').platform()}")
        print(f"  Répertoire courant: {os.getcwd()}")
        
        # Fichiers APK disponibles
        apk_files = list(Path(".").glob("*.apk"))
        print(f"  APK disponibles: {len(apk_files)}")
        
        # Rapports générés
        rapports = UtilitairesPentest.lister_rapports()
        print(f"  Rapports: {len(rapports)}")
    
    @staticmethod
    def analyser_apk_info(chemin_apk: str) -> Dict:
        """Affiche les infos d'un APK"""
        if not os.path.exists(chemin_apk):
            print(f"❌ Fichier non trouvé: {chemin_apk}")
            return {}
        
        infos = {
            "nom": os.path.basename(chemin_apk),
            "chemin": os.path.abspath(chemin_apk),
            "taille_bytes": os.path.getsize(chemin_apk),
            "taille_kb": os.path.getsize(chemin_apk) / 1024,
            "taille_mb": os.path.getsize(chemin_apk) / (1024 * 1024),
            "date_modif": datetime.fromtimestamp(os.path.getmtime(chemin_apk)),
            "hashes": UtilitairesPentest.calculer_hashes_multiples(chemin_apk)
        }
        
        print(f"\n📱 Infos APK: {infos['nom']}")
        print("=" * 60)
        print(f"  Chemin: {infos['chemin']}")
        print(f"  Taille: {infos['taille_kb']:.2f} KB ({infos['taille_mb']:.2f} MB)")
        print(f"  Modifié: {infos['date_modif']}")
        print(f"\n  Hashes:")
        print(f"    MD5:    {infos['hashes']['md5']}")
        print(f"    SHA1:   {infos['hashes']['sha1']}")
        print(f"    SHA256: {infos['hashes']['sha256']}")
        
        return infos
    
    @staticmethod
    def generer_script_frida_avance(package_name: str) -> str:
        """Génère un script Frida avancé"""
        script = f'''
// ============================================
// Script Frida Avancé pour {package_name}
// ============================================

Java.perform(function() {{
    
    console.log("[*] Attache à {package_name}...");
    
    // 1. HOOKING CRYPTOGRAPHIE
    console.log("[+] Hooks Cryptographie activés");
    var Cipher = Java.use("javax.crypto.Cipher");
    
    Cipher.getInstance.overload('java.lang.String').implementation = function(algorithm) {{
        console.log("[CRYPTO] getInstance(" + algorithm + ")");
        return this.getInstance(algorithm);
    }};
    
    // 2. HOOKING RÉSEAU
    console.log("[+] Hooks Réseau activés");
    var HttpURLConnection = Java.use("java.net.HttpURLConnection");
    
    HttpURLConnection.setRequestProperty.implementation = function(key, value) {{
        console.log("[NETWORK] Header: " + key + " = " + value);
        return this.setRequestProperty(key, value);
    }};
    
    // 3. HOOKING STOCKAGE
    console.log("[+] Hooks Stockage activés");
    var FileWriter = Java.use("java.io.FileWriter");
    
    FileWriter.write.overload('java.lang.String').implementation = function(str) {{
        console.log("[STORAGE] Write: " + str.substring(0, Math.min(50, str.length())));
        return this.write(str);
    }};
    
    // 4. HOOKING SharedPreferences
    console.log("[+] Hooks SharedPreferences activés");
    var SharedPreferences = Java.use("android.content.SharedPreferences$Editor");
    
    SharedPreferences.putString.implementation = function(key, value) {{
        console.log("[PREFS] putString(" + key + ", " + value + ")");
        return this.putString(key, value);
    }};
    
    console.log("[✓] Framework Frida chargé avec succès!");
}});
'''
        return script
    
    @staticmethod
    def exporter_resultats_json(rapport_path: str, output_json: str = "resultats_pentest.json"):
        """Exporte les résultats en JSON"""
        try:
            # Lecture du rapport texte
            with open(rapport_path, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Structuration des données
            resultats = {
                "timestamp": datetime.now().isoformat(),
                "rapport_source": rapport_path,
                "contenu": contenu,
                "statistiques": {
                    "taille_rapport_kb": len(contenu) / 1024
                }
            }
            
            # Sauvegarde JSON
            with open(output_json, 'w', encoding='utf-8') as f:
                json.dump(resultats, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Rapport exporté en JSON: {output_json}")
            
        except Exception as e:
            print(f"❌ Erreur: {e}")

def afficher_menu_utilitaires():
    """Affiche le menu des utilitaires"""
    print("\n" + "=" * 60)
    print("🛠️  MENU UTILITAIRES")
    print("=" * 60)
    print("[1] Lister les rapports")
    print("[2] Afficher dernier rapport")
    print("[3] Infos sur un APK")
    print("[4] Générer config.json")
    print("[5] Nettoyer fichiers temporaires")
    print("[6] Infos système")
    print("[7] Générer script Frida avancé")
    print("[8] Retour au menu principal\n")

def main_utilitaires():
    """Menu principal des utilitaires"""
    while True:
        afficher_menu_utilitaires()
        choix = input("👉 Votre choix: ").strip()
        
        if choix == "1":
            UtilitairesPentest.afficher_rapports()
        elif choix == "2":
            UtilitairesPentest.afficher_rapport()
        elif choix == "3":
            apk = input("📝 Chemin de l'APK: ").strip()
            UtilitairesPentest.analyser_apk_info(apk)
        elif choix == "4":
            UtilitairesPentest.generer_config_json()
        elif choix == "5":
            UtilitairesPentest.nettoyer_fichiers_temp()
        elif choix == "6":
            UtilitairesPentest.afficher_infos_systeme()
        elif choix == "7":
            package = input("📦 Nom du package: ").strip()
            script = UtilitairesPentest.generer_script_frida_avance(package)
            with open("frida_advanced.js", "w") as f:
                f.write(script)
            print("✓ Script Frida généré: frida_advanced.js")
        elif choix == "8":
            break
        else:
            print("❌ Choix invalide")

if __name__ == "__main__":
    main_utilitaires()
