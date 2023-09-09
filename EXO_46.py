"""
Ecrire un programme demandant à l'utilisateur de saisir
- une liste d'abscisses
- une liste d'ordonnées
- une liste de 0 et de 1
Par exemple:
- x = [1, 2, 3, 4, 5]  # on a 5 x
- y = [2, 4, 6, 8, 10] # on a 5 y
- c = [0, 1, 0, 1, 0]  # on a 5 c

- Le programme devra prendre ces valeurs et les stocker dans une table
- Le programme devra ensuite tracer un nuage de points en utilisant les valeurs de x et de y
- Attention:
  - la colonne c represente une couleur de point
  - 0 --> bleu
  - 1 --> rouge
  - ex: le premier point, de coordonnées (1, 2) doit avoir la couleur bleue
"""
import pandas as pd

import matplotlib.pyplot as plt

x = input("Entrer une liste d'abscisses (séparés par un espace) ").split(" ")
y = input("Entrer une liste d'ordonnées (séparés par un espace) ").split(" ")
c = input("Entrer une liste de 0 ou 1 (séparés par un espace) ").split(" ")

data_final = pd.DataFrame({'axe_x':x,'axe_y':y,'color':c})

data_final.color = data_final.color.apply(lambda x: 'blue' if x=='0' else 'red')

print(data_final)

plt.scatter(x=data_final.axe_x,y=data_final.axe_y,c=data_final.color)
plt.show()