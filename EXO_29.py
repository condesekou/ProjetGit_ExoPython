"""
Ecrire une fonction qui prend en paramètre une chaine de caractère
La fonction devra renvoyer vrai si la chaine est un palindrome, faux autrement.
"""

mot = input("Donner un mot ")


if mot.lower() == mot[::-1].lower():
    print("Le mot est palindrome")
else:
    print("Le mot n'est pas palindrome")