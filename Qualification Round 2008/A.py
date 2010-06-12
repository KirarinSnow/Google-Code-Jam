#!/usr/bin/python
#
# Problem: Saving the Universe
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Inefficient O(SQ)-time algorithm. Can be solved in O(S+Q) time.

import sys

MAX = 1000000000

file = sys.stdin

def switches():
    ns = int(file.readline())

    ses = []
    for j in range(ns):
	ses.append(file.readline()[:-1])

    nq = int(file.readline())

    qus = []
    for k in range(nq):
	qus.append(file.readline()[:-1])

    table = []
    for jj in range(nq):
	table.append([])
	for kk in range(ns):
	    if qus[jj] == ses[kk]:
		conf = 1
	    else:
		conf = 0
	    table[jj].append(conf)

    if nq == 0:
	return "0"
    score = [[]]
    for m in range(ns):
	score[0].append(table[0][m])
    
    for v in range(1,nq):
	score.append([])
	for x in range(ns):
	    if table[v][x] == 1:
		score[v].append(MAX)
		
	    else:
		cc = MAX
		for p in range(ns):
		    if p == x:
			ad = 0
		    else:
			ad = 1
		    cc = min(cc, score[v-1][p] +ad)
		score[v].append(cc)

    scc = MAX
    for kkk in range(ns):
	scc = min(scc,score[nq-1][kkk])

    return str(scc)

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += switches()
    print s
