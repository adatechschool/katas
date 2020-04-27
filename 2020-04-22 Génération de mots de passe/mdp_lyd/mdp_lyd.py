#!/usr/bin/env python

import random
import string

def mdp_aleatoire():
    car = string.ascii_letters + string.digits + string.punctuation
    taille = int(input("Choisissez la taille du mdp : "))
    return ''.join(random.choice(car) for i in range(taille))

print("Le mdp proposé est :", mdp_aleatoire())
