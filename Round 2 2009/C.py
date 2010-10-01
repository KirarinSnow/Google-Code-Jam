#!/usr/bin/python
#
# Problem: Stock Charts
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Uses a randomized approach. Probably works on small set; probably
#           doesn't work on large set.

from random import *


def cp(a,b):
    return (len(a)*[True] == map(lambda x,y: x>y, a,b)) \
        or (len(a)*[True] == map(lambda x,y: x<y, a,b))

def compute():
    n, k = map(int, raw_input().split())

    pr = [map(int, raw_input().split()) for i in range(n)]

    g = []
    for i in range(n):
        g.append([])
        for j in range(n):
            g[i].append(False)

    for i in range(n):
        for j in range(i+1, n):
            if cp(pr[i], pr[j]):
                g[i][j] = True
                g[j][i] = True


    pp = range(n)
    cc = 88888888888

    # random permutation ... :(
    for t in range(1000):
        shuffle(pp)

        c = 0
        q = []
        for i in pp:
            added = False
            for s in q:
                for j in s:
                    if not g[i][j]:
                        break
                else: # matches all in set
                    s.add(i)
                    added = True
                    break

            if not added:
                q.append(set([i]))
        cc = min(cc, len(q))

    return cc

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
