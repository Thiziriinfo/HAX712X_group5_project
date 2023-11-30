#%%
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# %%
# lecture du dataframe
with open("./data/donnees-synop.json") as f:
    dict_synop = json.load(f)


# %%
df_synop = pd.DataFrame(dict_synop)

#%%
df_synop = df_synop.drop(["t","td","tminsol","nom_reg", "code_reg", "mois_de_l_annee", "code_epci", "ht_neige", "coordonnees","temps_present","type_de_tendance_barometrique"],axis=1)

#%%
df_synop = df_synop[df_synop.date > '2022-09']

#%%
df_synop = df_synop.loc[:, df_synop.isnull().sum()/len(df_synop.index) <0.3] 

# %%
df_synop["date"] = df_synop["date"].apply(
            lambda _: datetime.fromisoformat(_)
        )

#%%
df_synop['date'] = df_synop['date'].apply(lambda x: x.replace(tzinfo=None))

#%%
montpeul = df_synop[df_synop['nom']=='MONTPELLIER']
montpeul = montpeul.set_index(["date"])


# %%
plt.plot(montpeul['pres'].resample("d").mean())
plt.show()
# %%
