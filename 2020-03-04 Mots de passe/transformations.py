#!/usr/bin/env python

def majuscule(s):
  return {s.upper()}

def minuscule(s):
  return {s.lower()}

def camelcase(s):
  r1 = r2 = ""
  for index, car in enumerate(s):
    if index%2 == 0:
      r1 += car.upper()
      r2 += car.lower()
    else:
      r1 += car.lower()
      r2 += car.upper()
  
  return {r1, r2}

def transforme (s):
  transformations = set({})
  
  transformations = transformations.union(majuscule(s))
  transformations = transformations.union(minuscule(s))
  transformations = transformations.union(camelcase(s))
  
  return transformations


print (transforme("salut"))
