#!/usr/bin/python
#
# Problem: Multi-base happiness
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Only works on small input.


def numdigs(n, b):
    o = 0
    while n >= b**o:
        o += 1
    return o

def happy(n, b):
    def hh(n, b):
        while n not in seen and n != 1:
            seen.add(n)
            s = 0
            for i in range(numdigs(n, b)):
                s += ((n / (b**i)) % b)**2
            n = s
        if n == 1:
            return True
        else:
            return False

    seen = set()
    return hh(n, b)

def compute():
    def satisfactory(n, bases):
        r = True
        for b in bases:
            if b != 2 and b != 4:
                r = r and happy(n, b)
        return r
    
    bases = map(int, raw_input().split())

    n = 2
    while not satisfactory(n, bases):
        n += 1
    
    return n


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
