#!/usr/bin/python
#
# Problem: All Your Base
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out


import sys
from math import *
from string import *


def compute():
    d = dict()
    s = file.readline()[:-1]

    st = set(list(s))
    base = max(2,len(st))
    
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
        



file = sys.stdin

case = int(file.readline())

for i in range(case):
    print "Case #" + str(i+1) + ":",
    print compute()
