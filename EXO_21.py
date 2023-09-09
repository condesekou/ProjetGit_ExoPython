"""
Exercice 21:
------------
A.
Soit la variable chaine suivante:
chaine = "Un pays que je veux remttre sur pied"
- Ecrire un programme qui prend n'importe quelle chaine de caractères
- Et dans cette chaine, remplace "je veux" (s'il existe) par "Assim veut".

B.
Découper ensuite chaine en une liste de mots, stockée dans une variable liste_mots.
Vous proposerez deux manières de faire.

C.
A partir de liste_mots:
- créer un dictionnaire qui contiendra:
  - comme clés, chaque mot,
  - comme valeurs, le nombre d'occurence de chaque mot
Vous proposerez deux manières de faire.

Faites, A, B, et C à l'aide de fonctions dont vous définirez:
- les paramètres
- les valeurs retournées
"""

# Solution A 
chaine = "Un pays que je veux remttre sur pied"
print(chaine[chaine.index(" "):len(chaine)])
result = chaine.replace("je veux","Asim veut")
print(result)

# Solution B 
# 1ère méthode
liste_mots = chaine.split(" ")
print("Avec 1ère méthode :",liste_mots)

# 2ème méthode
mes_mots = []
i = 0
while i<len(chaine):
    try:
        index = chaine.index(" ",i)
        mot = chaine[i:index]
        mes_mots.append(mot)
        i = index+1
    except ValueError:
        mot = chaine.split(" ")[-1]
        mes_mots.append(mot)
        break

print("Avec la 2ème méthode",mes_mots)



