#!/usr/bin/python
#
# Problem: Fair Warning
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from fractions import *

def compute():
    t = map(int, raw_input().split()[1:])
    m = min(t)
    d = map(lambda x: x-m, t)
    g = reduce(gcd, d, 0)
    return (g - m%g)%g
    
for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
