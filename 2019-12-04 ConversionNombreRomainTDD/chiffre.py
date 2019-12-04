#I=1 V=5 X=10 L=50 C=100 D=500 M=1000
#additionner les valeurs correspondant aux chiffres romains
#si un chiffre plus petit précède un chiffre plus grand, il faut soustraire le chiffre plus petit au plus grand

def conversion(roman):
    resultat = 0
    for char in roman:
        if char == "I":
            resultat += 1
        elif char == "V":
            resultat += 5
        elif char == "X":
            resultat += 10
        elif char == "L":
            resultat += 50
        elif char == "C":
            resultat += 100
        elif char == "D":
            resultat += 500
        elif char == "M":
            resultat += 1000
    return resultat
