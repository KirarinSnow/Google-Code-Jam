#!/usr/bin/python
#
# Problem: Perfect Harmony
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large.


def compute():
    n, l, h = map(int, raw_input().split())
    f = map(int, raw_input().split())
    
    b = False
    for i in range(l, h+1):
        if len(filter(lambda x: i%x==0 or x%i==0, f)) == len(f):
            return i
    return "NO"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
