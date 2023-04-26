# Epreuve individuelle
Epreuve individuelle du 26/04/2023

## Création d'une base de données

On dispose d'un unique fichier ([`netflix.csv`](./netflix_titles.csv), les champs sont séparés par des '`;`') décrivant les émissions ou films disponibles sur une plateforme. Le fichier contient sur chaque ligne les informations sur une émission ou un film

* son titre, son type, son réalisateur (`director`),
* la liste des acteurs qui y jouent (`cast`),
* les pays où le film a été produit,
* la date à laquelle l'émission ou le film a été ajouté au portail (`date_added`), l'année de sa diffusion (`release_year `),
* les catégories auxquelles il appartient (`listed_in`), sa durée,
* ainsi qu'une courte description.

A noter que:

* Dans cette liste deux films n'ont jamais le même titre.
* Un réalisateur (`director`) peut aussi jouer dans le film (et donc apparaître dans le champ `cast`).

--

Ce fichier `csv` correspond en quelque sorte à une base de données réduite à _une seule relation_ (table).

* Cette relation satisfait-elle la première forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
    * Non. Cela tient à ce que certains champs (colonnes) contiennent plusieurs valeurs.
    * C'est le cas par exmple du champ `cast` qui contient une liste de noms.
    * C'est le cas aussi des catégories auxquelles appartiennent les films ou émissions (champ `listed_in`).
* Cette relation satisfait-elle la seconde forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
    * Non. Cela tient au fait qu'une même ligne décrit plusieurs entités (qui sont liées): film ou émission, et comédiens.
* Proposez, pour ces données, un schéma satifaisant les première et seconde formes normales.
    * Il nous faut éclater l'ensemble des données sur deux entités: film ou émission, et personnes (acteurs ou réalisateurs):
    * `person(name)` avec `name` (qui est le seul attribut dont on dispose pour décrire une personne) qui est une clé primaire
    * `movie(id, title, type, date_added, release_year, rating, duration, description)` avec `id` qui sera une clé primaire auto-incrémentée (un peu à l'image de la colonne `show_id`)
    * `country(name)` avec `name` (qui est le seul attribut dont on dispose pour décrire un pays) qui est une clé primaire
    * `category(name)` avec `name` (qui est le seul attribut dont on dispose pour décrire une catégorie) qui est une clé primaire

* A ces entités, il faut ajouter des tables les associant:
    * Une association `N:N` entre acteur et film ou émission: `appears_in(movie_id, person, role)` où l'attribut `role` précisera si la personne apparait comme acteur ou réalisateur; les clés movie_id et name sont alors des clés étrangères respectivement empruntées aux tables `movie` et `person`.
    * Une association `N:N` entre films ou émissions et catégories `show_types(movie_id, category_name)`; les clés `movie_id` et `category_name` sont alors des clés étrangères respectivement empruntées aux tables `movie` et `category`.
    * Une association `N:N` entre films ou émissions et pays (de production) `produced_in(movie_id, country_name)`; les clés `movie_id` et `country_name` sont alors des clés étrangères respectivement empruntées aux tables `movie` et `country`.

--

* Proposez une requête qui calcule le nombre d'émissions de télé produites (`release_year`) avant 2010.
    * `SELECT COUNT(id) FROM movie WHERE type='TV Show' and release_year < 2010`
* Proposez une requête qui calcule le nombre d'émissions ou de films dans lesquels une personne apparaît comme réalisateur.
    * `SELECT COUNT(movie_id) FROM appears_in WHERE person_name=` _nom_ `AND role='director'`
* Proposez une requête qui calcule le nombre d'émissions (`TV Show`) dans lesquels une personne apparaît comme réalisateur.
    * `SELECT COUNT(AI.movie_id) FROM appears_in as AI, movie as M WHERE M.id = AI.movie_id AND AI.person_name=` _nom_ `AND AI.role='director' AND M.type='TV Show'`
* Proposez une requête qui calcule le nombre de "Thrillers" dans lesquels apparait une personne dont on précise le nom.
    * `SELECT COUNT(AI.movie_id) FROM appears_in as AI, show_types as ST WHERE AI.person_name=` _nom_ `AND AI.role='director' AND AI.movie_id=ST.movie_id AND ST.category_name='Thrillers'`
* Proposez une requête qui donne les noms des personnes ayant joué dans un film dont ils sont aussi réalisateurs.
    * `SELECT DISTINCT(AI1.person_name) FROM appears_in as AI1, appears_in as AI2 WHERE AI1.person_name=AI2.person_name AND AI1.role='director' AND AI2.role='actor'`
