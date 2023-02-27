# CMI_programmation

## Séance 3 - visualisations avec `plotly`

Vous avez déjà fait une oremière visualisation avec `plotly` (un barchart à partir des données d'appels téléphoniques).

La librarie `plotly`offre un nombre relativement grand de visualisations maintenant devenues standard. [Prenez-le temps d'aller jeter un coup d'oeil](https://plotly.com/python/).

Nous utiliserons [les données sur les projets de recrutements (emplois) de 2017 à 2022](https://github.com/guywiz/CMI_programmation/tree/main/data).

### Consignes pour l'écriture du code

Veillez à produire du code bien structuré. Vous reprendrez ce code la fois prochaine poru le faire évoluer, et il sera utile d'avoir bien séparer les traitements, de les avoir bien isolé dans des fonctions. En particulier, il est avisé de séparer la _préparation des données_ (`pandas`) de la _configuration de la visualisation_ (`plotly`).

### Line Plots

* **Exercice.** Sur le modèle proposé `Average High and Low Temperatures in New York`, construisez des visualisations :
    * de l'évolution des emplois (projets de recrutements) sur trois familles de métiers, en montrant les courbes des emplois (`met`), des emplois jugés difficiles `xmet`) et des emplois saisonniers (`smet`) sur la période 2017 - 2020.
    * ou de l'évolution des emplois (projets de recrutements) sur trois régions, en montrant les courbes des emplois (`met`), des emplois jugés difficiles `xmet`) et des emplois saisonniers (`smet`) sur la période 2017 - 2020.

### Pie Charts
* **Exercice.** Proposer une question sur les données qui peut trouver répoinse à l'aide d'une représentaiton en Pie Chart (Camembert). Explorez les paramètres de formes du Pie Charts (choix de l apalette de couleurs, légende, effets de style, ...).

### Box Plots (boîtes à moustaches)

Les Box Plots permettent d'illustrer les quartiles (inférieur, supérieur et médiane) d'un ensemble d'observations.

* **Exercice.** Utilisez une visualisation Box Plots pour illustrer les quartiles des emplois, tous domaines confondus, sur les différents départements de France en 2017.

* **Exercice.** Même question mais pour un secteur donné, en présentant une boîte à moustache sur chacune des années.

### Bubble Maps

* **Exercice.** Utilisez une visualisation Bubble Maps pour montrer la distributiuon des offres d'emplois de `Cuisiniers` sur l'ensemble du territoire au niveau régional. [Il vous faudra pouvoir trouver les coordonnées géographiques des régions](https://www.ign.fr/reperes/centre-geographique-des-regions-metropolitaines).

    *  Reprenez la constructiun d'une carte similaire au niveau départemental.
