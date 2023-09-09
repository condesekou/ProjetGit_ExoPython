"""
il existe un module nommé time dans votre système
et à l'intérieur de ce module, il y a une fonction: asctime
lire la doc, donner un exemple d'utilisation de cette fonction
"""
import time

current_time = time.localtime()

print("Temps non formaté : ",current_time)

formatted_time = time.asctime(current_time)

print("Après utilisation de la methode asctime : ", formatted_time)

