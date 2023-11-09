#%%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#%%
#lecture du dateframe
df = pd.read_csv("./data/mesure_horaire_view.csv")

#%%
#nettoyage df
df = df.drop(['date_fin', 'statut_valid', 'x_l93', 'y_l93', 'geom'], axis=1)

#%%
#liste des villes et des polluants
villes = df["nom_com"].unique().tolist()
polluants = df["nom_polluant"].unique().tolist()

#%%
#fonction qui fait la sélection ville et polluant
def selection(ville , polluant):
    df_1 = df.loc[(df['nom_com'] == ville) & (df['nom_polluant'] == polluant), : ]
    return df_1

#%%
test = selection(villes[3], polluants[2])
test2 = selection('MONTPELLIER','NOX')

#fonction sur qui crée les listes pour le graphique
def liste(df, nb_heure):
    dates = df['date_debut'][1 : nb_heure].to_list()
    formatting = "%Y-%m-%d %H:%M:%S"
    x = [datetime.strptime(date , formatting) for date in dates]
    y = df['valeur'][1 : nb_heure].to_list()
    return x, y


#%%
#Fonction qui trace le graphique
def graphique(ville, polluant, nb_heure):
    df_pv = selection(ville, polluant)
    donnees = liste(df_pv,nb_heure)
    plt.plot(donnees[0], donnees[1])
    plt.xlabel('Date')
    plt.ylabel('Valeur')
    plt.title("Valeur du polluant à la ville sur " + str(nb_heure) + " heures")
    plt.grid(True)
    plt.gcf().set_size_inches(9, 7)
    plt.xticks(rotation=45)
    plt.show()


# %%
