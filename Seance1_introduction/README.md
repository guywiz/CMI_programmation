# CMI_programmation

## Séance d'introduction

Cette première séance fait une revue du langage python afin de poser les bases.

### Structures de données

 `python`propose essentiellement deux structures de données: les _listes_ et les _dictionnaires_.
 
 * Les listes regroupent des items de type variés dont l'ordre importe dans la liste: on accès aux éléments de la liste à partir de leur indice (qui commence à 0). A noter, c'est une particulartié de `python`, que les éléments n'ont pas nécessairement à être de même type.
  * `range` permet de créer une liste d'netiers consécutifs (pratique pour effectuer une simple itération
  * `for x in L`
  * `L[i]`, `L[:i]`, `L[i:]`, `L[-i]`, etc.
 * Construction d'une liste à la volée (List Comprehension) `[x^2 for x in range(10)]`
 * Tri
 * Filtrage d'une liste `filter(lambda x: math.sqrt(x) < 2, range(10))`
 * On peut parcourir une liste en itératn simultanément sur ses valeurs et ses indices (pratique !) `for i, x in enumerate(L)`

* Les dictionnaires sont des ensembles de paires (clé, valeur) dont l'ordre n'importe pas.
 * On peut accéder aux clés du dictionnaire `D.keys()`, ou à ses valeurs `D.values()` ou à ses paires `D.items()`

