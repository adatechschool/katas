#!/urs/bin/env python

import random
import string

lettre = {0:"a", 1:"e", 2:"i", 3:"o", 4:"u"}

def mot_aleatoire(nombre):
    i = 0
    phrase = ""
    while i<nombre :
        key = random.choice(list(lettre))
        phrase += lettre[key]
        i += 1
        #print(phrase)
        #print('je suis dans le while')
    return phrase 

print(mot_aleatoire(15))
