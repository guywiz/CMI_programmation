# CMI_programmation

## Séance 6 `dash`

On peut voir une application web ainsi, elle consiste:

* en une ou plusieurs pages web
* chacune des pages est peuplée de composants (des éléments HTML, des composants dynamiques comme des menus ou des visualisations)
* les évènements sur les pages web (provoqués par l'action de l'utilisateur) apportent des modifications à certians composants des pages de l'appplication.

La construction de l'applicaiton web consiste donc à la construction des pages et des composants, et à la gesiton des évènements.

L'applicaiton elle-même, qu'on appellera le contrôleur, est responsable de la structure de l'application qu'il doit connaître (quels composants, comment il est désigné (son "`id`"), ce à quoi il est destiné, ce qu'il attend, les évènements qui en sont issus, etc.)

Deux autres modules viennent l'épauler:

* Le _modèle_ qui est responsable de la gesiton des données: c'est lui qui connaît comment les données sont organisées (une base de données ? des fichiers ? un mélange des deux ? des donnée sà aller chercher sur le web à l'aide d'une API ? etc.);
    * il sait comment extraire de la base des données selon certains critères, il propose au contrôleur un ensemble de foncitons pour obtenir les données dans une forme adaptée.

* La _vue_ qui est responsable de la création des objets de l'interface graphique de l'application (des menus, des visualisations);
* il propose au contrôleur un ensemble de focntions pour produire des visuels qui sont adaptés aux composants qui ont été mis en place.

### Canevas d'application web construite avec la librairie `dash` (et `plotly-express`)

La librairie `python dash`permet de consrtuire une application web selon les principes évoqués ici.

* Le contrôleur est l'application elle-même.
* La gestion des évènements se fait par le biais de `callback`
    * Un `callback` précise le type d'évènements qu'il écoute. Une fonction lui est rattachée: dès lors qu'un évènement est traité, la fonciton est exéciutée. La fonction retourne un objet (une valeur) utile pour mettre à jour un composant de l'application. 

```
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
...
app.layout = html.Div([ ... ])

@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(patho_name):
    ...
    
if __name__=='__main__':
	app.run_server(debug=False)
```

L'application se lance en exxécutant ce code python, stocké dans le fichier `dashapp.py` disons:

```
$ python dashapp.py 

Dash is running on http://127.0.0.1:8050/

 * Serving Flask app "dashapp" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

```

L'application ets alors accessible depuis un navigateur à l'URL `http://127.0.0.1:8050/` (localhost sur le port 8050).

**Exercice**. Nous avons en cours commenté la construction de l'appplication web permettant de visualiser un histogramme des données de santé. Reprenez ce code pour l'adapter aux données sur les emplois, de manière à visualiser un histogramme qui pourrait montrer:

* Le nombre d'emplois (projets de recrutement, champs `met`) par famille de métiers (axe horizontal) pour une année (choix de l'année dans un menu `dropdown`)
* Le nombre de postes (champs `met`) par année (axe horizontal) pour une famille de métiers (choix dans un menu `dropdown`)
* La proportion de projets de recrutement jugés difficiles (`xmet`) par région (axe horizontal) pour une famille de métiers (choix dans un menu `dropdown`)
* La proportion de postes saisonniers (champs `smet`) par région (axe horizontal) pour une année (choix de l'année dans un menu `dropdown`), pour la famille de métiers `Ouvriers de la construction et du bâtiment`

**Exercice**. Porposez une visualisation où l'utilisateur fixe deux paramètres, à l'aide de deux menus déroulants (dropdown) d'une visualisation, comme exemple:
* La proportion de postes saisonniers (champs `smet`) par région (axe horizontal) pour une année (choix de l'année dans un menu `dropdown`), et pour une famille de métiers (choisi dans un autre menu `dropdown`).
* Proposez une autre visualisation de ce type.

**Exercice**. Proposez une alternative (plus ou moins équivalente) à l'usage d'un histogramme (Pie Chart, Line Chart, etc.).