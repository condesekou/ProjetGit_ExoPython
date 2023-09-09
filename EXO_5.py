"""
counter = 0                     " initialisation de la variable de parcours"
end_value = 100                 " la valeur maximale à atteindre"
print("counter value", counter) " affiche la valeur de la variable de parcours" 
while counter <= end_value:     " boucler tantque 0<=100 " 
    print(counter)              " afficher la variable de parcours"
    counter = counter + 1       " incrementé la variable de parcours pour passer à la valeur suivante"
print("counter value", counter) " afficher la dernière valeur de la variable de parcours"
"""
"""
    La différence entre la boucle while et la boucle for est que, la boucle while est utilisée lorsque 
    le nombre d'itérations est inconnu, elle continuera à boucler tantque la condition est vérifié.
    Alors que la boucle for est utilisée lorsque le nombre d'itérations est connue à l'anvance.
"""
# - Ecrivez le programme précédent en utilisant une boucle for
print("le programme précédent en utilisant une boucle for")
counter = 0
end_value = 100
print("counter value", counter)
for counter in range(end_value+1):
    print(counter)
print("counter value", counter)

print("afficher les nombres allant de 10 à 20 en comptant de 2 en 2")
i = 10
while i <=20 :
    print(i)
    i+=2

print("afficher les nombres allant de 20 à 10 en comptant de 4 en 4")
i=20
while i>10:
    print(i)
    i-=4
