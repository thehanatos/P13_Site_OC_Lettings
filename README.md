# 🏠 Orange County Lettings

Bienvenue sur le projet **Orange County Lettings** – une plateforme de location immobilière permettant d'explorer des profils utilisateurs et des annonces de locations.

---

## 🚀 Résumé

Ce projet est une application Django permettant :

* La consultation de locations (`lettings`)
* La gestion de profils utilisateurs (`profiles`)

---

## 🧑‍💻 Développement local

### 🔧 Prérequis

- Compte GitHub avec accès à ce repository
- Git CLI
- SQLite3 CLI
- Python 3.6 ou supérieur

> 💡 Il est supposé que la commande `python` exécute l'interpréteur Python 3.6+ (à moins qu’un environnement virtuel soit activé).

---

### 💻 macOS / Linux

#### 1. Cloner le repository

```bash
cd /path/to/put/project/in
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

#### 2. Créer et activer l’environnement virtuel

```bash
cd /path/to/Python-OC-Lettings-FR
python -m venv venv
# Si erreur sur Ubuntu :
# sudo apt-get install python3-venv
source venv/bin/activate
```

#### 3. Vérifications

```bash
which python          # Doit pointer vers ./venv/
python --version      # Doit afficher 3.6 ou supérieur
which pip             # Doit pointer vers pip dans le venv
```

#### 4. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 5. Lancer le serveur

```bash
python manage.py runserver
```

Aller sur  `http://localhost:8000`

---

### 🧪 Qualité du code et tests

#### Linting

```bash
flake8
```

> Les fichiers comme `migrations/`, `.git/`, `env/`, etc., sont exclus via le fichier `.flake8`.

#### Tests unitaires & couverture

```bash
coverage erase
coverage run -m pytest
coverage report -m
```

---

### 🗃️ Base de données SQLite

```bash
cd /path/to/Python-OC-Lettings-FR
Ouvrir une session shell `sqlite3`
Se connecter à la base de données `.open oc-lettings-site.sqlite3`
Afficher les tables dans la base de données `.tables`
Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
Lancer une requête sur la table des profils :
`select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
.quit pour quitter
```

---

### 🔐 Panel d’administration Django

Se rendre sur :
 `http://localhost:8000/admin`

Connectez-vous avec :

- **Utilisateur** : `admin`
- **Mot de passe** : `Abc1234!`

---

### 🪟 Windows (PowerShell)

Activer le venv :

```powershell
.\venv\Scripts\Activate.ps1
```

Remplacer `which <ma-commande>` par :

```powershell
(Get-Command <ma-commande>).Path
```

---

## 🐳 Docker (en local)

Docker permet d'exécuter l'application dans un conteneur isolé, assurant une cohérence parfaite entre les environnements de développement, de test et de production. Cela élimine les problèmes liés aux différences de configuration système ou de dépendances.

### ⚙️ Build et Run de l’image

```bash
docker build -t oc_lettings_site_local:latest .
```

```bash
docker run -p 8000:8000 oc_lettings_site_local:latest
```

> Assurez-vous que le module kernel `veth` est activé pour éviter les erreurs `failed to create endpoint`.

---

## 🚢 Déploiement

### 🔎 Vue d’ensemble

Le projet est déployé via **Render.com**, qui utilise une image Docker générée automatiquement par **GitHub Actions** à chaque mise à jour de la branche `main`.

---

### 🛠️ Configuration requise

| Élément                  | Détail                                                             |
| -------------------------- | ------------------------------------------------------------------- |
| Docker                     | Image avec `gunicorn` et fichiers statiques collectés            |
| GitHub Actions             | Pour CI, lint, tests, coverage et construction de l’image Docker   |
| Render.com                 | Hébergeur déployant le site à partir de l’image Docker          |
| Variables d’environnement | `SECRET_KEY`, `DEBUG`, `SENTRY_DSN` (configurées sur Render) |

---

### 📝 Étapes pour déployer

#### 🧪 1. Vérification en local

```bash
docker build -t oc_lettings_site_local:latest .
docker run -p 8000:8000 oc_lettings_site_local:latest
```

Visitez : http://localhost:8000

#### 🚀 2. Configuration sur Render

- Créer un nouveau **Web Service**
- Choisir **Docker** comme environnement
- Lier ce **dépôt GitHub**
- Ajouter les variables d’environnement nécessaires
- Activer les **auto-deploys sur la branche `main`**

#### 🤖 3. Configuration GitHub Actions

Un workflow CI/CD (`.github/workflows/main.yml`) s’assure que :

- le code est linté (`flake8`)
- les tests sont passés (`pytest`)
- l’image Docker est construite

---

## 📚 Documentation Complète

Pour une documentation détaillée incluant l’architecture, le guide d’installation, les technologies utilisées :
[Consultez la documentation sur Read the Docs ](https://p13-site-oc-lettings.readthedocs.io/fr/latest/index.html)

## 📎 Liens utiles

- Site en production (Render) : `https://p13-site-oc-lettings.onrender.com/`
- Repository GitHub : https://github.com/thehanatos/P13_Site_OC_Lettings

## 👤 Auteur

Projet réalisé dans le cadre du parcours **Développeur Python** — OpenClassrooms.

Fork du dépôt d’origine :
[OC Python Lettings FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR)
