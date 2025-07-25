Déploiement
===========

==============
Pipeline CI/CD
==============

Un pipeline CI/CD est mise en place via le fichier .github/workflows/django.yml.
Ce fichier permet, à chaque push et pullrequest, de lancer les tests unitaires,
fonctionnels et d'intégrations afin de s'assurer que le site fonctionne correctement
et qu'au moins 80% du code est couvert.

Si une pullrequest ou un push vers la branche master est effectué,
le pipeline se connecte à Docker Hub pour créer deux images Docker du projet
qui seront stockées sur Docker Hub, dans le répertoire du projet.

La première image créée est une image utilisant le hash du commit.
Ainsi, chaque commit possède son image, ce qui permet de revenir facilement
en arrière lors d'un déploiement en cas de problèmes non détectés.

La seconde image Docker, à chaque fois identique à l'image du dessus,
est envoyée sur Docker Hub en utilisant le tag prédéfini latest et écrase
donc l'image précédente qui possédait ce tag, ce qui permet d'avoir une
url prédéfinie à utiliser pour toujours avoir une image avec l'image
la plus récente du projet.

Une fois l'image docker latest poussée sur Docker Hub,
le pipeline termine par un appel curl à l'url donnée par Render
-- service cloud sur lequel est déployé le projet --
pour lancer un déploiement avec l'image Docker la plus récente
portant le tag latest.

======
Render
======

Render est le service cloud sur lequel est déployé le projet Orange County Lettings.

=============================
Les variables d'environnement
=============================

Sur Github:
~~~~~~~~~~~
Les variables d'environnements doivent être à la fois ajoutées sur Github
et sur Render pour le déploiement. Pour ajouter une variable d'environnement
sur Github, allez dans les Settings du projet dans le répertoire du projet,
puis dans Secrets and variables, puis cliquez sur Actions et enfin sur le
bouton New repository secret.

Une fois cela fait, pensez à appeler la nouvelle variable d'environnement
dans le fichier pour la pipeline dans la rubrique env: en utlisant
le format VAR_NAME : ${{ secrets.VAR_NAME }} -- VAR_NAME étant à remplacer
par le nom que vous avez donné à votre variable d'environnement.

Sur Render
~~~~~~~~~~

Pour ajouter une variable d'environnement sur Render, une fois sur
la page du projet, dans le menu vertical à droite, allez dans Environment,
cliquez sur Edit puis sur Add.