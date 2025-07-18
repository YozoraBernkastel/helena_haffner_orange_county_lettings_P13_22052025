## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

### Vérifier la couverture de tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `coverage run -m pytest`
- `coverage html` ou `coverage report` pour avoir le détail de la couverture.

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Mettre en place la variable d'environnement SENTRY_KEY sur Pycharm

- Ouvrez votre projet dans Pycharm.
- Cliquez sur le bouton représentant trois points à la verticale en haut à droite à côté du bouton de Debug.
- Sélectionnez "__Edit...__"
- Sélectionnez la configuration permettant de lancer le serveur (correspondant à **python3 manage.py runserver**)
- À la ligne "__Environment Variables__", cliquez sur l'icone représentant un document contenant une liste.
- Cliquez sur le bouton __+__.
- Dans la colonne Name, écrivez "__SENTRY_KEY__"
- Dans la colonne Value, ajoutez la clé Sentry qui vous a été donnée.


## Déploiement

### Le Pipeline CI/CD

Un __pipeline CICD__ est mise en place via le fichier __.github/workflows/django.yml__.
Ce fichier permet, à chaque push et pullrequest, de lancer les tests unitaires, fonctionnels et d'intégrations afin
de s'assurer que le site fonctionne correctement et qu'au moins 80% du code est couvert.

**Si une pullrequest ou un push vers la branche master est effectué**, le pipeline se connecte à Docker Hub pour créer deux
images Docker du projet qui seront stockées sur Docker Hub, dans le répertoire du projet.

La première image créée est une image utilisant le hash du commit. Ainsi, chaque commit possède son image, ce qui permet
de revenir facilement en arrière lors d'un déploiement en cas de problèmes non détectés.

La seconde image Docker, à chaque fois identique à l'image du dessus, est envoyée sur Docker Hub en utilisant le
tag prédéfini __latest__ et écrase donc l'image précédente qui possédait ce tag, ce qui permet d'avoir une url
prédéfinie à utiliser pour toujours avoir une image avec l'image la plus récente du projet.

Une fois l'image docker __latest__ poussée sur Docker Hub, le pipeline termine par un appel curl à
l'url donnée par __Render__ -- service cloud sur lequel est déployé le projet -- pour lancer un déploiement
avec l'image Docker la plus récente portant le tag latest.

### Render

__Render__ est le service cloud sur lequel est déployé le projet Orange County Lettings.


### Les variables d'environnement

#### Sur Github
Les variables d'environnements doivent être à la fois ajoutées sur Github et sur Render pour le déploiement.
Pour ajouter une variable d'environnement sur Github, allez dans les Settings du projet dans le répertoire du projet,
puis dans __Secrets and variables__, puis cliquez sur __Actions__ et enfin sur le bouton New repository secret.

Une fois cela fait, pensez à appeler la nouvelle variable d'environnement dans le fichier pour la pipeline
dans la rubrique __env:__ en utlisant le format __VAR_NAME : ${{ secrets.VAR_NAME }}__ -- VAR_NAME étant à 
remplacer par le nom que vous avez donné à votre variable d'environnement.

#### Sur Render
Pour ajouter une variable d'environnement sur Render, une fois sur la page du projet, dans le menu vertical à droite, allez
dans __Environment__, cliquez sur __Edit__ puis sur Add.

