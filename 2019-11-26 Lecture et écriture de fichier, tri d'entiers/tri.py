#!/usr/bin/python

import csv

with open ("désordre", "r") as désordre:
  contenu = désordre.read()
  for nombre_chaine in contenu.split():
    nombre_chaine = int(nombre_chaine)
  #print (contenu.split())
  #print (contenu)
  if désordre.closed:
    print ("je sais pas quoi")
  
