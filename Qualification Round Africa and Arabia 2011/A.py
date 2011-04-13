#!/usr/bin/env python
#
# Problem: Closing the Loop
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    s = input()
    v = raw_input().split()
    r = []
    b = []

    for k in v:
        n = int(k[:-1]) - 1
        if k[-1] == 'R':
            r.append(n)
        else:
            b.append(n)
    r.sort()
    b.sort()
    g = min(len(r), len(b))
    
    return 0 if g == 0 else sum(r[-g:] + b[-g:])
        

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
