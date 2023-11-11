import requests
import json
# API URL 
api_url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/donnees-synop-essentielles-omm/records?limit=20"

#récupérer les données JSON de l'API
response = requests.get(api_url)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    # Charger les données JSON à partir de la réponse
    data = response.json()

    
    print(data)
else:
    print("La requête a échoué avec le code:", response.status_code)
