#!/usr/bin/python
#
# Problem: FreeCell Statistics
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    n, pd, pg = map(int, raw_input().split())

    if pg == 100 and pd < 100:
        return "Broken"
    if pg == 0 and pd > 0:
        return "Broken"
    if pd == 0:
        return "Possible"

    p = pd
    r = 100
    while p%5 == 0 or p%2 == 0:
        if p%5 == 0:
            p /= 5
            if r%5 == 0:
                r /= 5
        if p%2 == 0:
            p /= 2
            if r%2 == 0:
                r /= 2
    if r <= n:
        return "Possible"
    else:
        return "Broken"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
