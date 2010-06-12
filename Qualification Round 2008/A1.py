#!/usr/bin/python
#
# Problem: Saving the Universe
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys

MAX = 1000000000

file = sys.stdin

def switches():
    ns = int(file.readline())

    ses = []
    for j in range(ns):
	ses.append(file.readline()[:-1])

    d = dict()
    d.update(((x,0) for x in ses))

    tot = 0

    nq = int(file.readline())

    qus = []
    for k in range(nq):
	qus.append(file.readline()[:-1])

    cns = 0

    for jj in range(nq):
	check = d.get(qus[jj])
	if check == 0:
	    d.update(((qus[jj],1),))
	    cns += 1
	    if cns >= ns:
		tot += 1
		cns = 0
		d = dict()
		d.update(((x,0) for x in ses))
		d.update(((qus[jj],1),))
		cns = 1
    
    return str(tot)

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += switches()
    print s
