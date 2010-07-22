#!/usr/bin/python
#
# Problem: Text Messaging Outrage
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    p, k, l = map(int, raw_input().split())
    fs = map(int, raw_input().split())
    
    fs.sort()

    c = 0
    for i in range(l):
	c += fs[l-i-1] * (i/k + 1)

    return c


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
