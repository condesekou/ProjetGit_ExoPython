"""
écrire un programme qui
- demande à l'utilisateur de saisir un nombre
- stocke ce nombre dans une variable n
- additionne chaque chiffre du nombre n
- affiche cette somme
Vous proposerez deux solutions: avec un for et avec un while
"""

nbre = int(input("Entrer un nombre "))

# Avec la boucle for
som = 0
for i in range(nbre+1):
    som+=i

print("Boucle for - La somme est : ",som)

#Avec la boucle while
i,som=1,0
while i<=nbre:
    som+=i
    i+=1
print("Boucle While - La somme est : ",som)

