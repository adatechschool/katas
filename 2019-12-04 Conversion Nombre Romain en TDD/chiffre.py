#I=1 V=5 X=10 L=50 C=100 D=500 M=1000
#additionner les valeurs correspondant aux chiffres romains
#si un chiffre plus petit précède un chiffre plus grand, il faut soustraire le chiffre plus petit au plus grand

table_conversion = {
        None: 0,
        "I" : 1, 
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000
        }

def conversion(roman):
    resultat = 0
    for char, suivant in zip(roman, list(roman[1:]) + [None]):
        if table_conversion[char] < table_conversion[suivant]:
            resultat -= table_conversion[char]
        else:
            resultat += table_conversion[char]
    return resultat
