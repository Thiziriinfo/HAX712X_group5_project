#%%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#%%
#lecture du dateframe
df = pd.read_csv("./data/mesure_horaire_view.csv")

# %%
#selection d'une ville et d'un polluant
df_1 = df.loc[df['nom_com'] == 'TOULOUSE', : ]
df_1 = df_1.loc[df_1['nom_polluant'] == 'NOX', : ]

#%%
#creation de la liste des heures
n = 24 #nombres d'heures
dates = df_1['date_debut'][1 : n].to_list()
formatting = "%Y-%m-%d %H:%M:%S"
x = [datetime.strptime(date , formatting) for date in dates]
#%%
#reation de la liste des valeurs
y = df_1['valeur'][1 : n].to_list()

#%%
#graphique valeur = f(temps)
plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Valeur')
plt.title("Valeur du NOX à Toulouse sur " + str(n) + " heures")
plt.grid(True)
plt.gcf().set_size_inches(9, 7)
plt.xticks(rotation=45)
plt.show()



# %%


# %%
