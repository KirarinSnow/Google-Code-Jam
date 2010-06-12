#!/usr/bin/python
#
# Problem: Minimum Scalar Product
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out

import sys
from math import *

MAX = 1000000000

def compute():
    nn = int((file.readline().split())[0])
    q = map(int,file.readline().split())
    r = map(int,file.readline().split())
    q.sort()
    r.sort()
    v = 0
    for p in range(nn):
	v+= q[p]*r[nn-p-1]
    return str(v)


file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += compute()
    print s
