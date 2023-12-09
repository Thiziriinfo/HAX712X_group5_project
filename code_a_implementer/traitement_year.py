# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# %%
# lecture du dataframe
df_atmo = pd.read_csv("/home/guillaume/project_2023_2024/HAX712X_group5_project/data/donnees_atmo.csv")

#%%
def selection(ville, polluant):
    if ville == "MONTPELLIER":
        df_atmo["nom_station"] = df_atmo["nom_station"].replace(
            ["Montpelier Pere Louis Trafic"], "Montpelier Antigone Trafic"
        )
    df_1 = df_atmo.loc[
        (df_atmo["nom_com"] == ville) & (df_atmo["nom_polluant"] == polluant), :
    ]
    return df_1


# %%
# Fonction qui trace le graphique
def graphique(ville, polluant):
    # sélection : pas utile
    df_pv = selection(ville, polluant)
    # les différentes stations
    nom_stations = df_pv["nom_station"].unique()
    nb_stations = len(nom_stations)
    # plusieurs graphiques
    if nb_stations == 1:
        fig, axes = plt.subplots(1, 1, figsize=(10, 5), layout="constrained")  # Créer une seule sous-figure
        axes = [axes]  # Mettre l'unique axe dans une liste
    else:
        fig, axes = plt.subplots(nb_stations, 1, figsize=(10, 15), sharex=True, layout="constrained")
    # titre général
    fig.suptitle("Pollution au " + str(polluant) + " à " + str(ville), fontsize=16)

    for i in range(nb_stations):
        # on garde seulement les données de la station i
        df_pvs = df_pv.loc[df_pv["nom_station"] == nom_stations[i]]
        # transformation en datetime de date_debut
        df_pvs["date_debut"] = df_pvs["date_debut"].apply(
            lambda _: datetime.strptime(_, "%Y-%m-%d %H:%M:%S")
        )
        # datetime devient index
        df_pvs = df_pvs.set_index(["date_debut"])
        # on moyennise par jour
        axes[i].plot(df_pvs["valeur"].resample("d").mean())
        # labellisations et titre
        for label in axes[i].get_xticklabels():
            label.set_ha("right")
            label.set_rotation(45)
        axes[i].set_ylabel("Concentration en µg/m3")
        axes[i].set_title(
            "Concentration du " + str(polluant) + " à " + str(nom_stations[i])
        )
        axes[i].grid(True)
        
    plt.savefig("year.svg", dpi=300, transparent=True)
    plt.show()


# %%
