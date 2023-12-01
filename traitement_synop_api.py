#%%
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import requests


# %%
# lecture du dataframe

url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?refine=nom_reg%3A%22Occitanie%22&refine=date%3A%222023%22"

response = requests.get(url)

if response.status_code == 200:
    df_synop = response.json()
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")


#%%
results = df_synop.get('results', [])
df_synop = pd.DataFrame(results)

#%%
df_synop = df_synop.drop(["t","td","tminsol","nom_reg", "code_reg", "mois_de_l_annee", "code_epci", "ht_neige", "coordonnees","temps_present","type_de_tendance_barometrique"],axis=1)
df_synop["date"] = df_synop["date"].apply(
            lambda _: datetime.fromisoformat(_)
        )
#%%
df_synop = df_synop[df_synop.date > '2022-09']

#%%
df_synop = df_synop.loc[:, df_synop.isnull().sum()/len(df_synop.index) <0.3] 

#%%
df_synop['date'] = df_synop['date'].apply(lambda x: x.replace(tzinfo=None))

#%%
montpeul = df_synop[df_synop['nom']=='MONTPELLIER']
montpeul = montpeul.set_index(["date"])


# %%
plt.plot(montpeul['pres'].resample("d").mean())
plt.show()
# %%
