#!/usr/bin/python
#
# Problem: All Your Base
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    d = dict()
    s = raw_input()

    st = set(list(s))
    base = max(2, len(st))
    
    sum = 0
    for k in s:
        if k in d:
            value = d[k]
        else:
            value = len(d)
            if value < 2:
                value = 1 - value
            d[k] = value
        sum *= base
        sum += value

    return sum


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
