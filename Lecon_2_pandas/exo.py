import pandas as pd
import os
import plotly.express as px
import argparse

# une fonction qui charge les donnees (appels tel) et renvoie un dataframe
# la fonction doit comporter un paramètre (booléen) indiquant si les lignes
# comportant des données manquantes doivent être écartées (valeur par défaut True)

def load_data(filepath, sep=";", discard_incomplete_data=True):
    if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    df = pd.read_csv(filepath, sep=sep)
    print(f'{df.head()}')
    if discard_incomplete_data:
            df = df.dropna(subset=["Forward_Number", "End Time"])
    return df

# une fonction qui filtre les données pour ne retenir que les appels passés
# entre une date de debut et une date de fin dont les valeurs par défaut sont None
# la fonction ne modifie pas le dataframe recu en entree mais en retourne un nouveau

def filter_data(input_df, start_date=None, end_date=None, date_col="Date", time_col="Heure"):
    df_filtered = input_df.copy()
    
    # cree une colonne Start time a partir de date et heure
    df_filtered["Start Time"] = pd.to_datetime(df_filtered[date_col] + " " + df_filtered[time_col], format="%d/%m/%Y %H:%M:%S")
    df_filtered["End Time"] = pd.to_datetime(df_filtered["End Time"])
    
    if start_date is not None:
        start_date = pd.to_datetime(start_date)  # convertit start_date en datetime
        df_filtered = df_filtered[df_filtered["Start Time"] >= start_date]
    
    if end_date is not None:
        end_date = pd.to_datetime(end_date)  # convertit end_date en datetime
        df_filtered = df_filtered[df_filtered["Start Time"] <= end_date]
    
    # supprime la colonne "Start time" temporaire si elle n'existait pas dans l'original
    if "Start time" not in df.columns:
        df_filtered = df_filtered.drop(columns=["Start Time"])
    
    return df_filtered

# une fonction qui agrege les donnees (duree des conversations) selon differents criteres
# appels passes le matin, en apres-midi, en soiree
# appels agrege par jour, par semaine

def aggregate_data(df, coarsity=None, date_col="Date", time_col="Heure"):
    df = df.copy()
    df["Start Time"] = pd.to_datetime(df[date_col] + " " + df[time_col], format="%d/%m/%Y %H:%M:%S")
    
    if coarsity is None:
        df['time_period'] = df['Start Time'].dt.hour.map(lambda h: 'Morning' if h < 12 else ('Afternoon' if h < 17 else 'Evening'))
        grouped = df.groupby(['Calling_Number', 'time_period']).size()
    
    elif coarsity == "day":
        df['day_of_week'] = df['Start Time'].dt.day_name()
        grouped = df.groupby(['Calling_Number', 'day_of_week']).size()
    
    elif coarsity == "week":
        df['week_start'] = df['Start Time'].dt.to_period('W').apply(lambda r: r.start_time.date())
        grouped = df.groupby(['Calling_Number', 'week_start']).size()
    
    else:
        raise ValueError("Invalid coarsity parameter. Use None, 'day', or 'week'.")
    
    return grouped.reset_index(name='call_count')

def compute_avg_weekly_calls(df):
    # Convert date and time columns to datetime
    df['start_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Heure'], format='%d/%m/%Y %H:%M:%S')
    df['end_datetime'] = pd.to_datetime(df['End Time'], format='%d.%m.%Y %H:%M:%S')
    
    # Determine the week start for each call
    df['week_start'] = df['start_datetime'].dt.to_period('W').apply(lambda r: r.start_time.date())
    
    # Count the number of calls per caller and per week
    weekly_calls = df.groupby(['Calling_Number', 'week_start']).size().reset_index(name='weekly_call_count')
    
    # Compute the average weekly call count per caller
    avg_weekly_calls = weekly_calls.groupby('Calling_Number')['weekly_call_count'].mean().reset_index(name='avg_weekly_call_count')
    
    return avg_weekly_calls

# des fonctions qui permettent de visualiser les données selon differents criteres
def violin_plot(df, y_axis, plot_title):    
    fig = px.violin(df, y=y_axis, box=True, points="all", title=plot_title)
    fig.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument("-f", "--file", required=True, help="Path to the file")
    
    args = parser.parse_args()
    print(f"Filename provided: {args.file}")

    print('Launching script')
    # traitement des arguments

    print('Loading data')
    df = load_data(args.file)
    print('Filtering data')
    filtered_df = filter_data(df)
    ave_weekly_count = compute_avg_weekly_calls(filtered_df)
    print(ave_weekly_count.head())
    violin_plot(ave_weekly_count, y_axis="avg_weekly_call_count", plot_title="Distribution du nombre moyen d'appels par semaine et par appelant")
    