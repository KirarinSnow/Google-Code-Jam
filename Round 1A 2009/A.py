#!/usr/bin/python
#
# Problem: Multi-base happiness
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Only works on small input.


import sys
from math import *
from string import *

def numdigs(n, b):
    o = 0
    while n >= b**o:
        o+=1
    return o


def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def next():
    return buffer.pop(0)

def nint():
    return int(next())

def happy(n, b):
    def hh(n, b):
        while n not in seen and n != 1:
            seen.add(n)
            sum = 0
            for i in range(numdigs(n, b)):
                sum += ((n / (b**i)) % b)**2
            n = sum
        if n == 1:
            return True
        else:
            return False

    seen = set()
    return hh(n,b)

def compute():
    def satisfactory(n, bases):
        r = True
        for b in bases:
            if (b != 2 and b!= 4):
                r = r and happy(n,b)
        return r
    
    bases = map(int, file.readline().split())

    n = 2
    while not satisfactory(n, bases):
        n+=1
    
    return n


file = sys.stdin

case = int(file.readline())

for i in range(case):
    print "Case #" + str(i+1) + ":",
    print compute()
