# CMI_programmation

### Pour en savoir plus ...

Ce [blog de Selva Prabhakaran](https://www.machinelearningplus.com/python/101-pandas-exercises-python/) liste 101 exercices (et propose des solutions) pour les manipulations les plus courantes sur les `DataFrame` (et les `Series`qui mis simplement sont des `DataFrame`à une colonne).

Le [site Kaggle propose aussi une liste de 75 exercices sur les `DataFrame`](https://www.kaggle.com/code/tangchengshun/pandas-75-exercises-with-solutions) (avec solutions).

## Quelques exercices sur les `DataFrame`

Les exercices se penchent sur les [données de consommation (au niveau individuel) mises à disposition sur le site `data.gouv.fr`](https://www.data.gouv.fr/fr/datasets/donnees-de-consommations-et-habitudes-alimentaires-de-letude-inca-3/). Consultez le site pour en savoir plus sur les données.

Nous utiliserons le fichier de données `Conso_compo_alim.csv` disponibles dans le dossier `data` de ce dépôt.

### Données de consommation

Ces données restent difficiles à interprétées de manière certaine (le protocole de récolte semble assez complexe et technique). Nous conviendrons:

* Que la colonne NOIND est le numéro d'un individu ayant participé à l'expérience. Une ligne associée à ce numéro correspond à une quantité d'aliment consommé par cet individu. Ainsi, la ligne 2 indique que l'individu 110100101 a consommé 147.5 grammes d'eau du robinet.
    * L'aliment consommé est indiqué à la colonne `occ_alim_libelle` dont les libellés sont suposés "normalisés",
    * La quantité consommée est indiquée à la colonne `qte_conso` en grammes (avec une correspondance évidente 1g liquide = 1ml, pour tous les liquides, jus, etc.).
* Nous utiliserons aussi le libellé plus "libres" apparaissant dans les colonnes `aliment_libelle_INCA3` mais laisserons de côté le libellé `aliment_libelle_FX` en langue anglaise.
* Nous nous intéresserons aussi aux colonnes:
    * `occ_hdeb` précisant l'heure à laquelle l'aliment est absorbé.
    * `occ_lieu` qui code le lieu où ets consommé l'aliment. On trouve à la fin d'[une notice](https://www.data.gouv.fr/fr/datasets/r/6262cb5e-747e-442a-97b0-934213a7d504) la signification des codes:
        1. A la maison
        2. Chez amis/famille/assistante maternelle...
        3. A la cantine au travail/crèche/école/collège/lycée/université
        4. Pas à la cantine, au travail/école/collège/lycée/université
        5. Restaurant/café/fast-food/sandwicherie sur place...
        6. Dehors : rue, parc, plage...
        7. Dans les transports (train/avion/voiture...)
        8. Autre lieu

### Questions

A chaque fois, donnez le script qui permet de répondr eà la quesiotn, et une explication en une phrase précisant ce qu'il faut calculez pour obtenir la réponse à la question, et comment le script procède pour mener le calcul.

* Combien d'individus l'enquête concerne-t-elle ?
* Combien de prises d'aliments concerne-t-elle, en moyenne, pour chacun des individus ?
* On s'attend à ce qu els aliemnts soient pris le plus souvent à la maison -- confirmez cette hypothèse.
    * Quel ets le deuxième lieu de consommation le plus fréquent ?
* Quel aliment (consommé par un individu ayant participé à l'enquête) contient le plus de `magnesium` ? (Peut-être y a -t-il plusieurs réponses possibles à la question)
* Certains aliments sont à base ou contiennent du __chocolat__ (si on se réfère au libellé qui apparait en colonne `aliment_libelle_INCA3`. Combien en moyenne ces aliments contiennent-ils de `magnesium` ?
* Y a-t-il des aliments sans sucre ?
    * Quel est le poids moyen d'une portion (consommé par un individu) d'un tel aliment ?
    * Qu'a consommé l'individu ayant consommé le plus de sucre (dans une portion) ?
* Quels sont les aliments contenant de la noix ?
* Les pizza (tous types) contiennent-elles en moyenne plus de `fer`ou plus de `cuivre` ?