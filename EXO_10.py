"""
écrire un programme qui :
- demande à l'utilisateur de saisir le rayon de la base du cylindre,
- demande à l'utilisateur de saisir la hauteur du cylindre
- définit une fonction f qui:
  - prend 3 paramètres: rayon r, hauteur h, nombre n
  - calcule le volume v du cylindre de rayon r et de hauteur h
  - renvoie le volume v, arrondi à n chiffres après la virgule
- utilise la fonction f pour calculer le volume v
- affiche v
"""
import math 

def f(rayon,hauteur,nombre):
    volume = math.pi * rayon**2 * hauteur
    return round(volume,nombre)

r = float(input("Entrer le rayon du cylindre "))
h = float(input("Entrer la hauteur du cylindre "))
n = 3

print("Volume du cylindre :",f(r,h,n))
