# CMI_programmation

## Epreuve individuelle

Les questions se penchent sur les données de santé. Les données, [disponibles sur le site data.gouv.fr](https://www.data.gouv.fr/fr/datasets/effectif-de-patients-par-pathologie-sexe-classe-dage-et-territoire-departement-region/) listent le nombre de personnnes souffrant de pathologies, selon différents profils (catégories d'age, homme ou femme) et localisation géographique (département, région).

[Les données sont disponibles sur le dépôt du cours](https://github.com/guywiz/CMI_programmation/tree/main/data) (fichier `Pathologies.csv`).

Les différentes variables sont décrites [dans le fichier `Pathologies_variables.txt`](https://github.com/guywiz/CMI_programmation/tree/main/data/Pathologies_variables.txt) (recopié du site d'origine des données).

### Questions

La colonne `libelle_classe_age` précise la catégorie d'age des patients (pour chaque pathologie), sous la forme d'une expression "de X à Y ans".

* A partir du contenu de cette colonne `libelle_classe_age`, fabriquez deux nouvelles colonnes qui contiennet les bornes inf et sup de l'intervalle d'age décrit de manière litérale. Les classes d'âges "plus de 95 ans" et "tous âges" devront êtr etraitées de manière spécifique en prenant par exemple comme âge maximum 120 ans, disons. 

--

Parmi les pathologies considérées, l'une d'elles reste vagues et difficiles à interpréter: "Autres affections de longue durée (dont 31 et 32)" (colonnes`patho_niv1`, `patho_niv2` et `patho_niv3`).

* Calculer le `DataFrame` ne contenant que les lignes pour lesquelles les colonnes `patho_nivX` ne contiennent pas cette valeur.

--

* Combien de pathologies sont répertoriées sur toute la durée de l'enquête ?
    * de niveau 1 ?
    * de niveau 2 ?
    * de niveau 3 ?

* Parmi celles-ci combien concernent des personnes de moins de 30 ans (jusqu'à 29 ans inclus) ?

--

* Quelle pathologie (niveau 3) concerne le plus grand nombre de personnes (le plus grand nombre de patients pris en charge (colonne `ntop`) ?

* Quelle pathologie (niveau 3) atteint plus les femmes que les hommes (au regard du nombre de prises en charge `ntop`) ?

--

* En Nouvelle-Aquitaine (départements Charente (16), Charente-Maritime (17), Corrèze (19), Creuse (23), Dordogne (24), Gironde (33), Landes (40)):
    * quelle pathologie est dominante sur toute la durée (de 2015 à 2020) ?
    * quelle pathologie a le plus progressé si on compare le début de la période (2015) à la fin de période de l'enquête (2020) ?

--

* En Nouvelle-Aquitaine, sur quelle commune le nombre de "Maladie de Parkinson" (pathologie niveau 3)
    * est-elle la plus importante (sur toute la période) ?
    * a-t-elle le plus progressé entre 2015 et 2020 ?

--

* En Gironde (département 33), quelle pathologie (niveau 3) atteint plutôt les hommes de moins de trente ans ?

* En Gironde toujours, on considère maintenant non pas le nombre absolu de patients pris en charge mais le taux relatif à la population de référence (colonne `npop`). Dans quelle commune le nombre relatif de patients pris en charge est le plus petit ?
