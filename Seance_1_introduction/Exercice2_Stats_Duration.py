import csv

def to_seconds(h_m_s):
	nb_hours = int(h_m_s[0:2])
	nb_minutes = int(h_m_s[3:5])
	nb_seconds = int(h_m_s[6:])
	return nb_hours*3600 + nb_minutes*60 + nb_seconds

def to_h_m_s(nb_seconds):
	seconds_left = nb_seconds
	nb_hours = int(seconds_left // 3600)
	seconds_left = seconds_left % 3600
	nb_minutes = int(seconds_left // 60)
	seconds_left = seconds_left % 60
	return str(f'{nb_hours}:{nb_minutes}:{nb_seconds}')


with open('../data/appels_tel.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	min = float('inf') # infinity
	max = -1 # duration is always positive
	moyenne = 0.0
	nb_lignes = 0
	for row in reader:
		value = to_seconds(row['Duration'])
		nb_lignes += 1
		moyenne += float(value)
		if min > value:
			min = value
		if max < value:
			max = value
	moyenne /= nb_lignes

print(f'Durée moyenne des conversations: {to_h_m_s(moyenne)}')
print(f'Durée max des conversations: {to_h_m_s(max)}')
print(f'Durée min des conversations: {to_h_m_s(min)}')
