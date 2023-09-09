""" 
Soit le programme suivant:

import turtle
polygon = turtle.Turtle()
color = "green"
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
polygon.color(color)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.exitonclick()

En vous inspirant du programme précédent, écrivez un programme qui demande à l'utilisateur
- "quelle figure voulez vous tracer?"
- "de quelle couleur doit être le contour de la figure?"

L'utilisateur devra saisir le nom d'une figure puis le nom d'une couleur
Le programme devra tracer cette figure en respectant la couleur choisie
Les figures acceptées sont:
- "cylindre", "cône", "pyramide", "prisme hexagonal" """

# CORRECTION 
import turtle

fig_accepte = ["cylindre","cone","pyramide","prisme"]
color = ["red","green","yellow"]

# Fonction qui permet de déssiner le cylindre
def dessine_cylindre(rayon,hauteur,polygon):
    rayon = 50 
    hauteur = 100

    polygon.up()
    polygon.goto(0, -rayon)  # Positionner la tortue au point de départ
    polygon.down()

    polygon.circle(50)
    polygon.penup()
    polygon.goto(0, hauteur)
    polygon.pendown()
    polygon.circle(50)

    polygon.penup()
    polygon.goto(0, 0)
            
    polygon.up()
    polygon.forward(rayon)
    polygon.down()
    polygon.left(90)
    polygon.forward(hauteur+rayon)
    polygon.left(90)

    polygon.up()
    polygon.forward(rayon*2)
    polygon.down()
    polygon.left(90)
    polygon.forward(hauteur+rayon)   

# Fonction qui permet de dessiner un cone
def dessine_cone(rayon,cone):
    cone.circle(rayon)
    cone.up()
    cone.goto(0,rayon)
    cone.forward(rayon)
    cone.down()
    cone.left(100)
    cone.forward(rayon*5)
    cone.left(157)
    cone.forward(rayon*5)

# Fonction pour déssiner la pyramide
def dessine_pyramide(pyramide):
    for _ in range(2):
        pyramide.left(45)
        pyramide.forward(100)
        pyramide.left(135)
        pyramide.forward(100)

    pyramide.left(90)
    pyramide.forward(200)
    pyramide.goto(0,0)
    pyramide.up()
    pyramide.right(90)
    pyramide.left(45)
    pyramide.forward(100)
    pyramide.left(73)
    pyramide.down()
    pyramide.forward(150)
    pyramide.goto(0,0)
    pyramide.left(62)
    pyramide.forward(100)
    pyramide.right(116)
    pyramide.forward(228)
    pyramide.right(166)
    pyramide.forward(140)
    pyramide.up()
    pyramide.goto(0,0)

# Fonction qui permet de dessiner le prise hexagonal
def dessine_prisme(prisme):
    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides
    
    prisme.up()
    prisme.goto(0,200)
    prisme.down()
    for i in range(num_sides):
        prisme.forward(side_length)
        prisme.right(angle)

    prisme.up()
    prisme.goto(0,0)
    prisme.down()
    for i in range(num_sides):
        if i in [0,1,5]:
            prisme.up()
            prisme.forward(side_length)
            prisme.right(angle)
            continue
        prisme.down()
        prisme.forward(side_length)
        prisme.right(angle)

    prisme.up()
    prisme.goto(0,0)
    prisme.left(angle)
    prisme.backward(side_length)
    prisme.left(angle/2)
    prisme.down()
    prisme.forward(200)
    prisme.backward(200)
    prisme.left(angle/2)
    prisme.backward(side_length)
    prisme.right(angle/2)
    prisme.forward(200)
    prisme.right(90)
    prisme.forward(side_length)
    prisme.right(90)
    prisme.forward(200)
    prisme.backward(200)
    prisme.left(90+angle)
    prisme.forward(side_length)
    prisme.left(angle/2)
    prisme.left(180)
    prisme.forward(200)



figure = input("Quelle figure voulez-vous tracer ? ")
if figure not in fig_accepte:
    print("Figure non prise en charge.")
    print("Chosissez une figure parmi celles-ci : ",fig_accepte)
else:
    couleur = input("De quelle couleur doit être le contour de la figure? ")
    if couleur not in color:
        print("Couleur non prise en charge.")
        print("Chosissez une couleur parmi celles-ci : ",color)
    else:        
        polygon = turtle.Turtle()
        polygon.color(couleur)

        if figure == "cylindre":
            dessine_cylindre(rayon=50,hauteur=100,polygon=polygon)
            #turtle.exitonclick()
        elif figure=="cone": 
            dessine_cone(rayon=50,cone=polygon)
            #turtle.exitonclick()
        elif figure=="pyramide":
            dessine_pyramide(pyramide=polygon)
            #turtle.exitonclick()
        elif figure=="prisme":
            dessine_prisme(prisme=polygon)
            #turtle.exitonclick()
        else:
            print("Merci...")
        
        turtle.exitonclick()


  

        

            

