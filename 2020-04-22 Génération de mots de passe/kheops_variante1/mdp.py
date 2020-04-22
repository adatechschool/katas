#!/usr/bin/env python

import sys
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVZXYZabcdefghijklmnopqrstuvwxyz0123456789=+-_()[]{}#~@*|\/^%;:><.!,?$"

n = int (sys.argv[1])

mdp = "".join([chars[random.randint(0, len(chars)-1)] for i in range(0,n)])

print (mdp)
