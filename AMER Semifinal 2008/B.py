#!/usr/bin/env python
#
# Problem: Code Sequence
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


MOD = 10007

def compute():
    n = input()
    s = map(int, raw_input().split())
    
    d = [(s[i]-s[i-1])%MOD for i in range(1, n)]
    
    last = 0
    while 1:
        d1 = d[::2]
        d2 = d[1::2]
        if 1 >= len(set(d1)) >= len(set(d2)):
            return "UNKNOWN"
        if len(set(d2)) == 1:
            if len(d)%2 == 1:
                last = d2[0]
                break
            else:
                d = d1
        elif len(set(d1)) == 1:
            if len(d)%2 == 1:
                d = d2
            else:
                last = d1[0]
                break
            
    return str((s[-1] + last)%MOD)

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
