# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# %%
# lecture du dateframe
df = pd.read_csv("./data/mesure_horaire_view.csv")

# %%
# nettoyage df
df = df.drop(["date_fin", "statut_valid", "x_l93", "y_l93", "geom", "metrique"], axis=1)

# %%
# liste des villes et des polluants
villes = df["nom_com"].unique().tolist()
villes.sort()
polluants = df["nom_polluant"].unique().tolist()
polluants.sort()


# %%
# fonction qui fait la sélection ville et polluant
def selection(ville, polluant):
    df_1 = df.loc[(df["nom_com"] == ville) & (df["nom_polluant"] == polluant), :]
    return df_1


# %%
test = selection(villes[3], polluants[0])
test2 = selection("MONTPELLIER", "NOX")


# fonction sur qui crée les listes pour le graphique
def liste(df, nb_heure):
    dates = df["date_debut"][1:nb_heure].to_list()
    formatting = "%Y-%m-%d %H:%M:%S"
    x = [datetime.strptime(date, formatting) for date in dates]
    y = df["valeur"][1:nb_heure].to_list()
    return x, y


# %%
# Fonction qui trace le graphique
def graphique(ville, polluant, nb_heure):
    df_pv = selection(ville, polluant)
    stations = df_pv["code_station"].unique()
    nom_stations = df_pv["nom_station"].unique()
    nb_stations = len(stations)
    fig, axes = plt.subplots(nb_stations, 1, figsize=(10, 15) , sharex=True)
    fig.suptitle('This is a somewhat long figure title', fontsize=16)

    for i in range(nb_stations):
        df_pvs = df_pv.loc[df_pv["code_station"] == stations[i]]
        donnees = liste(df_pvs, nb_heure)
        axes[i].bar(donnees[0], donnees[1])
        axes[i].set_xlabel("Date")
        axes[i].set_ylabel("Concentration en µg/m3")
        axes[i].set_title(
            "Concentration du "
            + str(polluant)
            + " à "
            + str(nom_stations[i])
            + " sur "
            + str(nb_heure)
            + " heures"
        )
        axes[i].grid(True)
        #axes[i].set_size_inches(9, 7)

    plt.show()


# %%
