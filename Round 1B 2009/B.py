#!/usr/bin/python
#
# Problem: The Next Number
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out


import sys
from math import *
from string import *


def next():
    return buffer.pop(0)

def nint():
    return int(next())


def compute():
    def f(x):
        if x == '0':
            return 'a'
        else:
            return x
    
    def g(x):
        if x == 'a':
            return '0'
        else:
            return x
    
    def ds(n): # largest decreasing suffix
        i = 0
        while i < len(n)-1 and n[len(n)-1-i] <= n[len(n)-2-i]:
            i+=1
            
        return len(n)-2-i,n[len(n)-1-i:]
        
    n = list(str(nint()))

    inc, d = ds(n)

    
    if inc == -1:
        d2 = map(f, d)
        d2.sort()
        d3 = map(g, d2[1:])
        d3.sort()
        
        return d2[0] + '0' + ''.join(d3)

    else:
        d.insert(0,n[inc])
        d.sort()

        ii = d.index(n[inc]) + d.count(n[inc])
        if ii >= len(d):
            aa = 1/0 #????
        else:
            aa = d[d.index(n[inc])+d.count(n[inc])]
        d.remove(aa)
        return ''.join(n[:inc]) + aa + ''.join(d)



file = sys.stdin

case = int(file.readline())
buffer = file.read().split()

for i in range(case):
    print "Case #" + str(i+1) + ":",
    print compute()
