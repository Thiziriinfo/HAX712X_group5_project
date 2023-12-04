#%%
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import requests


class WeatherData:
    def __init__(self, url):
        self.url = url
        self.df_synop = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            self.df_synop = pd.DataFrame(results)
        else:
            print(f"La requête a échoué avec le code d'état {response.status_code}")

    def preprocess_data(self):
        if self.df_synop is not None:
            
            self.df_synop = self.df_synop.drop(["t", "td", "tminsol", "nom_reg", "code_reg",
                                                "mois_de_l_annee", "code_epci", "ht_neige",
                                                "coordonnees", "temps_present",
                                                "type_de_tendance_barometrique"], axis=1)
            self.df_synop["date"] = self.df_synop["date"].apply(
                lambda _: datetime.fromisoformat(_)
            )
            self.df_synop = self.df_synop[self.df_synop.date > '2022-09']
            self.df_synop = self.df_synop.loc[:, self.df_synop.isnull().sum() / len(self.df_synop.index) < 0.3]
            self.df_synop['date'] = self.df_synop['date'].apply(lambda x: x.replace(tzinfo=None))

    def plot_city_pressure(self, city_name):
        city_data = self.df_synop[self.df_synop['nom'] == city_name]
        city_data = city_data.set_index(["date"])

        plt.plot(city_data['pres'].resample("d").mean())
        plt.title(f"Pressure in {city_name}")
        plt.xlabel("Date")
        plt.ylabel("Pressure")
        plt.show()


# Utilisation de la classe
url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?refine=nom_reg%3A%22Occitanie%22&refine=date%3A%222023%22"
weather_data = WeatherData(url)
weather_data.fetch_data()
weather_data.preprocess_data()
weather_data.plot_city_pressure("MONTPELLIER")



