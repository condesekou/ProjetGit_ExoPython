"""
Ecrire une fonction qui
- demande un entier de depart i et un entier d'arrivée j
- calcule la somme des entiers compris entre i et j de trois façons différentes :
  - en utilisant la formule classique : s = n n 1 / 2
  - en utilisant une boucle while
  - en utilisant une boucle for
"""

nbDepart = int(input("Entrer un entier de départ "))
nbArrivee = int(input("Entrer un entier d'arrivée "))

# avec la boucle while
i = nbDepart
som = 0
while i<=nbArrivee:
    som+=i
    i+=1

print(f"La somme des entier entre {nbDepart} et {nbArrivee} avec la boucle while est : {som}")

# Avec la boucle for
som2 = 0
for k in range(nbDepart,nbArrivee+1):
    som2+=k

print(f"La somme des entier entre {nbDepart} et {nbArrivee} avec la boucle for est : {som2}")
