"""
Écrire une fonction compterMots ayant un argument (une chaîne de caractères)
La fonction renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.
"""
def compterMot(chaine:str):
    lst = chaine.split(" ")
    mydict = {}
    for m in lst:
        mydict[m]=lst.count(m)
    return mydict

machaine = input("Entrer une chaine de caractères ")

print("Le dictionnaire final : ")
print(compterMot(machaine))
