# CMI_programmation

## Epreuve individuelle

Les questions se penchent sur les données d'emplois, plus précisément sur les projets de recrutement qui ont cours par région/département/commune, [disponibles sur le site data.gouv.fr](https://www.data.gouv.fr/fr/datasets/enquete-besoins-en-main-doeuvre-bmo/).

### Données sur les besoins en main d'oeuvre

Vous travaillerez sur les données répertoriant les besoins en main d'oeuvre pour l'année XXX. Vous pouvez télécharger ces données à partir de ce lien.

Les données sont accompagnées d'un fichier décrivant les variables observées pour chacun des projets de recrutement, dont vous prendrez connaissance.

Les données elles-mêmes sont stockées dans un fichier csv séparé.

Les différentes variables renseignent le nombre de projets de recrutement par type de métiers et par région et département, en soulignant les projets _jugés difficiles_ ou ceux qui correspondent à des emlpois _saisonniers_.

### Questions

Dans les colonnes `met`, `xmet` et `smet`, certaines données ne sont pas renseignées et sont remplacées par un simple astérisque `*`. Cela provoque une interprétation par `pandas` du contenu de ces colonnes en tant que chaînes de caractère.

* Quelle(s) instruction(s) permet de vérifier que si la colonne `met`vaut `*`, il en alors va de même pour les colonnes `smet` comme pour la colonne `xmet` ?

On filtre les données pour ne garder que les lignes où `met`est égal à `*`.

`emplois_non_valides_met = emplois[emplois['met'] == '*']`

On filtre ces données pour ne garder que les lignes pour lequelles `smet` est égal à `*`, et on constate que toutes sont concernées (nbombre de lignes du `DataFrame`résultant). La même manipulation vaut pour `xmet`.

`emplois_non_valides_met[emplois_non_valides_met['smet'] == '*']`

--

* Calculer le `DataFrame` ne contenant que les lignes  pour lesquelles la colonne `met` contient bien (une chaîne de caractères représentant) un entier ?

`emplois_valide_met = emplois[emplois['met'] != '*']`

* Quelle instruction appliquée au résultat obtenu permet de convertir la colonne `met`en un entier ? (Astuce: regardez du côté de la méthode `astype`).

`emplois_valides_met['met'] = emplois_valide_met['met'].astype(int)`

--

* Combien de projets de recrutements sont répertoriés pour l'année XXX (2017, 2018, ..., 2022) ?

`emplois_valides_met['met'].sum()`

* Combien parmi ceux-ci concernent un emploi de YYY (`Coiffeur`, `Plombier`, `Journaliste`, `Infirmier`, `Electricien`, `Soudeur`, `Juriste`, `Boucher`, `Charcutier`, `Cuisinier`, `Concierge`, `Graphiste`)  ?

`emplois_valides_met[emplois_valides_met['Nom métier BMO'].str.contains('Coiffeur')]['met'].sum()`

--

* Dans quelle région le nombre de recrutements jugés difficiles est-il le plus grand ?

On écarte le slignes non renseignées:

`emplois_valides_met_xmet = emplois_valides_met[emplois_valides_met['xmet'] != '*']`

On convertit la valeur `xmet`en entier:

`emplois_valides_met_xmet['xmet'] = emplois_valides_met_xmet['xmet'].astype(int)`

(on peut ignorer le message qui n'est qu'un "Warning")

et on calcule:

`emplois_valides_met_xmet[['NOM_REG', 'xmet']].groupby('NOM_REG').sum()`

pour constater que le besoin est le plus grand en Ile-de-France.

--

* En Nouvelle-Aquitaine, quel est le besoin (parmi les recrutements jugés difficiles) en moyenne sur les familles de métiers ?

On filtre les données pour ne conserver que les chiffres concernant la Nouvelle-Aquitaine:

`emplois_valides_met_xmet_NA = emplois_valides_met_xmet[emplois_valides_met_xmet['NOM_REG'] == 'Nouvelle-Aquitaine']`

et on calcule:

`emplois_valides_met_xmet_NA[['Lbl_fam_met', 'xmet']].groupby('Lbl_fam_met').sum()`

pour constater que la demande (en projets jugés difficiles) est la plus forte pour les métiers liés aux "Fonctions liées à la vente, au tourisme et aux services".

--

* En ZZZ (département Gironde, Landes, ...), sur quelle commune le nombre de projets de recrutement saisonniers est-il le plus grand ?

On filtre les données pour ne garder que les lignes qui sont renseignées, on convertit les données en type entier, puis on regroupe par commune avant de calculer le total de projets de recrutements saisonniers:

`emplois_saisonniers = emplois[emplois['smet'] != '*']`

`emplois_saisonniers['smet'] = emplois_saisonniers['smet'].astype(int)`

`emplois_saisonniers_Gironde = emplois_saisonniers[emplois_saisonniers['NomDept'] == 'Gironde']`

`emplois_saisonniers_Gironde[['NOMBE22', 'smet']].groupby('NOMBE22').sum()`

pour trouver que le nombre de métiers saisonniers ets le plus grand sur la commune de Bordeaux.

* En Gironde toujours, pour quel métier le nombre de projets de recrutements saisonniers est-il le plus grand ?

Il faut regrouper les donnnées (pour la Gironde) selon les métiers et calculer la somme des valeurs `smet`, puis extraire la métier qui correspond à cette valeur maximum:

`max = emplois_saisonniers_Gironde[['Nom métier BMO', 'smet']].groupby('Nom métier BMO').sum().max()`

`mask = emplois_saisonniers_Gironde[['Nom métier BMO', 'smet']].groupby('Nom métier BMO').sum()['smet'] == max`

`emplois_saisonniers_Gironde[['Nom métier BMO', 'smet']].groupby('Nom métier BMO').sum()[mask]`

qui permet d'identifier le métier de _Viticulteurs, arboriculteurs salariés_.

* Dans quelle région la proportion des projets de recrutements de `Maraîcher` qui sont des emplois saisonniers est la plus grande ?

Il faut d'abord convertir le champ `met` en entier (on ne l'a pas fait), puis regrouper selon les régions, avant de calculer le ratio:

`emplois_saisonniers['met'] = emplois_saisonniers['met'].astype(int)`

`compil_emplois_saisonniers = emplois_saisonniers[['NOM_REG', 'met', 'smet']].groupby('NOM_REG').sum()`

`compil_emplois_saisonniers['ratio'] = compil_emplois_saisonniers['smet'] / compil_emplois_saisonniers['met']`

pour trouver que ce ratio est le plus grand dans la région de Corse.
