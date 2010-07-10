#!/usr/bin/python
#
# Problem: Saving the Universe
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Inefficient O(SQ)-time algorithm. Can be solved in O(S+Q) time.


MAX = 1000000000

def compute():
    ns = input()
    ses = [raw_input() for j in range(ns)]
    nq = input()
    qus = [raw_input() for j in range(nq)]

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
	return 0

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

    return scc

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
