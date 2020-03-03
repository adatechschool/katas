#!/usr/bin/env python

# Objectifs :
# - se connecter à une bdd sqlite3
# - tester si une table « Produits » existe, et si non la créer
# - insérer un produit
# - lister les produits

import sqlite3

conn = sqlite3.connect('base-prod.sqlite3')

cur = conn.cursor()

cur.execute ('''SELECT * FROM sqlite_master WHERE type = 'table' AND name = 'Produits' ''')

# Retourne None si la table n'existe pas
# Retourne des données sinon
r = cur.fetchone()

if r == None:
  cur.execute ('CREATE TABLE Produits (prix float, code int, description text)')
  print ("La table n'existait pas alors je l'ai créée")

