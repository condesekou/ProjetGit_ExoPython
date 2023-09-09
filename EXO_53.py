"""
- écrire une fonction récursive qui calcule le produit de deux nombres positifs en utilisant seulement l'addition et la récursion (ne pas utiliser de multiplication).

- écrire une fonction récursive qui calcule la divisition de deux nombres positifs en utilisant seulement la soustraction et la récursion (ne pas utiliser de division).

"""
def produit(x, y):
    if y == 0:
        return 0
    elif y < 0:
        return -produit(x, -y)
    else:
        return x + produit(x, y - 1)
    
def division(x, y):
    if x < y:
        return 0
    else:
        return 1 + division(x - y, y)

a = int(input("Donner le premier nombre "))
b = int(input("Donner le 2ème nombre "))
resultat_produit = produit(a, b)
print("Le produit de", a, "et", b, "est", resultat_produit) 


resultat_division = division(a, b)
print("La division de", a, "par", b, "est", resultat_division) 

