# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# %%
# lecture du dataframe
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
def graphique(ville, polluant):
    df_pv = selection(ville, polluant)
    nom_stations = df_pv["nom_station"].unique()
    nb_stations = len(nom_stations)
    fig, axes = plt.subplots(nb_stations, 1, figsize=(10, 15), sharex=True)
    fig.suptitle("Pollution au " + str(polluant) + " à " + str(ville), fontsize=16)

    for i in range(nb_stations):
        df_pvs = df_pv.loc[df_pv["nom_station"] == nom_stations[i]]
        df_pvs["date_debut"] = df_pvs["date_debut"].apply(
            lambda _: datetime.strptime(_, "%Y-%m-%d %H:%M:%S")
        )
        df_pvs = df_pvs.set_index(["date_debut"])
        axes[i].plot(df_pvs["valeur"].resample("d").mean())
        axes[i].set_ylabel("Concentration en µg/m3")
        axes[i].set_title(
            "Concentration du " + str(polluant) + " à " + str(nom_stations[i])
        )
        axes[i].grid(True)

    plt.show()


# %%
