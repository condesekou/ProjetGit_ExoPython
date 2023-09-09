"""
Exercice 4:
-----------
- Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom
- Ecrire un programme qui utilise turtle pour écrire (dessiner) votre nom (chaque lettre ayant une couleur différente)
"""
import turtle

dessin = turtle.Turtle()
dessin.color("red")

# la lettre C
dessin.circle(40,-180)
dessin.up()
dessin.goto(50,0)
dessin.right(180)
dessin.down()
# la lettre O
dessin.color("blue")
dessin.circle(40)
dessin.up()
dessin.goto(100,0)
dessin.left(90)
dessin.down()
# la lettre N
dessin.color("green")
dessin.forward(80)
dessin.right(145)
dessin.forward(95)
dessin.left(145)
dessin.forward(80)
dessin.up()
dessin.goto(165,0)
dessin.down()
# la lettre D
dessin.color("black")
dessin.forward(80)
dessin.right(90)
dessin.circle(-40,180)
dessin.right(180)
dessin.up()
dessin.goto(220,0)
dessin.down()
# La lettre E
dessin.color("yellow")
dessin.forward(40)
dessin.backward(40)
dessin.left(90)
dessin.forward(40)
dessin.right(90)
dessin.forward(40)
dessin.backward(40)
dessin.left(90)
dessin.forward(40)
dessin.right(90)
dessin.forward(40)

turtle.exitonclick()