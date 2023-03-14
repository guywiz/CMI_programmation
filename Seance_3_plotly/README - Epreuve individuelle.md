# CMI_programmation

## Epreuve individuelle

Les questions se penchent sur les données de santé. Les données, [disponibles sur le site data.gouv.fr](https://www.data.gouv.fr/fr/datasets/effectif-de-patients-par-pathologie-sexe-classe-dage-et-territoire-departement-region/) listent le nombre de personnnes souffrant de pathologies, selon différents profils (catégories d'age, homme ou femme) et localisation géographique (département, région).

[Les données sont disponibles sur le dépôt du cours](https://github.com/guywiz/CMI_programmation/tree/main/data) (fichier `Pathologies.csv`).

Les différentes variables sont décrites [dans le fichier `Pathologies_variables.txt`](https://github.com/guywiz/CMI_programmation/tree/main/data/Pathologies_variables.txt) (recopié du site d'origine des données).

### Questions

Parmi les pathologies considérées, l'une d'elles reste vagues et difficiles à interpréter: "Autres affections de longue durée (dont 31 et 32)" (colonnes`patho_niv1`, `patho_niv2` et `patho_niv3`).

* Calculer le `DataFrame` ne contenant que les lignes pour lesquelles les colonnes `patho_nivX` ne contiennent pas cette valeur.

`df = pd.read_csv('Pathologies.csv', sep=';')`

`autres_affects = 'Autres affections de longue durée (dont 31 et 32)'`

`df = df[df['patho_niv1'] != autres_affects]`

--

La colonne `libelle_classe_age` précise la catégorie d'age des patients (pour chaque pathologie), sous la forme d'une expression "de X à Y ans".

* A partir du contenu de cette colonne `libelle_classe_age`, fabriquez deux nouvelles colonnes qui contiennet les bornes inf et sup de l'intervalle d'age décrit de manière litérale. Les classes d'âges "plus de 95 ans" et "tous âges" devront êtr etraitées de manière spécifique en prenant par exemple comme âge maximum 120 ans, disons.

On définit deux fonctions:

```
def age_inf(libelle):
    if 'plus' in libelle:
        return 95
    elif 'tous' in libelle:
        return 0
    else:
        return int(libelle.split(' ')[1])

def age_sup(libelle):
    if 'plus' in libelle:
        return 120
    elif 'tous' in libelle:
        return 120
    else:
        return int(libelle.split(' ')[3])
```

qu'on utlise ensuite pour créer les colonnes:

`df['age_inf'] = df['libelle_classe_age'].apply(age_inf)`

`df['age_sup'] = df['libelle_classe_age'].apply(age_sup)`

--

* Combien de pathologies sont répertoriées sur toute la durée de l'enquête ?
    * de niveau 1 ? `len(df['patho_niv1'].unique())`
    * de niveau 2 ? `len(df['patho_niv2'].unique())`
    * de niveau 3 ? `len(df['patho_niv3'].unique())`

* Parmi celles-ci combien concernent des personnes de moins de 30 ans (jusqu'à 29 ans inclus) ?

`len(df[df['age_sup'] < 30]['patho_niv1'].unique())` (idem pour les niveaux 2 et 3)

--

* Quelle pathologie (niveau 3) concerne le plus grand nombre de personnes (le plus grand nombre de patients pris en charge (colonne `ntop`) ?

max_patho = 

* Quelle pathologie (niveau 3) atteint plus les femmes que les hommes (au regard du nombre de prises en charge `ntop`) ?

`df_agreg_ages = df[['patho_niv3', 'ntop']].groupby('patho_niv3').sum()`

puis on calcule la valeur maximale:

`max_patho = df_agreg_ages.max()`

et on trouve (par inspection simple ou en filtrant) qu'il s'agit des "Hospitalisations ponctuelles".

--

* En Nouvelle-Aquitaine (départements Charente (16), Charente-Maritime (17), Corrèze (19), Creuse (23), Dordogne (24), Gironde (33), Landes (40)):
    * quelle pathologie est dominante sur toute la durée (de 2015 à 2020) ?
    * quelle pathologie a le plus progressé si on compare le début de la période (2015) à la fin de période de l'enquête (2020) ?

On filtre les données pour ne conserver que les entrées relatives à la Nouvelle-Aquitaine.

```
def in_NA(dept):
    return dept in ['16', '17', '19', '23', '24', '33', '40']
```

On fabrique une colonne indiquant si le département est en Nouvelle-Aquitaine:

`df['in_NA'] = df['dept'].apply(in_NA)`

puis on filtre:

`df_NA = df[df['in_NA']]`

et on repernd le même calcul que précédemment:

`df_NA_agreg = df_NA[['patho_niv3', 'ntop']].groupby('patho_niv3').sum()`

pour trouver encore ici qu'il s'agit des "Hospitalisations ponctuelles".

Pour la progression des pathologies, il nous faut isoler les entrées sur l'année 2015, puis sur l'année 2020 (toujours en Nouvelle-Aquitaine), en faisant par exemple:

```
df_2015 = df_NA[df_NA['annee'] == 2015]
df_2022 = df_NA[df_NA['annee'] == 2022]
```

Mais alors on obtient des DataFrames qui n'ont pas le même nombre d'entées (lignes). L'effort pour réconcilier les donnée ssur ces deux années est considérables. A l'évidence, les données ne sont pas structurées pour faciliter le traitement nécessaires pour répondre à une telle question.

--

* En Gironde (département 33), quelle pathologie (niveau 3) atteint plutôt les hommes de moins de trente ans ?


