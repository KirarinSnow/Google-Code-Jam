#!/usr/bin/python
#
# Problem: The Price is Wrong
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys
from math import *
from string import *

MAX = 100000000000


def grab():
    return int(file.readline())

def grabs():
    return map(int,file.readline().split())

def removechars(str, chars):
    return str.translate(maketrans('',''),chars)

def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():

    def rep(prefix, q, can, prev):
        if len(q) == 0:
            can.append(prefix)
            return
        else:
            for i in q:
                if prev[i] == q:
                    rep(prefix+[i], [], can, prev)
                else:
                    rep(prefix+[i], prev[i], can, prev)

    def lcs(a, n, prods):
        max = -1
        best = []
        prev = []
        for i in xrange(n):
            best.append(1)
            prev.append([i])

        for i in xrange(1,n):
            for j in range(i):
                if a[i] > a[j] and best[i] <= best[j] + 1:
                    if best[i] < best[j] + 1:
                        best[i] = best[j] + 1
                        prev[i] = [j]
                    else:
                        prev[i].append(j)
                   
        end = [0]
        for i in xrange(n):
            if max <= best[i]:
                if max < best[i]:
                    max = best[i]
                    end = [i]
                else: 
                    end.append(i)

        candidates = []
        queue = []

        rep([], end, candidates, prev)

        return candidates

    ret = []

    prods = file.readline().split()

    vals = grabs()

    assoc = []
    for i in range(len(vals)):
        assoc.append([vals[i],i])

    assoc.sort()

    assoc2 = map(lambda x: [x[1],x[0],0], assoc)
    for i in range(len(assoc2)):
        assoc2[i][2] = i
    
    assoc2.sort()
        
    lt = map(lambda x: x[2], assoc2)

    lc = lcs(lt, len(lt), prods)

    for k in range(len(lc)):
        ret.append([])
        for i in xrange(len(lt)):
            if i not in lc[k]:
                ret[k].append(prods[i])

        ret[k].sort()
        ret[k] = ' '.join(ret[k])

    ret.sort()
    return ret[0]
            

file = sys.stdin

n = int(file.readline())

for i in range(n):

    print "Case #" + str(i+1) + ":",
    print compute()
