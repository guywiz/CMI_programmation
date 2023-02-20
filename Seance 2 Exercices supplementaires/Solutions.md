# CMI_programmation

## Exercices

On suppose avoir chargé les données:

`import pandas as pd`

`conso_df = pd.read_csv('Conso_compo_alim.csv', sep=';')`

A chaque fois, donnez le script qui permet de répondre à la quesiotn, et une explication en une phrase précisant ce qu'il faut calculez pour obtenir la réponse à la question, et comment le script procède pour mener le calcul.

* _Combien d'individus l'enquête concerne-t-elle ?_

La colonne `NOIND` renseigne le numéro d'un individu (la ligne correspond à la consommation d'aliments). Il faut donc trouver combuen de valeurs différentes contient cette colonne.

`len(conso_df['NOIND'].unique())`

L'enquête concerne donc 4114 personnes.

* _Combien de prises d'aliments concerne-t-elle, en moyenne, pour chacun des individus ?_

Il faudrait pour chaque individu calculer le nombre de lignes le concernant. On peut obtenir cette valeur en créan artificiellement une colonne dont la valeur est systématiquement 1 et faire un regroupement par individu avant d'appliquer l'opérateur `sum`.

`conso_df['Prise_aliments'] = 1`

`prises_individuelles = conso_df[['NOIND', 'Prise_aliments']].groupby(['NOIND']).sum()`

Reste à calculer la valeur moyenne de la colonne `Prise_aliments` dans ce `DataFrame`:

`prises_individuelles['Prise_aliments'].mean()`

Le nombre de prises par individu est en moyenne de 62.3

* _On s'attend à ce que les aliments soient pris le plus souvent à la maison -- confirmez cette hypothèse._
    * _Quel est le deuxième lieu de consommation le plus fréquent ?_

On peut encore ici fois utiliser la colonne 'Prise_aliments' (qui vaut systématiquement 1), et faire un regroupement selon la valeur de la colonne `occ_lieu` avant d'appliquer l'opérateur `sum`:

`prises_lieux = conso_df[['occ_lieu', 'Prise_aliments']].groupby(['occ_lieu']).sum()`

On constate que le domicile dépasse largement tous les autres lieux de consommation. Il ets plus de dix fois égal à l'occurence du second lieu (qui est `Chez amis/famille/assistante maternelle...`).

* Quel aliment (consommé par un individu ayant participé à l'enquête) contient le plus de `magnesium` ? (Peut-être y a -t-il plusieurs réponses possibles à la question)

La quantité de magnesium de l'aliment consommé apparait en colonne `magnesium`. Il nous faut trouver la valeur maximum apparaissant dans cette colonne et les aliments pour lesquelles cette valeur est la valeur maximum.

`max_magnesium = conso_df['magnesium'].max()`

`conso_max_magnesium = conso_df[conso_df['magnesium'] == max_magnesium]`

On visualise ensuite les 14 aliments qui atteignent cette valeur maximum:

`conso_max_magnesium[['aliment_libelle_INCA3', 'magnesium']]`

et on constate que l'aliment atteignant la valeur max est la portion de basilic (!).

* _Certains aliments sont à base ou contiennent du __chocolat__ (si on se réfère au libellé qui apparait en colonne `aliment_libelle_INCA3`. Combien en moyenne ces aliments contiennent-ils de `magnesium` ?_

On considère un `DataFrame` réduit aux aliments consommés (lignes de `conso_df`) dont le libellé fait apparaître le mot `chocolat`.

`conso_chocolat = conso_df[conso_df['aliment_libelle_INCA3'].str.contains('chocolat')]`

On calcule ensuite la valeur moyenne de la colonne `magnesium` de ce frame:

`conso_chocolat['magnesium'].mean()`

et on trouve la valeur 56.5 (à interpréter en `mg` ?).

* _Y a-t-il des aliments sans sucre ?_

On considère le `DataFrame` réduit aux aliments pour lesquels la valeur de la colonne `sucres` est égale à 0. (On peut se questionner sur la colonne `glucides` ...)

`conso_no_sucres = conso_df[conso_df['sucres'] == 0]`


* _Quel est le poids moyen d'une portion (consommé par un individu) d'un tel aliment ?_

Reste à calculer la moyenne de la variable (colonne) `qte_conso`:

`conso_no_sucres['qte_conso'].mean()`

* _Qu'a consommé l'individu ayant consommé le plus de sucre (dans une portion) ?_

La quantité maximum de sucres consommée en une portion est:

`max_sucres = conso_df['sucres'].max()`

Reste à filtrer les données pour ne conserver que les lignes où cette valeur est égale à la valeur maximale.

`conso_df[conso_df['sucres'] == max_sucres]`

La réponse à la quesiton est difficile à cerner tant le nombre d'individus ayant consommé une quantité maximale de sucre est grand. Il y en a 1672:

`len(conso_df[conso_df['sucres'] == max_sucres]['NOIND'].unique())`

* _Quels sont les aliments contenant de la noix ?_

On isole les lignes pour lesquelles le libellé contient le mot noix:

`conso_noix = conso_df[conso_df['aliment_libelle_INCA3'].str.contains('noix')]`

Et on liste les différents libellés de ces lignes (prises d'aliments):

`conso_noix['aliment_libelle_INCA3'].unique()`

* _Les pizza (tous types) contiennent-elles en moyenne plus de `fer`ou plus de `cuivre` ?_

`pizzas = conso_df[conso_df['aliment_libelle_INCA3'].str.contains('pizza')]`

Les données contiennent 934 lignes faisant état d'une consommation de pizza. Pour chacune de ces instances, la quantité de fer est supérieure à la quantité de cuivre puisque le frame

`pizzas[pizzas['fer'] < pizzas['cuivre']]`

est vide.

