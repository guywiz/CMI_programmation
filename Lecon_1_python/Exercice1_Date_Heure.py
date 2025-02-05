import csv

def no_value(row, fields):
	return sum([row[field] == '' for field in fields]) > 1

tested_fields = ['Date', 'Heure']

with open('../data/appels_tel.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	nb_lignes_defectueuses = sum([no_value(row, tested_fields) for row in reader])

print(f"Le fichier comporte {nb_lignes_defectueuses} lignes dont les champs {', '.join(tested_fields)} sont vides")

