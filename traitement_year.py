# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# %%
# lecture du dataframe
df_atmo = pd.read_csv("./data/donnees_atmo.csv")

# %%
# nettoyage df_atmo
df_atmo = df_atmo.drop(["date_fin", "statut_valid", "x_l93", "y_l93", "geom", "metrique", "id", ], axis=1)

# %%
# liste des villes et des polluants
villes = df_atmo["nom_com"].unique().tolist()
villes.sort()
polluants = df_atmo["nom_polluant"].unique().tolist()
polluants.sort()


# %%
# fonction qui fait la sélection ville et polluant
def selection(ville, polluant):
    if ville == 'MONTPELLIER':
        df_atmo["nom_station"] = df_atmo["nom_station"].replace(['Montpelier Pere Louis Trafic'], 'Montpelier Antigone Trafic')
    df_atmo_1 = df_atmo.loc[(df_atmo["nom_com"] == ville) & (df_atmo["nom_polluant"] == polluant), :]
    return df_atmo_1



# %%
# Fonction qui trace le graphique
def graphique(ville, polluant, debut, fin):
    df_atmo_pv = selection(ville, polluant)
    nom_stations = df_atmo_pv["nom_station"].unique()
    nb_stations = len(nom_stations)
    fig, axes = plt.subplots(nb_stations, 1, figsize=(10, 15), sharex=True)
    fig.suptitle("Pollution au " + str(polluant) +
                 " à " + str(ville) + " du " + str(debut) + " au " + str(fin), fontsize=16)

    for i in range(nb_stations):
        df_atmo_pvs = df_atmo_pv.loc[df_atmo_pv["nom_station"] == nom_stations[i]]
        df_atmo_pvs["date_debut"] = df_atmo_pvs["date_debut"].apply(
            lambda _: datetime.strptime(_, "%Y-%m-%d %H:%M:%S")
        )
        df_atmo_pvs = df_atmo_pvs.set_index(["date_debut"])
        df_atmo_pvs = df_atmo_pvs.loc[debut:fin]
        axes[i].plot(df_atmo_pvs["valeur"].resample("d").mean())
        for label in axes[i].get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)
        axes[i].set_ylabel("Concentration en µg/m3")
        axes[i].set_title(
            "Concentration du " + str(polluant) + " au " + str(nom_stations[i])
        )
        axes[i].grid(True)

    plt.show()



# %%
