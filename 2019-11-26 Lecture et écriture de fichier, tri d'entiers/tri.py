#!/usr/bin/python

import csv

with open ("désordre", "r") as désordre:
  contenu = désordre.read()
  liste_nombres = []
  for nombre_chaine in contenu.split():
    nombre_chaine = int(nombre_chaine)
    liste_nombres += [nombre_chaine]
  
  print (liste_nombres)
  #print (contenu.split())
  #print (contenu)
  if désordre.closed:
    print ("je sais pas quoi")
  
