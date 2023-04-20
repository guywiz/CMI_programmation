# Epreuve individuelle (exemple)
A titre d'exemple pour préparer l'épreuve du 26/04/2023

## Création d'une base de données

On dispose d'un unique fichier ([`clothes_sales.csv`](./clothes_sales.csv), les champs sont séparés par des '`;`') décrivant les commandes effectuées par des clients auprès d'un fournisseur de vêtements. Le fichier contient sur chaque ligne une information d'une commande (`order`), décrivant le produit (`product`) commandé, et le client (`customer`) l'ayant commandé.

Ce fichier `csv` correspond en quelque sorte à une base de données réduite à _une seule relation_ (table).

* Cette relation satisfait-elle la première forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
    * La première forme normale exige que chaque attribut (colonne) contiennent une information "atomique", une seule information. C'est-à-dire qu'ils ne contiennent pas une combinaison de plusieurs informations que l'on pourrait stocker séparément dans des attributs.
    * C'est le cas ici pour les adresses des clients (`customer`) qui agrègent numéro de bâtiment et rue, ville code postal et pays en un seul champ.
    * C'est aussi le cas des informations personnelles des clients (age et genre, champ `gender and age `).
    * La première forme normale n'est donc pas satisfaite.

* Cette relation satisfait-elle la seconde forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
    * La seconde forme normale exige que l'on puisse définir une clé primaire de manière à ce que les valeurs des attributs d'une entrée (ligne) soient déterminées par la valeur de cette clé.
    * En d'autres mots, les attributs sont ceux qui décrivent une seule entité.
    * La seconde forme normale n'est pas satisfaite ici puisque sur une même ligne on trouve des informations décrivant le client (`customer`), et le produit (`product_name`) acheté par le client, et la commande (`order_id`) à laquelle est rattachée cet achat.

* Proposez, pour ces données, un schéma satifaisant les première et seconde formes normales.
    * Il nous faut éclater l'ensemble des données sur trois entités: `customer`, `product`, `order`
    * `customer(name, gender, age, no/street, city, postal_code, country)` clé primaire `name`
    * `product(product_id, product_name, product_type, size, colour, unit_price, description)`clé primaire `product_id` (qu'il faut générer puisque nous n'avons pas d'identifiant pour les produits)
    * `order(id, date, customer)` clé primaire `id`, clé étrangère `customer`
    * qui doit être complétée par une relation d'association qui associe commande, produit et client:
    * `order_list(order_id, product_id, quantity)` clés étrangères `order_id` et `product_id`

--

* Proposez une requête qui calcule le nombre de commandes d'un client donné, dont on précise le nom (champ `customer`).
* Proposez une requête qui calcule le nombre de produits commandés par un client donné (parmi toutes les commandes qu'il a passé) , dont on précise le nom (champ `customer`).
* Proposez un script qui calcule le montant total d'une commande (à partir de son numéro).
* ...

--

* Proposez un script qui construit la base correspondant à ce schéma.
* Proposez un script qui alimente la base de données à partir du fichier.
