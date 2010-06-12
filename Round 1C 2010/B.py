#!/usr/bin/python
#
# Problem: Load Testing
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 

from math import *

def compute():
    l, p, c = map(int, raw_input().split())
    return ceil(log(ceil(log((p+0.0)/l,c)),2))

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
