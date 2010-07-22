#!/usr/bin/python
#
# Problem: Old Magician
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    w, b = map(int, raw_input().split())

    if b%2 == 0:
	return "WHITE"
    else:
        return "BLACK"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
