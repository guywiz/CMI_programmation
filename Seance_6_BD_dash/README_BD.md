# CMI_programmation

## Séance 6 BD

Cette séance est revenue sur les bases de données, leur conception et leur construction.

Deux avantages des bases de données ont été soulignés, et ils se manifestent dans le cas de la base des données de santé: la taille des données stockées dans la base (par opposition à la taille du fichier `csv` d'origine), et la souplesse qui est gagnée sur les données pour formuler des requêtes plus fines.

Dans le cas des données de santé, le gain est un facteur 10. Les données d'origine font plus de 500Mo alors que la base est de taille d'un peu plus de 40Mo.

Mais le gain se fait plus sentir sur la possibilité de formuler certaines requêtes sur les données - qu'il était difficile d'efectuer sur un `DataFrame` contenant le fichier `csv` d'origine.
	
C'était le cas pour un exercice précédent où l'on souhaitait calculer l'évolution (en termes de nombre d'hospitalisation) des pathologies entre 2015 et 2020. La difficulté tient au fait que l'année concernée par les données (le nombre `ntop` d'hospitalisation apparait en colonne `annee`. Les choses auraient été facilitées si les chiffres avaient été livrés dans des colonnes séparées (une colonne pour chaque année).

Les bases de données permettent de se sortir de cette impasse. L'opération de _jointure_ permet en effet de construire une relation (eun table) qui suit le schéma qui nous intéresse (une colonne pour les chiffres d'une année).

Le mécanisme de jointure est assez simple/ Il consiste à effectuer le produit cartésie, des éléments de deux tables (on peut aussi faire une jointure d'une table avec elle-même), et de ne retenir du produit cartésien que certrains éléments, là où des attributs coincident.

Ainsi, les données permetant de calculer aisément l'évolution du nombre d'hospitalisation entre 2015 et 2020 peut se faire avec la jointure:

```
		SELECT A.pathologie, A.npop AS npop2015, A.ntop AS ntop2015, B.npop AS npop2020, B.ntop AS ntop2020, A.dept
		FROM population A, population B
		WHERE A.pathologie = B.pathologie AND A.dept=B.dept AND A.annee = 2015 AND B.annee=2020;
```

On effectue un produit cartésien de la table `population` avec elle-même:

`FROM population A, population B`

(en désignant ces deux "copies" par des noms différents, `A` et `B`. Mais on ne retient de ce produit cartésien que les tuples pour lesquels certaines contraintes sont satisfaites:

`WHERE A.pathologie = B.pathologie AND A.dept=B.dept AND A.annee = 2015 AND B.annee=2020`

et du produit cartesien, on ne s'intéresse qu'à certians attributs qui seront retournés:

`SELECT A.pathologie, A.npop AS npop2015, A.ntop AS ntop2015, B.npop AS npop2020, B.ntop AS ntop2020, A.dept`

P.S. La mécanique qui permet d'effectuer une jointure entre des tables différentes est similaire, bien qu'il soit nécessaire de préciser ce qui doit être fait des attributs qui existent dans une table et pas dans l'autre. On pourra au besoin explorer cette quesiton plus tard.

**Exercice**. Vous avez travaillé dans vos équipes-projet à la conception d'une base de données reprenant les données sur les emplois (projets de recrutement) entre 2017 et 2022.

Vous avez aussi travaillé à l'alimentation de cette base à partir des diffférents fichiers `csv`.
