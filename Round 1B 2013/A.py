#!/usr/bin/env python
#
# Problem: Osmos
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    a, n = map(int, raw_input().split())
    m = map(int, raw_input().split())
    m.sort()

    b = len(m)
    i = 0
    p = 0
    while len(m) > 0:
        if m[0] < a:
            a += m.pop(0)
            i = 0
            b = min(b, p+len(m))
        else:
            if i > len(m):
                b = min(b, p-i+len(m)) 
                break
            else:
                i += 1
                p += 1
                a += a-1

    ans = b 
    print "Case #%d: %s" % (case+1, ans)
