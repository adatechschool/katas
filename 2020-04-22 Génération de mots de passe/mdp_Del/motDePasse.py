#!/urs/bin/env python

import random
import string

lettre = {1:"a", 2:"e", 3:"i", 4:"o", 5:"u"}

#print(random.choice(lettre))

def mot_aleatoire(nombre):
    i = 0
    phrase = ""
    while i<nombre :
        phrase += random.choice(lettre)
        i += 1
        print(phrase)
        print('je suis dans le while')
    return phrase 

print(mot_aleatoire(15))
