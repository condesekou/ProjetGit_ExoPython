"""
En partant du dictionnaire suivant:
student1 = {"Fullname": "Patrick Nsukami", "birthdate": "1980/01/01", "matières": {"maths": [45, 56, 78]}}

Demandez à l'utilisateur de saisir:
- une nouvelle matière
- le nombre de notes pour cette nouvelle matière
- les notes en question

Le programme devra ensuite modifier le dictionnaire initial tel que:
student1 = {"Fullname": "Patrick Nsukami",
            "birthdate": "1980/01/01",
            "matières": {"maths": [45, 56, 78], "english": [34, 67, 89]}}
"""
student1 = {"Fullname": "Patrick Nsukami", "birthdate": "1980/01/01", "matières": {"maths": [45, 56, 78]}}
matiere = input("La nouvelle matière ")
nbNote = int(input("Le nombre de notes à saisir "))

lstNotes = []
for i in range(nbNote):
    n = input(f"Note {i+1} ")
    lstNotes.append(n) 

mat = {matiere:lstNotes}

student1.get("matières").update(mat)

print(student1)

