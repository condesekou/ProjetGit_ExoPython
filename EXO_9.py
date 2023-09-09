"""
écrire un programme qui :
- demande à l'utilisateur de saisir le rayon de la base du cylindre,
- demande à l'utilisateur de saisir la hauteur du cylindre
- calcule le volume du cylindre
- affiche le volume du cylindre arrondi à 3 chiffres après la virgule
"""
import math 

rayon = float(input("Entrer le rayon du cylindre "))
hauteur = float(input("Entrer la hauteur du cylindre "))

volume = math.pi * (rayon**2) * hauteur

print("Volume du cylindre :",volume)
print("Volume du cylindre arrondi à 3 chiffre :",round(volume,3))
