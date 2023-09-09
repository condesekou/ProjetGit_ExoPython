"""
écrire un programme qui:
- définit un dictionnaire contenant des célébrations, ex: {"Nouvel an": "1 Janvier", "Tabaski": "10 Juillet", "Pentecote": "5 Juin"}
- demande à l'utilisateur de:
  - saisir le jour
  - saisir le mois
- vérifie si la date saisie correspond à une date de célébration
  - si oui, afficher la célébration en question
  - si non, afficher le message: "Cette date ne correspond à aucune célébration"

* Attention:
- même si l'utilisateur saisit "1 jAnViEr", le programme sera capable de reconnaitre qu'il s'agit du nouvel an

"""
celebrations = {"Nouvel an": "1 Janvier", "Tabaski": "10 Juillet", "Pentecote": "5 Juin"}
jour = input("Entrer le jour ")
mois = input("Entrer le mois ")

date = jour+" "+mois.capitalize()

find = False
for key,value in celebrations.items():
    if value==date:
        print(key)
        find = True
        break

if not find:
    print("Cette date ne correspond à aucune célébration")