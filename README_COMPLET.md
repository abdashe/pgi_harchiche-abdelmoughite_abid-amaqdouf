# 🔐 Framework de Pentest Mobile - Projet PFA v2.0

## 📋 Description

Framework complet d'automatisation pour les tests d'intrusion mobiles (pentest Android). Combine l'analyse statique, le reverse engineering, le hooking dynamique (Frida) et l'intégration MobSF pour un audit de sécurité complet.

## 🎯 Objectifs Pédagogiques

- ✓ Pentest mobile et tests de sécurité
- ✓ Reverse engineering d'applications Android
- ✓ Hooking dynamique avec Frida
- ✓ Intégration avec MobSF
- ✓ Rapport d'audit automatisé

## 🏗️ Architecture

```
APK Input
   ↓
┌─────────────────────────┐
│  Analyse Statique       │ → Extraction infos, permissions, hash
├─────────────────────────┤
│  Reverse Engineering    │ → Secrets, URLs, failles crypto
├─────────────────────────┤
│  Hooking Dynamique      │ → Interception Frida (crypto, réseau, stockage)
├─────────────────────────┤
│  Intégration MobSF      │ → Manifest, certificat, qualité code
├─────────────────────────┤
│  Scanner Vulnérabilités │ → Détection failles, scoring
├─────────────────────────┤
│  Rapport Final          │ → HTML/TXT avec recommandations
└─────────────────────────┘
   ↓
Report + Scripts Frida
```

## 📦 Structure du Projet

```
projet gestion d intrusion/
├── code1.py                      # Framework principal
├── run_pentest.py               # Script lanceur interactif
├── config.py                    # Gestion configuration
├── readme.md                    # Documentation
├── rapport_pentest_*.txt        # Rapports générés
├── frida_hook_script.js         # Script Frida généré
└── config.json                  # Configuration (généré)
```

## 🚀 Installation & Utilisation

### Prérequis
- Python 3.7+
- Aucune dépendance externe requise pour la version démo

### Usage Simple

```bash
# Mode interactif
python run_pentest.py

# Exécution directe
python code1.py
```

### Modes d'Analyse Disponibles

1. **Mode STATIQUE** - Analyse rapide
   - Extraction des permissions
   - Détection de secrets
   - Analyse des URLs

2. **Mode DYNAMIQUE** - Hooking avec Frida
   - Interception cryptographie
   - Monitoring réseau
   - Suivi stockage données

3. **Mode HYBRIDE** (Recommandé)
   - Combine statique + dynamique + MobSF
   - Rapport complet et détaillé

## 📊 Fonctionnalités Principales

### 1. Analyseur APK (Statique)
```python
from code1 import ApplicationPFA, TipoAnalyse

app = ApplicationPFA("mon_app.apk")
rapport = app.executer()
```

### 2. Hooking Dynamique (Frida)
- Hook sur `javax.crypto.Cipher` → Détection algorithmes crypto
- Hook sur `java.net.HttpURLConnection` → Monitoring requêtes
- Hook sur `java.io.FileWriter` → Suivi écritures fichiers

### 3. Intégration MobSF
- Upload automatique
- Analyse manifest
- Validation certificat
- Qualité code

### 4. Scanner de Vulnérabilités
- ✓ Permissions dangereuses (CAMERA, LOCATION, etc.)
- ✓ Secrets en dur (API keys, mots de passe)
- ✓ Cryptographie faible (MD5, DES)
- ✓ Communications non sécurisées (HTTP)
- ✓ Stockage insécurisé

## 📄 Exemple de Résultats

```
🔐 FRAMEWORK PENTEST MOBILE - PROJET PFA v2.0
Mode: HYBRIDE

[1] ANALYSE STATIQUE DE L'APK
✓ Fichier: mon_app.apk
✓ Taille: 5.42 MB
✓ MD5: a3f8b2c9d1e4f5g6h7i8j9k0...
✓ Permissions trouvées: 12

[2] REVERSE ENGINEERING
✓ Secrets trouvés: 3
  ⚠ API_KEY: AIzaSyD... [ELEVE]
  ⚠ MOT_DE_PASSE: admin123... [CRITIQUE]

[3] HOOKING DYNAMIQUE (FRIDA)
✓ 3 hooks actifs
✓ Données cryptographiques: 2 interceptées
✓ Données réseau: 3 interceptées
✓ Données stockage: 2 interceptées

[4] ANALYSE MobSF
✓ Analyse du Manifest
✓ Analyse du certificat
✓ Analyse de la qualité du code

[5] SCAN DE VULNERABILITES
✓ Vulnérabilités trouvées: 8
  🔴 Secret en dur dans le code
  🟠 Cryptographie faible: MD5
  🟡 Permission dangereuse: CAMERA

📊 Score de risque: 85/100
📈 Niveau: ÉLEVÉ - Corrections nécessaires rapidement

✅ Rapport généré: rapport_pentest_20260606_203015.txt
```

## 🔍 Classes Principales

### ApplicationPFA
Classe orchestre principale
```python
app = ApplicationPFA(
    chemin_apk="app.apk",
    package_name="com.example.app",
    tipo_analise=TipoAnalyse.HYBRIDE
)
rapport = app.executer()
```

### HookingDynamique
Gestion des hooks Frida
```python
hooking = HookingDynamique("com.example.app")
resultats = hooking.executer_hooks()
script = hooking.generer_frida_script()
```

### IntegrationMobSF
Intégration avec MobSF
```python
mobsf = IntegrationMobSF("app.apk")
resultats = mobsf.analyser_avec_mobsf()
```

## 📋 Configuration

Éditer `config.json` pour personnaliser:

```json
{
  "analyse": {
    "type_defaut": "hybride",
    "timeout_frida": 30
  },
  "frida": {
    "hooks": ["cryptographie", "reseau", "stockage"]
  },
  "rapport": {
    "format": "txt",
    "inclure_scripts": true
  }
}
```

## 🛠️ Intégrations Futures

- [ ] Support androguard réel (au lieu de simulation)
- [ ] Déploiement APK sur device/émulateur
- [ ] Frida client réel (au lieu de simulation)
- [ ] MobSF API réelle
- [ ] Export rapports en PDF/HTML
- [ ] Dashboard web
- [ ] Base de données vulnérabilités

## 📚 Technologies Utilisées

| Technologie | Usage |
|---|---|
| **Python 3.7+** | Langage principal |
| **Frida** | Hooking dynamique |
| **MobSF** | Analyse statique avancée |
| **Androguard** | Décompilation APK |
| **Burp Suite** | Interception réseau |

## 📖 Ressources Utiles

- [Frida Documentation](https://frida.re/)
- [MobSF GitHub](https://github.com/MobSF/Mobile-Security-Framework-MobSF)
- [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)
- [Android Security Guide](https://developer.android.com/training/articles/security)

## 🤝 Contribution

Contributions bienvenues! Domaines d'amélioration:
- Support androguard réel
- Intégration Burp Suite
- Export rapports avancés
- Tests automatisés
- Documentation API

## 📝 Licence

Projet académique - PFA

## ✉️ Contact & Support

Pour des questions ou des améliorations, veuillez:
1. Vérifier la documentation
2. Consulter les fichiers d'exemple
3. Examiner les logs d'erreur

---

**Version:** 2.0  
**Date:** 2026-06-06  
**Statut:** ✅ Operational
