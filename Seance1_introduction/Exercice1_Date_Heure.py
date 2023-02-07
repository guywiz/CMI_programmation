import csv

def no_value(row, field):
	return row[field] == ''

with open('../data/appels_tel.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	nb_lignes_defectueuses = 0
	for row in reader:
		if no_value(row, 'Duration'): # no_value(row, 'Date') or no_value(row, 'Heure'):
			nb_lignes_defectueuses += 1

print(f'Le fichier comporte {nb_lignes_defectueuses} lignes dont les champs Date ou heure sont vides')
