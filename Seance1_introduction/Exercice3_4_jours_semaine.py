import csv
from datetime import datetime

compil_jours_semaine = {x: 0 for x in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

def to_weekday(date_str):
	return datetime.strptime(date_str, '%d/%m/%Y').strftime('%A')

with open('../data/appels_tel.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		date = row['Date']
		day = to_weekday(date)
		compil_jours_semaine[day] += 1

print("Nombre d'appels selon les jours de la semaine:")
print(compil_jours_semaine)

###

fin_matinee = datetime.strptime('12:00:00', '%H:%M:%S')
fin_journee = datetime.strptime('18:00:00', '%H:%M:%S')

compil_appels_journees = {x: 0 for x in ['matinee', 'journee', 'soiree']}

def to_when(date_str):
	global matinee, journee, minuit
	when = datetime.strptime(date_str, '%H:%M:%S')
	if when < fin_matinee:
		return 'matinee'
	elif when < fin_journee:
		return 'journee'
	else:
		return 'soiree'

with open('../data/appels_tel.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	for row in reader:
		heure = row['Heure']
		compil_appels_journees[to_when(heure)] += 1

print("Nombre d'appels selon les moments de la journee:")
print(compil_appels_journees)
