#!/usr/bin/python
#
# Problem: Shopping Plan
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large set.

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

    # Note: all item lists are represented as integers, where the i-th
    # bit indicates membership of the i-th item in the list if 1, 0 otherwise

    


    ni, ns, pg = grabs()
    items = file.readline().split()
    perish = 0
    
    
    for i in range(ni):
	if '!' in items[i]:
	    items[i] = items[i][:-1]
	    perish += (1<<i)

    itd = dict()
    for i in xrange(ni):
	itd.update(((items[i],i),))


    st = [[]]
    sc = [[0,0]]
    st.extend([[]]*ns)
    sc.extend([[]]*ns)
    sth = [0]
    sth.extend([0]*ns)

    for i in xrange(ns):
	shop = file.readline().split()
	sc[i+1] = map(int,shop[0:2])
	st[i+1] = shop[2:]
	for j in range(len(st[i+1])):
	    st[i+1][j] = st[i+1][j].split(':')
	    st[i+1][j][1] = int(st[i+1][j][1])
	    st[i+1][j][0] = itd.get(st[i+1][j][0])
	    sth[i+1] += (1<<st[i+1][j][0] )

	    
    def dist(x,y,xx,yy):
	return sqrt((x-xx)**2+(y-yy)**2)

    def gss(s1,s2):
	return pg*dist(sc[s1][0],sc[s1][1],sc[s2][0],sc[s2][1])

    gg = []
    for i in xrange(ns+1):
	gg.append([])
	for j in xrange(ns+1):
	    gg[i].append(gss(i,j))



    def gas(s1,s2):
	return gg[s1][s2]





    # remaining items
    remain = 0
    for i in range(ni):
	remain += (1<<i)

    opt = [(0,0,remain,0)]
    visited = {}

    

    minc = MAX

    while len(opt) > 0:

	cur = opt.pop()

	if (cur[1],cur[2]) in visited:
	    ctu = visited.get((cur[1],cur[2]))
	    if cur[0] >= ctu:
		continue
	    else:
		visited.update((((cur[1],cur[2]),cur[0]),))
	else:
	    visited.update((((cur[1],cur[2]),cur[0]),))

	# ignore if current cost is greater than minimum to date
	if cur[0] >= minc:
	    continue

	# home
	if cur[1] == 0:
	    #if no more remaining items, compute min
	    if cur[2]==0:
		minc = min(minc,cur[0])
	    else:
		# otherwise, seek out more stores
		for q in range(1,ns+1):
		    if (sth[q]&cur[2] != 0):
			ccc = cur[0]+gas(0,q)
			if ccc < minc:
			    opt.append((ccc,q,cur[2],0))
	else:
	    for it in st[cur[1]]:
		# if store has some product in list
		if (1<<it[0]) & cur[2] != 0:
		    next = (cur[2])^(1<<it[0])
		    if (1<<it[0])&perish != 0 or cur[3] == 1:
			# if perishable item purchased, cannot go to another store
			opt.append(((cur[0]+it[1]+gas(0,cur[1])),0,next,1))
			if (sth[cur[1]]&next != 0):
			    opt.append(((cur[0]+it[1],cur[1],next,1)))
		    else:
			for ss in range(ns+1):
			    ccc = cur[0]+it[1]+gas(ss,cur[1])
			    if ccc < minc:
				opt.append((ccc,ss,next,0))
		    
    return '%(#)0.7f' % {'#' : minc}


file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
