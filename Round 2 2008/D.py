#!/usr/bin/python
#
# Problem: PermRLE
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Fails on large set.


from itertools import *


def compute():

    def ct(ii):
	ctt = 0
	tabl[ii].append(0)
	for r in range(len(tabl[0])-1):
	    if tabl[ii][r]!=tabl[ii][r+1]:
		ctt+=1
	return ctt

    k = input()
    ss = raw_input()
    ll = len(ss)
    nn = ll/k
    ps = []
    for j in permutations(range(k)):
	ps.append(j)

    tabl = []
    for i in range(len(ps)):
	tabl.append([])
	perm = ps[i]
	for j in range(nn):
	    subs = ss[j*k:j*k+k]
	    for jj in range(k):
		tabl[i].append(subs[perm[jj]])

    cc = 1000000000000

    x = len(ps)
    for i in range(x):
	cc = min(cc, ct(i))

    return cc


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
