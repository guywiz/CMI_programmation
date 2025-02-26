# CMI_programmation - Leçon 4

Cette leçon se penche sur la programmation objet, c'est-à-dire le paradigme de classe avec le langage `python`.

## Introduction

Les classes proposent une façon pratique et conceptuellement solide d'organiser le code selon les responsabilités (portées par les fonctions).

Une classe rassemble des variables (de classe) et des méthodes destinées à des tâches d'une même nature.

Typiquement dans l'application que vous êtes à construire, on peut imaginer utiliser une classe `DataManager` qui chapeaute les responsabilités relatives à la gestion des données de l'application. Par exemple,

- le `DataManager` est une façade qui masque les détails d'implémnetation de la connexion à une base de données, ou de la gestion des différents fichiers stockés localement, etc.
- de la même manière, le `ViewManager` masque les détails d'implémentation du calacul des diférents graphiques utiles au dashboard de votre application.

Ainsi, l'applicaiton elle-même utilisera une instance de chacun de ces objets.

### `class`

Comment construit-on une classe ? AVec le mot-clé `class`

```
class DataManager():
    def __init__(<params>):
        ...
    
```

La méthode `__init__` est imposée et correspond à ce qu'on appelle le constructeur de la classe, c'est-à-dire les choses à mettre en place au moment où une instance de la classe est créée.

On crée une instance de la classe en faisant:

```
data_manager = DataManager(<params>)
```

### Méthodes

La fonction `__init__` est le constructeur de la classe. La classe peut contenir aussi d'autres méthodes, disons par exemple

```
def load_data(<paramas>):
    # do domething to load data
    return <something or nothing>

def process_data(<params>):
    # process data, filter or transform
    return <something or nothing>
```

Ces fonctions, les méthodes de la classe, peuvent alors être invoquées depuis l'instance de ckasse qui a été créée:

```
data_manager.load_data(<params>)
data_manager.process_data(<params>)
```

### Variables de classe

Une classe peut contenir des variables qui sont alors accessibles par n'importe quelle méthode de la classe.

Ces variables sont souvent instanciées au niveau du constructeur.

```
    def __init__(<params>):
        self.file_path = "<chemin relatif ou absolue a un fichier de donnees de l'app>"
        # ou encore
        self.database_url = "<une url pour accéder à une base de données>"
        ...
```

Ainsi, on pourrait avoir:

```
def load_data(<paramas>):
    # do domething to load data
    with open(self.filepath,'r') as fp:
        # ...
    return <something or nothing>
```

### Exercice

Reprenez le code que vous avez écrit pour produire une visualisation des données d'appels téléphoniques, et organisez-le à l'aiode de classes qui sépare bien les responsabilités: modèle, vue et contrôleur.

Notez que le contrôleur lui aussi correspond à une classe `Dash`, qui est défini dans la librairie `dash`:

```
app = Dash(__name__)
```


