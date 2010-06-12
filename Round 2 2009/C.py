#!/usr/bin/python
#
# Problem: Stock Charts
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Uses a randomized approach. Probably works on small set; probably
#           doesn't work on large set.

import sys
from math import *
from string import *
from random import *


def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def next():
    return buffer.pop(0)

def nint():
    return int(next())

def cp(a,b):
    return (len(a)*[True] == map(lambda x,y: x>y, a,b)) \
        or (len(a)*[True] == map(lambda x,y: x<y, a,b))

def compute():
    n, k = nint(), nint()

    pr = []
    for i in range(n):
        pr.append([])
        for j in range(k):
            pr[i].append(nint())

    g = []
    for i in range(n):
        g.append([])
        for j in range(n):
            g[i].append(False)

    for i in range(n):
        for j in range(i+1,n):
            if cp(pr[i],pr[j]):
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

file = sys.stdin

case = int(file.readline())
buffer = file.read().split()

for i in range(case):
    print "Case #" + str(i+1) + ":",
    print compute()
