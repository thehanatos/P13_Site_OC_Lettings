Déploiement
===========

Vue d’ensemble :
----------------
Le projet est déployé via Render avec intégration continue via GitHub Actions. Chaque push sur `main` déclenche un build Docker et déploiement automatique.

Configuration requise :
-----------------------
- Secrets Render : `SECRET_KEY`, `SENTRY_DSN`
- Base PostgreSQL configurée sur Render
- Fichiers statiques gérés par `collectstatic`

Étapes de déploiement :
-----------------------
1. Connecter le dépôt GitHub à Render
2. Activer le déploiement automatique
3. Définir les variables d’environnement
4. Configurer le Dockerfile pour lancer Gunicorn
5. Accéder à l’URL publique fournie par Render

Commandes Render importantes :
------------------------------
- `python manage.py migrate` à lancer en post-deploy command
- `python manage.py collectstatic` pour servir les assets
