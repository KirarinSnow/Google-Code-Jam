#!/usr/bin/env python
#
# Problem: Bullseye
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import *

for case in range(int(raw_input())):
    r, t = map(int, raw_input().split())

    # quadratic equation?? offset by 1000 to handle precision
    c = max(0, int(ceil(sqrt((2*r+3)**2+8*(t-2*r-1))/4.0-(2*r+3)/4.0))-1000)
    
    # brute-force near the target to get the exact answer
    while 2*c*(c+1) + (2*r+1)*(c+1) <= t:
        c += 1    

    ans = c
    print "Case #%d: %d" % (case+1, ans)
