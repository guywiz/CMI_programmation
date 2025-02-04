import pandas as pd
from datetime import datetime
import plotly.express as px

# lecture des donnees et chargement dans un df

df_TEL = pd.read_csv('../data/appels_tel.csv', sep=';')

def hms_to_sec(hms):
	h, m, s = map(lambda v: int(v), hms.split(':'))
	return 3600*int(h) + 60*int(m) + int(s)

def to_h_m_s(nb_seconds):
	seconds_left = nb_seconds
	nb_hours = int(seconds_left // 3600)
	seconds_left = seconds_left % 3600
	nb_minutes = int(seconds_left // 60)
	seconds_left = seconds_left % 60
	return str(f'{nb_hours}:{nb_minutes}:{seconds_left}')

# ajout d'une colonne duree en secondes de l'appel

df_TEL['Duration_sec'] = df_TEL['Duration'].apply(hms_to_sec)

# duree moyenne, max, min, std
df_TEL['Duration_sec'].mean()
df_TEL['Duration_sec'].max()
df_TEL['Duration_sec'].min()
df_TEL['Duration_sec'].std()


def to_datetime(date_hms_tuple):
	date = date_hms_tuple['Date']
	hms = date_hms_tuple['Heure']
	# day month year separated by slashes
	# hour minute seconds separated by colon
	datetime_str = f'{str(date)} {str(hms)}' #'09/19/22 13:55:26'
	return datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')

# ajout d'une colonne datetime conjuguant date et heure de l'appel

df_TEL['Datetime'] = df_TEL[['Date', 'Heure']].apply(to_datetime, axis=1)

def to_weekday(date):
	return date.strftime('%A')

df_TEL['Weekday'] = df_TEL['Datetime'].apply(to_weekday)

###

# duree totale des appels inities par l'utilisateur (Calling_Number) 4RU64I8I242
# on utilise un masque booleen
# df_bool = df_TEL['Calling_Number'] == '4RU64I8I242'
# print('MASQUE BOOLEEN', df_bool)

duree_totale_4RU64I8I242 = df_TEL[df_TEL['Calling_Number'] == '4RU64I8I242']['Duration_sec'].sum()
print(f"Duree totale des appels inities par l'utilisateur (Calling_Number) 4RU64I8I242: {to_h_m_s(duree_totale_4RU64I8I242)}")

# nombre d'appels d'une durée de plus d'un quart d'heure
df_TEL[df_TEL['Duration_sec'] > 900].shape[0]

# regroupement (groupby) et temps moyen des appels selon les jours de la semaine
df_TEL.groupby(['Weekday'])['Duration_sec'].mean()

# temps d'appel moyen par jour de la semaine pour le numero de telephone 4RU64I8I242

df_TEL[df_TEL['Calling_Number'] == '4RU64I8I242'].groupby(['Weekday'])['Duration_sec'].mean()

# Avec qui l'utilisateur `4RU64I8I242` a-t-il passer le plus de temps au telephone (duree totale des appels) ?

df_TEL[df_TEL['Calling_Number'] == '4RU64I8I242'].groupby(['Called_Number'])['Duration_sec'].sum().reset_index(name ='Moyenne_appels').sort_values(by='Moyenne_appels', ascending=False)

### visualisations avec plotly

# visualisation des temps moyen des appels selon les jours de la semaine

df_fig = df_TEL.groupby(['Weekday'])['Duration_sec'].mean().reset_index(name ='Moyenne_appels_jour')
fig = px.bar(df_fig, x="Weekday", y="Moyenne_appels_jour") #, color="smoker", barmode="group")
fig.show()

# et si on veut ordonner les jours de la semaine

fig = px.bar(df_fig, x="Weekday", y="Moyenne_appels_jour", category_orders=dict(Weekday=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]))
fig.show()

# histogramme des durees des appels
fig = px.histogram(df_TEL, x="Duration_sec", nbins=200, log_y=True)
fig.show()

# histogramme des durees des appels en distinguant appels entrants ou sortants

def in_or_outgoing(call_type):
	if 'Incoming' in call_type:
		return 'Incoming'
	if 'Outgoing' in call_type:
		return 'Outgoing'
	return 'Neither'

df_TEL['In_Out'] = df_TEL['Type'].apply(in_or_outgoing)
ddf = df_TEL[df_TEL['In_Out'] != 'Neither']
fig = px.histogram(ddf, x="Duration_sec", nbins=200, log_y=True, color='In_Out')
fig.show()
