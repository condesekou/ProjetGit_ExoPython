"""
Définir deux ensembles suivants :
X = {'a', 'b', 'c', 'd' }
Y = {'s', 'b', 'd' }

puis affichez les résultats suivants :
– les ensembles initiaux ;
– le test d’appartenance de l’élément 'c' à X ;
– le test d’appartenance de l’élément 'a' à Y ;
– les ensembles X − Y et Y − X ;
– l’ensemble X ∪ Y (union) ;
– l’ensemble X ∩ Y (intersection).
"""
X = {'a', 'b', 'c', 'd' }
Y = {'s', 'b', 'd' }
print("==> Les ensembles initiaux")
print(X)
print(Y)
print("==> Le test d'appartenance de 'c' à X")
if 'c' in X:
    print("Vrai")
else:
    print("Faux")

print("==> Le test d'appartenance de 'a' à Y")
if 'a' in Y:
    print("Vrai")
else:
    print("Faux")

print("==> L'ensemble X - Y")
print(X-Y)

print("==> L'ensemble Y - X")
print(Y-X)

print("==> L'ensemble X U Y")
print(X.union(Y))

print("==> L'ensemble X n Y")
print(X.intersection(Y))



