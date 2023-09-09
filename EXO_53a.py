"""
- Qu'est ce qu'un diagramme en barre empilé ? Quand est ce qu'on s'en sert ?
- proposez des exemples d'illustration
"""

# Les diagrammes à barres empilées affiche la taille relative 
# (sous la forme d’un nombre total , pourcentage, ou d’une autre variable numérique) 
# d’une variable catégorielle, subdivisée par couleur en fonction d’un sous-groupe

import matplotlib.pyplot as plt
import pandas as pd

produits = ['Ordinateur', 'Imprimante', 'Sac', 'Chaussure']
ventes_janvier = [20000, 30000, 15000, 25000]
ventes_fevrier = [22000, 32000, 16000, 26000]

fig, ax = plt.subplots()

ax.bar(produits, ventes_janvier, label='Janvier')
ax.bar(produits, ventes_fevrier, label='Février', bottom=ventes_janvier)

ax.set_xlabel('Produits')
ax.set_ylabel('Ventes')
ax.set_title('Répartition des ventes par produit')

ax.legend()

plt.show()
