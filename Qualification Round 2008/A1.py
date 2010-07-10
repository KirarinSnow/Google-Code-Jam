#!/usr/bin/python
#
# Problem: Saving the Universe
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():    
    ns = input()
    ses = [raw_input() for j in range(ns)]
    nq = input()
    qus = [raw_input() for j in range(nq)]

    d = dict()
    d.update(((x,0) for x in ses))

    tot = 0
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
    
    return tot


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
