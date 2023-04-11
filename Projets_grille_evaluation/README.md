# CMI_programmation

## Projets -- attendus

Cette fiche explicite les attendus du projet, et les critères d'évaluation, tant du code rendu que de sa présentaiton en soutenance.

### Attendus

* Le code du projet doit être posé sur un dépôt git (CREMI). Assurez-vous de me donner accès au code (a minima en lecture).
* Vous pouvez rédiger une courte documentation: éditez un fichier README.md en [format `markdown`](https://www.markdownguide.org/basic-syntax/), il sera alors affiché dès l'accès à l'URL du projet. (Prenez modèle sur les fichiers de cours posées sur `github`)
* Vous développez une application à l'aide de la librairie `dash` qui permet de visualiser les données sur les emplois obtenues du site `data.gouv.fr`
* Votre application est construite selon le modèle MVC:
    * Le contrôleur dispose de `callback`pour exercer son contrôle, les évènements de l'application sont capturés à l'aide de ces mécanismes et permettent à l'utilisateur de sélectionner des paramètres sur les données et la visualisation qui l'intéresse.
    * Le modèle gère l'accès aux données qui sont stockées dans une base de données. Vous documenterez le schéma de données que vous avez construit. Vous fournirez les scripts permettant de reconstuire facilement la base de données à partir des fichiers sources obtenus de `data.gouv.fr`.
    * Vous avez sélectionné des (>+ 2) visualisations qui sont pertinentes pour répondre à certaines questions sur les données. Vous gérez des interactions sur les visualisations (sélection d'une zone ou de certains points, etc.).
    * L'association entre questions et visualisations sera documentée.
* Votre code est bien construit, modulaire et lisible.
* Vous documentez votre application (fichier README) permettent à un utilisateur intéressé de faire tourner facilement votre application. Les dépendance à des librairies tierces sont renseignées, vous aurez construit un fichier `requirements.txt` facilitant la création d'un environnement dans lequel l'application sera exécutée.