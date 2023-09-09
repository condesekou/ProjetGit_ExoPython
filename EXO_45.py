"""
A l'aide d'un programme Python, creer une table contenant les données suivantes:
- tarif = [20, 30, 10, 40]
- étiquette = ['Pommes, 'Bananes, 'Oranges', Mangues']
écrire le programme Python qui récupère ces données de la table et trace un diagramme en camembert
"""

import pandas as pd
import matplotlib.pyplot as plt

tarif = [20, 30, 10, 40]
etiquette = ['Pommes', 'Bananes', 'Oranges', 'Mangues']

data = pd.DataFrame({'etiquette':etiquette,'tarif':tarif})

print(data)

plt.pie(data=data,x=data.tarif,labels=data.etiquette,autopct='%1.1f%%', startangle=90)
plt.legend()
plt.show()