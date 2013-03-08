#!/usr/bin/python
#
# Problem: Qualification Round
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    s = map(int, raw_input().split())
    p = s.pop(0)
    c = s.pop(0)

    k = sum(s)/c
    f = True
    while f:
        f = False
        s = map(lambda x: min(k, x), s)
        if sum(s)/c < k:
            k = sum(s)/c
            f = True
    
    return k


for i in range(int(raw_input())):
    print "Case #%d: %s" % (i+1, compute())
