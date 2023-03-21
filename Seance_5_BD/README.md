# CMI_programmation

## Séance 5

Cette séance se penche sur le concept, et sur l'implémentation des bases de données.

Les deux jeux de données publiques que nous avons utilisés jusqu'à maintenant

* Emplois ("projets de recrutements") entre 2017 et 2022
* Santé publique (nombre de patients ayant été traités pour certaines pathologies entre 2015 et 2020)

ne sont pas organisés de manière "optimale". Plus précisément, le chargement des fichiers (tableurs) dans des DataFrame `pandas` exigent ensuite des manipulations parfois difficiles pour répondre à certaines questions.

* C'est le cas des données de santé publiques. Les données sont répertoriées par année (colonne `annee`) et l'extraction des données dans des DataFrame séparés pour calculer une progression entre deux années (par exemple) n'est pas aisée. Pour les emplois, l'éclatement des données sur plusieurs fichiers avec des entêtes différentes pour désigner les mêmes quantités est problématique. Par ailleurs, beaucoup d'informations sont répétées dans un même tableur ou entre fichiers. Outre l'espace inutilement occupée, ces redondances introduisent un risque d'incohérence des données.

Les principes de conception des bases de données vise essentiellement à éviter les incohérences: une donnée (le nom d’une pathologie, d'une catégorie d'emplois, ...) ne devrait être stocké qu’à un seul endroit qui fait foi. Cela suppose alors de veiller à ne pas répliquer la donnée et exige des mécanismes d’agencement des données pour servir les besoins d’une application.

Dans les deux jeux de données, on s’aperçoit que quantité d’informations sont stockées autant de fois qu’il y a de mesures qui sont effectuées ... On a avantage à organiser l’information de manière à stocker de manière distincte les informations qui décrivent les emplois, de celles qui décrivent les comptages qui sont effectués.

La théorie des bases de données élabore un formalisme proposant différentes normes, et une méthodologie qui permet de « convertir » les données vers l’une de ces normes, ou de vérifier qu’une norme est bien respectée par un schéma de base de données.
Le schéma doit être pensé en termes d’entités (d’un système géré par une application), et de liens (association) entre ces entités. Par exemple, dans le contexte d’une application commerciale, on distinguera les informations qui décrivent un client, de celles qui dérivent les transactions (factures, livraisons, etc.).

**Exercice.** Proposer un schéma entités - association pour décrire les données sur les emplois. Même question pour les données de santé.

### Théorie des bases de données – Formes normales

Nous avons esquissé les principes de la conception des bases de données, et allons revenir vers nos jeux de données pour s’assurer de la bonne conception des bases.

Une base consiste à désigner chacune des entités du « système », et les champs qui la décrivent. Cela donne lieu souvent à une vision « tabulaire » : chaque ligne de la table décrit l’une de ces instances, et les colonnes contiennent les valeur des différents champs.

_Première forme normale_. Cette première « norme » impose de ne pas stocker dans un champ des valeurs multiples. C’est le cas des données telles qu’elles sont proposées au téléchargement.

**Exercice.** Modifiez le schéma des données santé / emplois pour respecter la première forme normale.

_Seconde forme normale_. Cette seconde « norme » nécessite d’introduire la notion de clé primaire: un champ qui identifie une instance de manière unique.

Le schéma répond à cette norme si tous les autres champs sont déterminer par cette clé (on a une relation fonctionnelle entre clé et valeurs). Ca n’est évidemment pas le cas pour les données sur le comptage.

Une façon de faire passer un schéma en seconde forme normale consiste à scinder les données, faisant apparaître des entités distinctes.

Mais alors les deux entités sont liées (puisqu’elles étaient décrites en une même table). Pour que la référence entre elles entités (l’association) puisse être décrite, il faut introduire la notion de clé étrangère: une clé utilisée comme champ pour matérialiser l’association.

**Exercice.** Modifiez le schéma des données de santé / emplois pour respecter la seconde forme normale.

La normalisation peut être poussée encore plus loin, mais restons-en là pour l’instant. _La "philosophie" qui sous-tend la théorie des bases de données est de chercher une organisation qui favorise le maintien de la cohérence des données. Cela vise à éliminer les redondances, les effets transitifs (des liens fonctionnels entre les diffférentes attributs), et amène à éclater les données sur plkuysieurs relations. Une bonne approche lorsque l'on conçoit une base est de modéliser en amont l'espace d'information par des entités (du système qui est décrit) et des relations entre celles-ci._

