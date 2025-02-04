import re

# un dictionnaire qui comptabilise les frequences
alphabet = {} #{chr(x): 0 for x in int_minuscules + int_majuscules + int_accentuees}

# un autre dict pour comptabiliser les frequences de lettres dans le dico
freq = {} #{chr(x): 0 for x in int_minuscules + int_majuscules + int_accentuees}

with open('../data/vocabulaire_francais.csv', 'r') as fp:
	line = fp.readline()
	while line != '':
		mot = line.strip()
		try:
			alphabet[mot[0]] +=1
		except KeyError:
			alphabet[mot[0]] =1
		for x in mot:
			try:
				freq[x] += 1
			except KeyError:
				freq[x] = 1
		line = fp.readline()

print("Frequences des premieres lettres des mots")
print(alphabet)
print(freq)

###

nb_tt = 0
nb_ge = 0

with open('../data/vocabulaire_francais.csv', 'r') as fp:
	line = fp.readline()
	while line != '':
		if 'tt' in line:
			nb_tt += 1
		mot = line.strip()
		if mot[-2:] == 'ge':
			nb_ge += 1
		line = fp.readline()

print(f"Nombre de mots contenant la double consonne tt: {nb_tt}")
print(f"Nombre de mots se terminant par 'ge': {nb_ge}")

# deux fois la lettre z
# requiere l'utilisation d'expressions regulieres

pattern_string = '.*z.*z.*'
pattern = re.compile(pattern_string)
ens_mots = set()

with open('../data/vocabulaire_francais.csv', 'r') as fp:
	line = fp.readline()
	while line != '':
		result = re.match(pattern, line)
		if result:
			ens_mots.add(line.strip())
		line = fp.readline()

print(f"Nombre de mots contenant deux fois la lettre z: {len(ens_mots)}")
print(ens_mots)
