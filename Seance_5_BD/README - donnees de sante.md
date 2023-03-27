# CMI_programmation

## Construction d'une base sur les données de santé

L'analyse des données de santé nous amène à y voir trois types d'entités:

* Les données décrivant les pathologies (leur dénomination et une entrée qui est son code `top`, vraisemblablement emprunté à une nomencalture nationale).
* Les données sur la population, c'est-à-dire le nombre de personnes affectés d'une pathologie donnée, et parmi celles-ci le nombre qui ont dû être hospitalisées (en lien avec cette pathologie) l'année `YYYY`.
    * Ces données sont aussi géolocalisées, ces nombres sont donnés par département, chaque département étant dans une des grandes régions administratives.

On crée donc un schéma qui reprend ces entités, et les associations entre elles.

* L'entité localisation géographique, décrite par le nom de département (et la région à laquelle il appartient). Le nom de département est une clé primaire naturelle de cette entité (ou son numéro).
* L'entité pathologie décrite par les trois chaps patho_niv1, 2 et 3, et le "nom de code" top. (Il faudrait préalablement vérifier que ce code `top` est en effetunique pour chaque pathologie.) Cela en fait donc la clé primaire pour cette entité.
* Les données sur la population qui indique la taille de la population, dans un départemnt donné et une année particulière (entre 2015 et 2020), qui souffre de cette pathologie (`npop`) et le nombre parmi celle-ci qui a subi une hospitatlisation (`ntop`).

A noter certains attributs dont le sens est difficle à cerner pour les non-spécialistes (`prev`, `niveau_prioritaire`), mais que nous pourrons tout de même intégrer à la base.

Ainsi, le schéma de la base se résuime en trois entités:

`geographie (_dept_ text PRIMARY KEY, region text)`

```
pathologies (
		_top_ text PRIMARY KEY,
		patho_niv1 text,
		patho_niv2 text,
		patho_niv3 text,
		niveau_prioritaire text
```

```
population (
		pathologie text,
		dept int,
		annee int,
		age_inf int,
		age_sup int,
		sexe int,
		ntop int,
		npop int,
		prev real,
		FOREIGN KEY (pathologie) REFERENCES pathologies (top),
		FOREIGN KEY (dept) REFERENCES geographie (dept)
	)
```

## Alimenter la base

Reste maintenant à faire passer les données des différents fichiers dans la base. On peut donc lire les fichiers ligne à ligne et extraire sur chaque ligne les informaitons renseignant les entités qui sont en jeu, et les liens entre elles.

* A noter qu'une même pathologie sera lue autant de fois qu'elle apparait sur une ligne du fichier.
* Même chose pour les départements.
* Que certaines données ne sont pas toujours renseignées (mais le schéma de la base l'a prévu en n'exigeant pas que tous les attributs soient renseignés).

Ainsi, chaque ligne donnera lieu d'abord à la création d'une pathologie et d'un département. Lorsque ceux-ci existe déjà, il faut ignorer la ligne. A  noter qu'en raison de l'unicité des clés primaires, une tentiative d'insertion d'une entité avec une clé primaire existante provoque une erreur `sqlite3.IntegrityError` qui peut être intercepté.

On définit donc des fonctions pour chacun des types d'entités, puis un script qui est chargé de lire le fichier et d'appeler les fonctions. Les erreurs `sqlite3.IntegrityError` sont traitées au niveau du script.

Comme vous pourrez le constater (en faisant tourner le script), les départements sont très vite renseignés, alors que le nombre de pathologies croit plus lentememnt jusqu'à atteindre un total de 78 (de niveau 3, bien moins que les quelques 3 millions de lignes du fichier !).

P.S. Attention, le traitement est très long (ne le faites que pour une partie des données si vous expérimentez le script), il vaut mieux traiter les données une pathologie à la fois pour découper le traitement en plusieurs lots.

