"""
- Qu'est ce qu'un diagramme en barre ? Dans quel cas il s'utilise ?
- A l'aide de matplotlib, tracer un diagramme en barre representant les données suivantes:
x = ['Pommes, 'Bananes, 'Oranges', Mangues']
y = [20, 15, 25, 10]
- refaire la même chose cette fois ci avec des barres horizontales
- Ensuite, écrire un programme qui trace un diagramme en barre,
  - cette fois ci les données doivent venir d'une table SQL contenant deux colonnes: "nom", "quantité"
"""
# Un diagramme en barre permet de representer des variables catégorielles.
# Chaque barre represente un catégorie en particulier et la hauteur de la barre 
# indique la valeur de cette catégorie. 
# On l'utilise souvent pour des comparaison ou pour vérifier des tendances
import matplotlib.pyplot as plt

x = ['Pommes', 'Bananes', 'Oranges', 'Mangues']
y = [20, 15, 25, 10]

plt.bar(x,y)
plt.title("Le Diagramme en barre")
plt.show()

plt.barh(x,y)
plt.title("Le Diagramme en barre horizontal")
plt.show()


