#!/usr/bin/python
#
# Problem: A Digging Problem
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from heapq import *

MAX = 1<<30

def compute():
    def bottom(x, y):
        b = x+1
        while b < r and g[b][y] == '.':
            b += 1
        return b-1
    def lim(y, p):
        if p > 0:
            return y < c-1
        else:
            return y > 0

    r, c, f = map(int, raw_input().split())
    g = [raw_input() for i in range(r)]
    q = []
    d = {}
    t = MAX

    heappush(q, [0, (0, 0, 0, '', None)])

    while q:
        z, u = heappop(q)
        if u in d:
            continue
        d[u] = z

        if z > t:
            break

        x, y, m, el, er = u
        if x == r-1: # bottom
            t = min(t, z)
        else:
            if m == 0: # moving mode
                for p in (-1, 1):
                    if lim(y, p) and (g[x][y+p] == '.' or (el <= y+p <= er)):
                        h = bottom(x, y+p)
                        if 0 < h-x <= f:
                            heappush(q, [z, (h, y+p, 0, '', None)]) # fall
                        elif h == x:
                            heappush(q, [z, (x, y+p, 0, el, er)]) # move
                            if p < 0:
                                heappush(q, [z+1, (x, y, p, y+p, er)]) # dig
                            else:
                                heappush(q, [z+1, (x, y, p, el, y+p)]) # dig
            else: # digging mode
                if lim(y, -m) and (g[x][y-m] == '.' or (el <= y-m <= er)):
                    if g[x+1][y-m] != '.':
                        heappush(q, [z+1, (x, y-m, m, el, er)]) # continue dig
                h = bottom(x+1, y+m)
                if h-x <= f:
                    if h-x == 1:
                        if m < 0:
                            heappush(q, [z, (x+1, y+m, 0, el, y+m)]) # fall 1
                        else:
                            heappush(q, [z, (x+1, y+m, 0, y+m, er)]) # fall 1
                    else:
                        heappush(q, [z, (h, y+m, 0, '', None)]) # fall >1

    return "No" if t == MAX else "Yes %d" % t
    

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
