# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import requests


class AirQualityData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            return response.json().get('features', [])
        else:
            print(f"La requête a échoué avec le code d'état {response.status_code}")
            return []

    def create_dataframe(self):
        records_data = [record['attributes'] for record in self.data]
        df_atmo = pd.DataFrame(records_data)

        df_atmo["date_debut"] = df_atmo["date_debut"] / 1000
        df_atmo["date_debut"] = df_atmo["date_debut"].apply(lambda _: datetime.utcfromtimestamp(_))

        return df_atmo

    def display_data_summary(self):
        df_atmo = self.create_dataframe()

        villes = df_atmo["nom_com"].unique().tolist()
        villes.sort()
        polluants = df_atmo["nom_poll"].unique().tolist()
        polluants.sort()
     
        print("Liste des villes : ")
        print(tabulate([[v] for v in villes], headers=["Villes"]))

        print("\nListe des polluants : ")
        print(tabulate([[p] for p in polluants], headers=["Polluants"]))
      df_atmo
# Example usage:
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?where=1%3D1&outFields=nom_com,nom_station,code_station,typologie,nom_poll,valeur,date_debut,influence&outSR=4326&f=json"
air_quality_data = AirQualityData(url)
air_quality_data.display_data_summary()


