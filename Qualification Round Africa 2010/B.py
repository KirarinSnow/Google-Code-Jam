#!/usr/bin/python
#
# Problem: Reverse Words
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    return ' '.join(raw_input().split()[::-1])

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
