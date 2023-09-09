"""
lst = [55, 17, 38, 10, 25, 72, 567, 122, 369]

puis effectuez les actions suivantes :
– triez et affichez la liste ;
– ajoutez l’élément 12 à la liste et affichez la liste ;
– renversez et affichez la liste ;
– affichez l’indice de l’élément 17 ;
– enlevez l’élément 38 et affichez la liste ;
– affichez la sous-liste du 2eau 3eélément ;
– affichez la sous-liste du début au 2eélément ;
– affichez la sous-liste du 3eélément à la fin de la liste ;
– affichez la sous-liste complète de la liste ;
"""

lst = [55, 17, 38, 10, 25, 72, 567, 122, 369] 
print("===Liste triée ")
lst.sort()
print(lst)
print("===Ajout de l'élément 12 ")
lst.append(12)
print(lst)
print("===Renversement de la liste")
lst.reverse()
print(lst)
print("===Affichage de l'indice de l'élément 17")
print(lst.index(17))
print("===Suppression de l'élément 38 et affichage de la liste")
lst.remove(38)
print(lst)
print("===affichez la sous-liste du 2e au 3e élément ")
print(lst[1:3])
print("===affichez la sous-liste du début au 2e élément")
print(lst[0:2])
print("===affichez la sous-liste du 3e élément à la fin de la liste")
print(lst[2:])
print("===affichez la sous-liste complète de la liste")
print(lst[:])

