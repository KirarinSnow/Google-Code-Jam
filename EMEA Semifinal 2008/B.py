#!/usr/bin/env python
#
# Problem: Painting a Fence
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from itertools import *

MAX = 9999999999999

def compute():
    n = input()
    p = [raw_input().split() for i in range(n)]

    # Dummy color names for n <= 2 cases
    if n < 3:
        p.append(['Pyon Pyon', p[0][1], p[0][2]])
        p.append(['S/mileage', p[0][1], p[0][2]])

    s = map(lambda x: [int(x[1]), x[0], int(x[1]), int(x[2])], p)
    sf = sorted(s)

    colors = set(map(lambda x: x[1], s))

    cs = {}
    for cc in colors:
        cs[cc] = filter(lambda x: x[1] == cc, sf)
    
    m = MAX
    for c in combinations(colors, 3):
        v = map(lambda x: cs[x], c)
        v = sorted(sum(v, []))
        
        z = 0
        y = 0
        o = 0
        j = 1
        while j <= 10000:
            if z >= len(v) or v[z][2] > j:
                break

            else:
                while z < len(v) and v[z][2] <= j:
                    y = max(y, v[z][3])
                    z += 1

                j = y + 1
                o += 1

        else:
            m = min(m, o)
            continue

    if m == MAX:
        return "IMPOSSIBLE"
    else:
        return str(m)

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
