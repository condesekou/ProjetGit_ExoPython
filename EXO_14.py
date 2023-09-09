"""
écrire un programme qui:
- définit une liste ne contenant que des voyelles
- définit une liste ne contenant que des consonnes
- définit une liste ne contenant que la lettre "y"
- demande à l'utilisateur de saisir une lettre
- vérifie si la lettre saisie est une voyelle ou une consonne
- affiche l'un des 2 messages suivants
  - disant à l'utilisateur: "vous avez saisi une ..."
  - "y est parfois considéré comme une voyelle, parfois non"

"""
CONSONNES = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
VOYELLES = ["a","e","i","o","u"]
Y = ["y"]

lettre = input("Entrer une lettre ")

if lettre.lower() in CONSONNES:
    print("Vous avez saisie une consonne")
elif lettre.lower() in VOYELLES:
    print("Vous avez saisie une voyelle")
elif lettre.lower() in Y:
    print("y est parfois considéré comme une voyelle, parfois non")
else:
    print("Lettre non prise en charge...")
