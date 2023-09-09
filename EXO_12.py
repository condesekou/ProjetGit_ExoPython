"""
écrire un programme qui
- demande à l'utilisateur de saisir des nombres séparés par des "@"
- enregistre chacun de ces nombres dans une liste
- classe les nombres par ordre décroissant
- affiche la liste
"""

chaine = input("Entrer des nombre séparés par @ ")

lst = chaine.split("@")
lstNew = []
for nb in lst:
    lstNew.append(int(nb))

lstNew.sort()
print("La liste des nombres ordonnés : ",lstNew)

