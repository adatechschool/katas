#!/usr/bin/python

import csv

with open ("désordre", "r") as désordre:
  print (désordre.read())
  if désordre.closed:
    print ("je sais pas quoi")
  
