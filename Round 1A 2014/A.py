#!/usr/bin/env python
#
# Problem: Charging Chaos
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


MAX = 1<<32

for case in range(int(raw_input())):
    n, l = map(int, raw_input().split())
    o = map(lambda x: eval("0b"+x), raw_input().split())
    d = map(lambda x: eval("0b"+x), raw_input().split())
 
    c = MAX
    for i in range(n):
        x = d[i]^o[0]
        s = [x^o[j] for j in range(n)]
        if set(s) == set(d):
            c = min(c, bin(x).count('1'))
 
    ans = c if c < MAX else "NOT POSSIBLE"
        
    print "Case #%d: %s" % (case+1, ans)
