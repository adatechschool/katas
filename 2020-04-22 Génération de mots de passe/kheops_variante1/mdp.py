#!/usr/bin/env python

import sys
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVZXYZabcdefghijklmnopqrstuvwxyz0123456789=+-_()[]{}#~@*|\/^%;:><.!,?$"

n = int (sys.argv[1])

mdp = "".join([random.choice(chars) for i in range(0,n)])

print (mdp)
