# ============================================
# CONFIGURATION - Framework Pentest Mobile
# ============================================

import json
from typing import Dict, Any

class ConfigPentest:
    """Gestion de la configuration du framework"""
    
    # Configuration par défaut
    CONFIG_DEFAULT = {
        "framework": {
            "nom": "Framework Pentest Mobile - PFA",
            "version": "2.0",
            "auteur": "Étudiant PFA"
        },
        "analyse": {
            "type_defaut": "hybride",  # statique, dynamique, hybride
            "timeout_frida": 30,
            "timeout_mobsf": 60
        },
        "frida": {
            "enabled": True,
            "hooks": ["cryptographie", "reseau", "stockage"],
            "deep_inspection": True
        },
        "mobsf": {
            "enabled": True,
            "url": "http://localhost:8000",  # URL MobSF local
            "scan_type": "dynamic"
        },
        "rapport": {
            "format": "txt",
            "inclure_details": True,
            "inclure_recommandations": True,
            "inclure_scripts": True
        },
        "securite": {
            "obfuscation_check": True,
            "crypto_validation": True,
            "permission_analysis": True,
            "network_security": True
        }
    }
    
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self._charger_config()
    
    def _charger_config(self) -> Dict[str, Any]:
        """Charge la configuration depuis un fichier ou utilise les valeurs par défaut"""
        import os
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠ Erreur lors du chargement de la config: {e}")
                return self.CONFIG_DEFAULT
        else:
            return self.CONFIG_DEFAULT
    
    def sauvegarder(self):
        """Sauvegarde la configuration actuelle"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            print(f"✓ Configuration sauvegardée: {self.config_file}")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
    
    def obtenir(self, cle: str, defaut: Any = None) -> Any:
        """Obtient une valeur de la configuration"""
        keys = cle.split(".")
        value = self.config
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return defaut
        
        return value if value is not None else defaut
    
    def definir(self, cle: str, valeur: Any):
        """Définit une valeur dans la configuration"""
        keys = cle.split(".")
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = valeur
    
    def afficher(self):
        """Affiche la configuration actuelle"""
        print("\n" + "=" * 60)
        print("⚙️  CONFIGURATION ACTUELLE")
        print("=" * 60)
        print(json.dumps(self.config, indent=2, ensure_ascii=False))
    
    def creer_fichier_default(self):
        """Crée un fichier de configuration par défaut"""
        self.config = self.CONFIG_DEFAULT
        self.sauvegarder()
        print(f"✓ Fichier de configuration créé: {self.config_file}")

# Configuration globale
CONFIG = ConfigPentest()

if __name__ == "__main__":
    # Créer la configuration par défaut
    CONFIG.creer_fichier_default()
    CONFIG.afficher()
