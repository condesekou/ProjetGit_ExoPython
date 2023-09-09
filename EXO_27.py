"""
Ecrire un programme qui demande à l'user de saisir:
- nom
- prenom
- age
- adresse
- nombre de notes à saisir
- pour quelle matière saisir ces notes
- les notes en question

Le programme devra ensuite fabriquer un dictionnaire tel que:
student1 = {"Fullname": "Patrick Nsukami", "birthdate": "1980/01/01", "matières": {"maths": [45, 56, 78]}}
"""

nom = input("Entrer votre nom ")
prenom = input("Entrer votre prénom ")
age = int(input("Donner votre âge "))
adresse = input("Donner votre adresse ")
nbNote = int(input("Le nombre de notes à saisir "))
matiere = input("La matière concernée ")

notes = {"nom":nom,"prenom":prenom,"age":age,"adresse":adresse }

lstNotes = []
for i in range(nbNote):
    n = input(f"Note {i+1} ")
    lstNotes.append(n)

matieres = {matiere:lstNotes}
notes["matiere"] = matieres

print(notes)


