#!/usr/bin/env python

import random
import string
import sys

if len(sys.argv) != 2:
    print ("Syntaxe: {} <longueur>".format(sys.argv[0]))
    sys.exit(1)

taille = int(sys.argv[1])

def mdp_aleatoire(taille):
    car = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(car) for i in range(taille))


print("Le mdp proposé est : ", mdp_aleatoire(taille))