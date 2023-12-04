import pandas as pd

# Exemple de données
data = {'nom_com': ['SAINT-GIRONS', 'RODEZ', 'ALES', 'LA CALMETTE']}
df = pd.DataFrame(data)

# Appliquer la transformation sur la colonne 'nom_com'
df['nom_com'] = df['nom_com'].str.title()

# Afficher le DataFrame résultant
print(df)
