import turtle

# Demandez à l'utilisateur d'entrer la longueur et la largeur
long = float(input('Entrer la longueur : '))
larg = float(input('Entrer la largeur : '))

# Calculez la surface et le périmètre
surface = long * larg
perimetre = 2 * (long + larg)

print('La surface est', surface)
print('Le périmètre est', perimetre)

# Demandez si l'utilisateur souhaite tracer le rectangle
demande = input('Voulez-vous tracer le rectangle ? (O/N) ').strip().lower()

if demande == 'o':
    
    turtle.clear()
    rectangle = turtle.Turtle()
    
    for i in range(2):
        rectangle.forward(long)
        rectangle.left(90)
        rectangle.forward(larg)
        rectangle.left(90)    
    
    turtle.exitonclick()
else:
    print('Au revoir ...')