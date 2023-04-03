# CMI_programmation

## Séance 7 `dash` (encore) et vos projets

Cette séance

* est revenue sur la librairie `dash` de `python`
* s'est penché sur les quesitons potentielles sur les données d'emplois 2017-2022, et les visualisations à construire pour aider à y répondre

### Coordonnées géographiques

* Vous disposez d'une [base de code pour construire votre projet, qui suit le modle MVC (Modèle - Vue - Contrôleur)](../Seance_6_BD_dash/dash_exemple/);
* On trouve facilement de nombreux tutoriaux introductifs avec des exemples.

Prenez le temps d'explorer [la galerie d'exemples de visualisations proposés par `plotly`](https://plotly.com/python/)(qu'utilise `dash`).

L'un des composants qu'il vous faudra maîtriser et exploiter, vu la nature des données sur les emplois et vu les quesitons que l'on peut poser, est la carte géographique.

* Il vous faudra éventuellement (très certianemnt) obtenir le code postal des communes qui sont les centres des bassins d'emplois.
    * Vous pouvez obtenir ces données de plusieurs façons. Une approche simple est d'emprunter [un fichier de données par exemple disponible sur `data.gouv.fr`](https://www.data.gouv.fr/fr/datasets/5a9ac6b9c751df4caed2b133/). Reste ensuite à voir comment intégrer ces données dans votre base de données. Il vous sera très certainement nécessaire d'écrire un script dédié, il serait étonnant que les noms de communes soient orthographiés de la même manière entre ces données et les données d'emplois ... Par exemple, dans les données d'emplois on toruve la commune "BOURG EN BRESSE" alors qu'elle est orthogrpahiée "BOURG-EN-BRESSE" dans les données de `data.gouv.fr` ...
    * Certains centres de bassins d'emplois ne correspondent pas à une commune mais sont désignés par des appellations spécifiques "Centre 77" "ARDECHE CENTRE", "BASSIN D'AVIGNON", etc. Comment traiter ces données ?	 [L'INSEE fournit un fichier de correspondance listant les communes présentes dans chacun des bassins d'emplois, que vous pourriez utiliser.](https://www.insee.fr/fr/information/4652957)

### `dash`

Une fois réglé l'importation des coordonnées des bassins d'emplois (latitude et longitude), on peut obtenir des visualisations interactives réflétant le niveau de tension sur les métiers.

![](./geo_emplois.png)

Ces visualisations, combinées les unes avec les autres peucent iader à comprendre les données ou répondre à des questions sur les emplois. Convenons que les nombres `met` reflètent le besoin en emplois, et que d'une certiane façon on peut y lire la "tension" qu'il y a sur les métiers.

* Cartographier les métiers de manière à lire l'évolution du besoin au fil du temps. A l'aide d'un interacteur approprié, l'utilisateur pourra isolé la plage de temps ou l'année qui l'intéresse.
* Il peut être intéressant d'autoriser l'utilisateur à filtrer les données selon les familles de métiers, ou selon un métier particulier.
    * De la meme manière, il peut être intéressant d'examiner (cartographier, sélectionner les métiers pour lesquels l'offre demplois saisonniers est important, par exemple.
* En complément de la cartographie, on peut restituer des données sous forme tabulaire (pour lister le "top 10" ou "top 50", ...).
    * Aussi, pourquoi ne pas proposer à l'utilisateur de télécharger les données sous forme tabulaire le top 10, ou une fois qu'il a effectuer sa sélection sur la carte ?
* Etc.
