#!/usr/bin/env python
#
# Problem: Pogo
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    x, y = map(int, raw_input().split())

    n = 0
    s = 0
    while s < abs(x)+abs(y) or (s+x+y)%2 == 1:
        n += 1
        s += n
    
    r = ""
    for i in range(1, n+1)[::-1]:
        if abs(x) > abs(y):
            r += "WE"[x>0]
            x -= i*(-1, 1)[x>0]
        else:
            r += "SN"[y>0]
            y -= i*(-1, 1)[y>0]
    
    print "Case #%d: %s" % (case+1, r[::-1])
