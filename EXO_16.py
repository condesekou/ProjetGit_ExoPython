"""
Ce programme est un petit jeu qui permet de générer un nombre aléatoire entre deux valeurs. 
Ensuite permet à l'utilisateur de déviner le nombre généré en lui accordant un certains
nombre de tentatives.
"""
import random # import de la library random pour la génération des chiffres aléatoire
import math # import de la library pour l'utilisation des fonctions mathématiques

lower = int(input("saisir borne inférieure: ")) # Demander à l'utilisateur de saisir la borne inférieure
upper = int(input("saisir borne supérieure: ")) # Demander à l'utilisateur de saisir la borne supérieure

x = random.randint(lower, upper) # génération du chiffre aléatoire
print("\n\tVous avez ",
	round(math.log(upper - lower + 1, 2)),
	" chances pour trouver le nombre exact!\n") # détermination du nombre de tentatives en utilisant le logarithme

count = 0 # initialisation du conteur (tentantives)

while count < math.log(upper - lower + 1, 2): # boucler tantque le nombre de tentative n'est pas atteint
	count += 1 # incrémenter le nombre de tentatives
	guess = int(input("Devinez le nombre:- ")) # Demander à l'utilisateur de donner un nombre
	if x == guess: # Tester si le nombre saisi par l'utilisateur est identique au nombre généré
		print("Felicitations vous avez trouvé en ", # Si c'est le cas, afficher le message de félicitation en indiquant le nombre de tentatives effectués
			count, " essais")
		break # Arrêter la boucle
	elif x > guess: # Sinon, si le nombre saisi est supérieur au nombre généré, on affiche Trop petit
		print("Trop petit!")
	elif x < guess: # sinon, si le nombre saisi est inférieur au nombre généré, on affiche Trop grand
		print("Trop grand!")

if count >= math.log(upper - lower + 1, 2): # Après la boucle, on teste si le nombre tentatives effectuées est supérieur ou égal au nombre de tentatives accordées, on affiche le nombre à l"utilisateur
	print("\nLe nombre était %d" % x)
	print("\tLa prochaine fois peut-être!")