```
import sqlite3
import csv

def create_tables(database_name):
	db = sqlite3.connect(database_name)
	cur = db.cursor()

	# on suppose que si cette fonction est appelee
	# c'est que l'on souhaite reprendre la construciton de la base
	# donc on suppprime les tables existantes et on les reconstruit
	cur.execute("DROP TABLE IF EXISTS pathologies")
	cur.execute('''
	CREATE TABLE pathologies (
		top text PRIMARY KEY,
		patho_niv1 text,
		patho_niv2 text,
		patho_niv3 text,
		niveau_prioritaire text
	)''')

	cur.execute("DROP TABLE IF EXISTS geographie")
	cur.execute('''
	CREATE TABLE geographie (
		dept text PRIMARY KEY,
		region text
	)''')

	cur.execute("DROP TABLE IF EXISTS population")
	cur.execute('''
	CREATE TABLE population (
		pathologie text,
		dept int,
		annee int,
		age_inf int,
		age_sup int,
		sexe int,
		ntop int,
		npop int,
		prev real,
		FOREIGN KEY (pathologie) REFERENCES pathologies (top),
		FOREIGN KEY (dept) REFERENCES geographie (dept)
	)''')

	db.commit()
	db.close()

def insert_pathologie(database_name, pathologie_infos):
	top = pathologie_infos['top']
	niv1 = pathologie_infos['patho_niv1']
	niv2 = pathologie_infos['patho_niv2']
	niv3 = pathologie_infos['patho_niv3']
	niv_prioritaire = pathologie_infos['niveau_prioritaire']

	query = '''
			INSERT INTO pathologies ('top', 'patho_niv1', 'patho_niv2', 'patho_niv3', 'niveau_prioritaire') \
			VALUES ("{}", "{}", "{}", "{}", "{}")
			'''.format(top, niv1, niv2, niv3, niv_prioritaire)
	db = sqlite3.connect(database_name)
	cur = db.cursor()
	cur.execute(query)
	db.commit()
	db.close()	

def insert_geographie(database_name, geographie_infos):
	dept = geographie_infos['dept']
	region = geographie_infos['region']
	query = '''
			INSERT INTO geographie ('dept', 'region') \
			VALUES ("{}", "{}")
			'''.format(dept, region)
	db = sqlite3.connect(database_name)
	cur = db.cursor()
	cur.execute(query)
	db.commit()
	db.close()	

def insert_comptage(database_name, comptage_infos):
	classe_age = comptage_infos['cla_age_5']
	if classe_age == 'tsage':
		age_inf = 0
		age_sup = 120
	elif classe_age == '95et+':
		age_inf = 95
		age_sup = 120
	else:
		age_inf = int(classe_age.split('-')[0])
		age_sup = int(classe_age.split('-')[1])
	annee = int(comptage_infos['annee'])
	dept = comptage_infos['dept']
	pathologie = comptage_infos['top']
	sexe = int(comptage_infos['sexe'])
	npop = int(comptage_infos['npop'])

	query = '''
			INSERT INTO population (pathologie, dept, annee, age_inf, age_sup, sexe, npop) \
			VALUES ("{}", "{}", {}, {}, {}, {}, {})
			'''.format(pathologie, dept, annee, age_inf, age_sup, sexe, npop)
	db = sqlite3.connect(database_name)
	cur = db.cursor()
	cur.execute(query)
	db.commit()
	try:
		ntop = int(comptage_infos['ntop'])
		prev = float(comptage_infos['prev'])
		query = '''
				UPDATE population SET ntop={}, prev={}
				'''.format(ntop, prev)
		db = sqlite3.connect(database_name)
		cur = db.cursor()
		cur.execute(query)
		db.commit()
	except ValueError:
		pass
	db.close()

if __name__ == '__main__':
	database_name = "pathologies.sql"
	create_tables(database_name)

	print('Inserting Pathologies')
	with(open('Pathologies.csv', 'r')) as csvfile:
		i = 0
		p = 0
		d = 0
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			i += 1
			p += 1
			d += 1
			try:
				insert_pathologie(database_name, row)
			except sqlite3.IntegrityError:
				p -= 1
				pass
			try:
				insert_geographie(database_name, row)
			except sqlite3.IntegrityError:
				d -= 1
				pass
			if i % 50000 == 0:
				print(f'Inserting Pathologies ({i} lines, {p} pathologies)')
				print(f'Inserting Geographie ({i} lines, {d} departements)')

	print('Inserting Population counts')
	with(open('Pathologies.csv', 'r')) as csvfile:
		i = 0
		n = 0
		reader = csv.DictReader(csvfile, delimiter=';')
		for row in reader:
			i += 1
			n += 1
			try:
				insert_comptage(database_name, row)
			except sqlite3.IntegrityError:
				n -= 1
				pass
			if i % 50000 == 0:
				print(f'Inserting Population ({i} lines, {n} population counts)')

```
