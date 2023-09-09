"""
Un sac est rempli de 6 billes jaunes et de 14 billes vertes, toutes indiscernables au toucher.
On effectue un tirage au hasard d'une bille du sac et on appelle « succès » le fait d'obtenir la couleur jaune.
Ecrire le programme permettant de calculer la probabilité de chaque couleur en fonction du nbre de billes.
Ecrire le prorgamme qui simule le tirage d'une couleur
"""
import random

nb_billes_jaunes = 6
nb_billes_vertes = 14

total_billes = nb_billes_jaunes+nb_billes_vertes

prob_succes = round((nb_billes_jaunes/total_billes)*100,2) 
prob_echec = round((nb_billes_vertes/total_billes)*100,2) 

print("La probilité du succès est : ",prob_succes,"%")
print("La probilité de l'échec est : ",prob_echec,"%")

# similitation du tirage 
# On va créer une liste avec les couleur des différentes billes 
billes = ['jaune'] * nb_billes_jaunes
billes.extend(['verte']*nb_billes_vertes)

# On sélectionne une couleur au hasard
bille_tiree = random.choice(billes)

print("la bille tirée est",bille_tiree)


