#!/usr/bin/python

import csv

with open ("désordre", "r") as désordre:
  if désordre.closed:
    print ("je sais pas quoi")
    return

  contenu = désordre.read()
  liste_nombres = []
  for nombre_chaine in contenu.split():
    nombre_converti = int(nombre_chaine)
    liste_nombres += [nombre_converti]

  liste_nombres.sort()

with open ("croissant", "w") as croissant:
  for nombre in liste_nombres:
    nombre = str(nombre)
    croissant.write(nombre + " ")
