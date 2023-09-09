"""
On désire simuler Pile ou Face à l'aide d'un script dans lequel le chiffre 0 sera associé à Pile et le chiffre 1 à Face.
Écrire le script.
"""
import random

nbre = random.randint(0,1)
text = "Pile" if nbre==0 else "Face"

print("===> Le jeu est démarré ")
val = int(input("Pile (0) ou Face (1) ? "))

if  val == nbre:    
    print("Félicitations ! Vous avez gagné, le résultat etait",text)
else:
    print("Désolé, Vous avez perdu ! Le résultat était",text)


