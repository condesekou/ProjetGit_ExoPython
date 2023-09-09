"""
- A l'aide de matplotlib tracer la courbe telle que x = [1, 2, 3, 4] et y = [1, 4, 9, 16]
- A l'aide de matplotlib tracer le nuage de point tel quel que x = [1, 2, 3, 4] et y = [1, 4, 9, 16].
- Ensuite, ecrire un programme qui demande à l'utilisateur:
  - la liste des abscices
  - la liste des ordonnées
  - s'il veut tracer une courbe ou un nuage de point
  - le programme devra ensuite faire le tracé suivant ce que l'utilisateur aura saisi
"""

import matplotlib.pyplot as plt
x = [1, 2, 3, 4] 
y = [1, 4, 9, 16]

plt.plot(x,y)
plt.title("La courbe")
plt.show()

plt.scatter(x,y)
plt.title("Le nuage de point")
plt.show()

abs = input("Entrer la liste des abscices (séparé par un espaces) ").split(" ")
ord = input("Entrer la liste des ordonnés (séparé par un espaces) ").split(" ")

plt.plot(abs,ord)
plt.title("Representation de votre courbe")
plt.show()
