"""
Ecrivez un programme qui demande à l'utilisateur d'entrer
- t: sa taille en m (convertir t en nombre réel)
- m: sa masse en kg (convertir m en nombre réel)

Le programme devra ensuite calculer et afficher l'indice de masse corporelle et l'afficher:
- IMC = m / t²

Si IMC est:
- inférieur à 16,5: le programme devra afficher le message: "dénutrition"
- compris entre 16,5 et 18,5: "maigreur"
-         entre 18,5 et 25: "masse normale"
-         entre 25 et 30: "surpoids"
- supérieur à 30: "obésité"
"""

# CORRECTION 
taille = float(input("Quelle est votre taille ? "))
masse = float(input("Quelle est votre masse ? "))

indice = masse / (taille**2)

if indice<16.5:
    print("IMC = ",indice," - Dénutrition")
elif indice>=16.5 and indice<18.5:
    print("IMC = ",indice," - Maigreur")
elif indice>=18.5 and indice<25:
    print("IMC = ",indice," - Masse normale")
else:
    print("IMC = ",indice," - Obésité")

