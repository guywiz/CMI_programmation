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
