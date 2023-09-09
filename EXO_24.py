"""
Écrire un programme qui
- demande à l’utilisateur de saisir une liste de mots séparés par des virgules.
- fabrique un dictionnaire vide “D”
- parcourt la liste de mots
- si le mot possède au moins 3 lettres
  * ajoute dans le dictionnaire “D” le mot comme étant la clé, la longueur du mot comme étant la valeur

Par exemple, si la liste de mots est : ['cat', 'at', 'car', 'fear', 'center'],
alors le dictionnaire sera {'cat': 3, 'car': 3, 'fear': 4, 'center: 5'}
"""
mots = input("Entrer une liste de mots séparés par des virgules")
lst = mots.split(",")
D = {}

for m in lst:
    if len(m)>=3:
        D[m]=lst.count(m)

print(D)