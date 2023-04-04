import pandas as pd
import sqlite3

database_name = './model/pathologies.sql'

def get_pathologies():
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    query = f"SELECT DISTINCT patho_niv2 FROM pathologies WHERE patho_niv1='Cancers';"
    res = cur.execute(query)
    all = res.fetchall()
    db.close()
    return sorted(map(lambda x: x[0], all))

def extract_patho_data(patho_name):
    # find top code for pathologie
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    query = f"SELECT top FROM pathologies WHERE patho_niv2='{patho_name}';"
    res = cur.execute(query)
    all = tuple(map(lambda x: x[0], res.fetchall()))

    query = f"SELECT SUM(ntop) AS hospitalisation, SUM(npop) AS population, annee FROM 'population' WHERE pathologie IN {all} GROUP BY annee;"
    print('QUERY:', query)
    df = pd.read_sql(query, db)
    attributes = ['annee', 'population']
    return df, attributes
