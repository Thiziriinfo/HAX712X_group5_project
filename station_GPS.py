# %%
import pandas as pd

# %%
# lecture du dateframe
df = pd.read_csv("./data/donnees_atmo.csv")

# %%
# nettoyage df
df = df.drop(['id', 'insee_com',  'code_station',
       'typologie', 'influence', 'nom_polluant', 'id_poll_ue', 'valeur',
       'unite', 'metrique', 'date_debut', 'date_fin', 'statut_valid', 'x_l93',
       'y_l93', 'geom'], axis=1)

# %%
#station double
df["nom_station"] = df["nom_station"].replace(['Montpelier Pere Louis Trafic'], 'Montpelier Antigone Trafic')

# %%
#on récupère les valeurs uniques
df = df.drop_duplicates()

# %%
#tri
df = df.sort_values(by = ['nom_dept', 'nom_com', 'nom_station'])

# %%
df.reset_index(inplace=True,drop=True)

# %%
df.to_csv('localisation.csv')