### Interroger une base de données – langage SQL
Les systèmes de gestion de bases de données implémentent les procédures de recherche d’information dans des « tables » de manière très performantes. Les recherches dans la base doivent être rendues explicites à l’aide d’un langage dédié: `SQL`.

Comme tout langage de programmation, `SQL` utilise certains mots réservés pour former des expressions qui sont ensuite évaluées:

`SELECT * FROM Customers;`

* Le mot `SELECT` correspond à une interrogation (nous verrons d’autres actions possibles, comme `INSERT` ou `UPDATE`
* désigne, comme dans une expression régulière « toute valeur possible »
* `FROM` précède l’expression qui décrit la « relation » depuis laquelle la sélection est effectuée la sélection.
*  N.B.: une _relation_ est bien la formalisation mathématique correcte d’une table = un sous-ensemble d’un produit cartésien.

On peut aussi effectuer des sélection plus fine ou plus complexe, en précisant les champs qui sont à retirer, et des critères des lignes qui sont à prendre en considération:

`SELECT CustomerName, City FROM Customers;`

et pour restreindre la sélection:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

comme par exemple:

```
SELECT CustomerName, City FROM Customers 				WHERE Country=‘Mexico';
```

### Alimenter (« remplir ») une base de données
De la même manière, le langage permet d’insérer de nouveaux éléments dans la base. Une insertion s’effectue en suivant la syntaxe:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...); 
```

**Pour aller plus loin ...** Le sextuples présentés ici sont tirés du site W3C School, qui balaye l’ensemble du langage SQL, avec des exemples et exercices interactif.

### `sqlite` un gestionnaire de base de données minimaliste

Le langage sert donc à interroger une base de données. Mais à quoi ressemble une telle base, et comment donc sont exécuter les expressions écrites en langage SQL ? C’est le rôle d’un gestionnaire de bases de données.

Nombre de gestionnaires sont proposés, tant dans le monde open source que du côté des éditeurs logiciels.

Nous utiliserons le gestionnaire sqlite qui présente l’avantage d’être très léger (comme son nom l’indique). La commande sqlite3, et la librairie du même nom devra être installée déjà dans l’environnement que vous utilisez.

Au lancement de la commande, on peut crée une base de données en fournissant son nom. On peut aussi créer la base depuis un script python:

```
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
con.commit()
res = cur.execute("SELECT * FROM movie")
res.fetchone()
```

Ici, les requêtes à la base de données sont des chaînes de caractères qui sont passées en arguments à des fonctions. On aura avantage à bien paramétrer la construction de ces chaînes de manière à pouvoir varier les requêtes.

**Exercice.** Avant d'envisager de porter les données en base, il faut s'assurer de bien avoir identifier leur nature, les possibles redondances présentes dans les fichiers, les données manquantes, etc.

Pour les données de santé:

* Les trois champs `patho_niv1`, `patho_niv2`, `patho_niv3` sont-ils toujorus renseignés et différents ?
* Comment traiter l'attribut `libelle_classe_age` ?
* Les chiffres associées à l'attribut `libelle_sexe` est-il obtenu en agrégeant les valeurs des lignes correspondantes `femmes` et `hommes` ?
* Etc.

Pour les données sur les emplois:

* Comment réconcilier les libellés des attributs entre les différents fichiers ?
* Comment traiter le fait que les données sont éclatées sur plusieurs fichiers ?
* Comment traiter les données manquantes ?


**Exercice.** On suppose ici avoir arrêté le schéma de la base de données qui stockera les données de santé / emplois. Ecrivez un script insère en base les données.

Il vous faudra vous intéresser aux types possibles des champs stockés en base (chaînes de caractères, valeurs numériques, date, etc.).

### Jointures
Puisque le passage en forme(s) normale(s) amène à "éclater" les donnée sur plusieurs relations (tables), les requêtes sur les données vont exiger de "rassembler" en une même relation (table) des données se trouvant dans des relations distinctes. Cette opération est appelée une _jointure_. Elle consiste à faire correspondre des éléments de deux tables différentes à partir d'un atttribut qu'elle partage. Plusieurs cas peuvent se présenter:

