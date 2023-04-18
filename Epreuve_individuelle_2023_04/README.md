# Epreuve individuelle (exemple)
A titre d'exemple pour préparer l'épreuve du 26/04/2023

## Création d'une base de données

On dispose d'un unique fichier ([`clothes_sales.csv`](./clothes_sales.csv), les champs sont séparés par des '`;`') décrivant les commandes effectuées par des clients auprès d'un fournisseur de vêtements. Le fichier contient sur chaque ligne une information d'une commande (`order`), décrivant le produit (`product`) commandé, et le client (`customer`) l'ayant commandé.

Ce fichier `csv` correspond en quelque sorte à une base de données réduite à _une seule relation_ (table).

* Cette relation satisfait-elle la première forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
* Cette relation satisfait-elle la seconde forme normale ? Si oui pourquoi, sinon donnez un exemple mettant en faute cette forme normale.
* Proposez, pour ces données, un schéma satifaisant les première et seconde formale normale.

--

* Proposez une requête qui calcule le nombre de commandes d'un client donné, dont on précise le nom (champ `customer`).
* Proposez une requête qui calcule le nombre de produits commandés par un client donné (parmi toutes les commandes qu'il a passé) , dont on précise le nom (champ `customer`).
* Proposez un script qui calcule le montant total d'une commande (à partir de son numéro).

--

* Proposez un script qui construit la base correspondant à ce schéma.
* Proposez un script qui alimente la base de données à partir du fichier.
