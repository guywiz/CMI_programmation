# CMI_programmation

## Projets -- attendus

Cette fiche explicite les attendus du projet, et les critères d'évaluation, tant du code rendu que de sa présentaiton en soutenance.

### Attendus

* Le code du projet doit être posé sur un dépôt git (CREMI ou github). Assurez-vous de me donner accès au code (a minima en lecture).
* Vous pouvez rédiger une courte documentation: éditez un fichier README.md en [format `markdown`](https://www.markdownguide.org/basic-syntax/), il sera alors affiché dès l'accès à l'URL du projet. (Prenez modèle sur les fichiers de cours posées sur `github`)
* Vous développez une application à l'aide de la librairie `dash` permettant de visualiser un modèle prédictif construit à partir de données de votre choix.
* Votre application est construite selon le modèle MVC:
    * Le contrôleur dispose de `callback`pour exercer son contrôle, les évènements de l'application sont capturés à l'aide de ces mécanismes et permettent à l'utilisateur de sélectionner des paramètres sur les données et la visualisation qui l'intéresse.
    * Le modèle gère l'accès aux données qui sont stockées dans une base de données. Vous documenterez le schéma de données que vous avez construit. Vous fournirez les scripts permettant de reconstuire facilement la base de données à partir des fichiers sources obtenus de `data.gouv.fr`.
    * Votre application doit permettre d'explorer le modèle prédictif. Typiquement, on doit pouvoir modifier certains paramètres d'entrée du modèle, et visualiser comment se situe la prédiction dans l'ensemble des données d'entrainement du modèle.
    * Vous pouvez ajouter des visualisations annexes qui aident à comprendre le fonctionnement du modèle. Vous gérez les interactions sur les visualisations (sélection d'une zone ou de certains points, etc.) et l'adaptation du modèle en fonction de ces interactions.
* Votre code est bien construit, modulaire et lisible.
  * L'architecture MVC est implémentée à l'aide de classes.
  * Utilisez des fonctions pour isoler des calculs par nature (accès à la base de données, manipulation des dataframes, etc.)
* Vous documentez votre application (fichier README) permettant à un utilisateur intéressé de faire tourner facilement votre application. Les dépendances à des librairies tierces sont renseignées, vous aurez construit un fichier `requirements.txt` facilitant la création d'un environnement dans lequel l'application sera exécutée.

--

###  Grille d'évaluation – Document de projet (dépôt)

| Criteria  | Bien (4) | Acceptable (3) |  Amateur (2) | Insatisfaisant (1) | Score | Additional remarks |
|-----------|---|---|---|---|-------|--------------------|
| Implicit difficulty of dataset and methods used | Needed non obvious combination of ideas and tools | Required work, inventive solution | Required work but obvious solution |Straightforward, not much work | - | - |
| Code Readability | The code is exceptionally well organized and very easy to follow. | The code is fairly easy to read. | The code is readable only by someone who knows what it is supposed to be doing. | The code is poorly organized and very difficult to read. | - | - |
| Code Reusability | The code could be reused as a whole or each routine could be reused. | Most of the code could be reused in other programs. | Some parts of the code could be reused in other programs. | The code is not organized for reusability. | - | - | 
| Documentation | The project document is well written, helps understand the code, and puts things in perspective with respect to the project's objectives. | While the code is properly documented, the document lacks a domain-oriented discussion. | The documentation boils down to comments embedded in the code with some simple header comments separating routines. | The documentation, if any, does not help the reader understand the code. | - | - |

###  Grille d'évaluation – Soutenance

| Criteria  | Bien (4) | Acceptable (3) |  Amateur (2) | Insatisfaisant (1) | Score | Additional remarks |
|-----------|---|---|---|---|-------|--------------------|
| Mise en contexte |  Bonne description des enjeux liés aux données et au modèle |  Good presentation, well balanced, lively, got all the information in the right order, straight to the point | Globally OK, could improved (showing better images, emphasizing the right things, etc.) | Exposé en vrac, enjeux difficile à saisir | - | - |
| Aspects techniques |  Emphase sur les points intéressants, bonne description des challenges relevés  |  Good presentation, well balanced, lively, got all the information in the right order, straight to the point | Globally OK, could improved (showing better images, emphasizing the right things, etc.) | Présentation sans relief, difficulté à identifier les points saillants | - | - |


### Evaluation globale

| Criteria  | Bien (4) | Acceptable (3) |  Amateur (2) | Insatisfaisant (1) | Score | Additional remarks |
|-----------|---|---|---|---|-------|--------------------|
| (Global) Effort | Astute and creative, pleasant and relevant | Some thinking, a mixture of ready-made and custom approaches, pretty good end result | Good combinations of existing ideas and algorithms but could do better| Relatively easy, relied on ready-made solutions | - | - |

