"""
- écrire une fonction récursive qui calcule le nombre de chiffre d'un nombre positif.
"""

def nbre_chffre(n):
    if n < 10:
        return 1  
    else:
        return 1 + nbre_chffre(n / 10)



nombre = int(input("Entrer un nombre positif "))
resultat = nbre_chffre(nombre)
print("Le nombre de chiffres dans", nombre, "est", resultat)  
