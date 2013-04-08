#!/usr/bin/pypy
#
# Problem: Make it Smooth
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out


MAX = 1<<32

def cost(k, v):
    if (k, v) not in c:
        if k < 0:
            c[(k, v)] = 0
        else:
            t = d + cost(k-1, v)

            o = abs(s[k]-v)
            if m > 0:
                for u in range(256):
                    if t <= o:
                            break
                    t = min(t, cost(k-1, u) + o + max(0, abs(v-u)-1)/m*i)
            else:
                t = min(t, cost(k-1, v) + o)
 
            c[(k, v)] = t           

    return c[(k, v)]

for case in range(int(raw_input())):
    d, i, m, n = map(int, raw_input().split())
    s = map(int, raw_input().split())

    c = {}
    ans = min([cost(n-1, v) for v in range(256)])

    print "Case #%d: %s" % (case+1, ans)
