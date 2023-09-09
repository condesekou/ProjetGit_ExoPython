"""
écrire un programme qui:
- définit une fonction h
  - qui prend en paramètre un nombre n
  - calcule le reste de la division n/2
- demande à l'utilisateur un nombre N
- appelle la fonction h avec le nombre N

D'après vous, comment écrire une fonction qui vous dit
- si vrai ou faux un nombre est impair ?
- si vrai ou faux un nombre est pair ?
"""
def h(nombre):
    return nombre%2

nb = int(input("Entrer un nombre "))
reste_division = h(nb)
if reste_division==0:
    print("Le nombre",nb,"est paire")
else:
    print("Le nombre",nb,"est impaire")



