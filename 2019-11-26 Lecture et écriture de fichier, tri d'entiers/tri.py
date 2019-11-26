#!/usr/bin/python

import csv

with open ("désordre", "r") as désordre:
  for x in désordre:
    print (x)
  if désordre.closed:
    print ("je sais pas quoi")
  
