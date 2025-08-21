Description et démarrage du projet
==================================================

Projet Web de l'entreprise fictive Orange County Lettings dédié à la location et aux
biens immobiliers.

Le code du site est découpé en trois modules:

- lettings qui gère la partie du site concernant les locations
- profiles qui gère la partie du site concernant les profiles utilisateurs.
- oc_lettings_site qui fait le pont entre lettings et profiles

Ce projet est crée à partir du framework Django.
Python, HTML et CSS sont les langages utilisés.

Installation du Projet
~~~~~~~~~~~~~~~~~~~~~~
 git clone git@github.com:YozoraBernkastel/helena_haffner_orange_county_lettings_P13_22052025.git

======================================
Environnement Virtuel utilisé : Poetry
======================================
Installation:

 curl -sSL https://install.python-poetry.org | python3 -

Activer l'environnement virtuel : Si la version de votre Poetry est inférieure à 2.1 :

 poetry shell

Si vous utilisez la version 2.1, il faudra soit d'abord installer la commande shell via la commande :

 poetry self add poetry-plugin-shell

Soit utiliser la commande :

 eval $(poetry env activate)

Installer les dépendances (les fichiers pyproject.toml ou poetry.lock doivent être présents dans le dossier et qui sont l'équivalent de requirements.txt) :

 poetry install

Sortir de l'environnement virtuel :

 exit

=========================================================
Mettre en place les variables d'environnement sur Pycharm
=========================================================
1. Ouvrez votre projet dans Pycharm.
2. Cliquez sur le bouton représentant trois points à la verticale en haut à droite à côté du bouton de Debug.
3. Sélectionnez "Edit..."
4. Sélectionnez la configuration permettant de lancer le serveur (correspondant à python3 manage.py runserver)
5. À la ligne "Environment Variables", cliquez sur l'icône représentant un document contenant une liste.
6. Cliquez sur le bouton +.
7. Dans la colonne Name, écrivez "SENTRY_KEY"
8. Dans la colonne Value, ajoutez la clé Sentry qui vous a été donnée.

Liste des Variables d'environnement et valeurs :

- ALLOWED_HOSTS : 127.0.0.1
- CSRF_TRUSTED : ://127.0.0.1/
- DJANGO_SETTINGS_MODULE : path_vers_le_settings-local
- PYTHONUNBUFFERED : 1
- SECRET_KEY : valeur_de_la_secret_key
- SENTRY_KEY : url_vers_le_repo_sentry_du_projet

