#!/usr/bin/python
#
# Problem: Milkshakes
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def check():
	for i in range(len(table)):
	    p = 0
	    if table[i] == 1:
		continue
	    if table[i] == 0:
		return -2
	    if len(table[i]) == 0:
		return -3
	    cc = 0
	    for c in range(len(table[i])):
		if table[i][c] != 0:
		    cc += 1
		    p = c
	    if cc == 0:
		return -4
	    if len(table[i]) == 1 and table[i][0][1] == 1:
		return i
	    if cc == 1 and table[i][p][1] == 1:
		return i
	return -1

    n = input()
    m = input()

    table = []
    r = [0] * n
    
    for i in range(m):
	table.append([])
	g = map(int, raw_input().split())
	t = g[0]
	for j in range(t):
	    table[i].append([g[2*j+1],g[2*j+2]])
    
    q = check()
    while q >= 0:
	qq = 0
	while table[q][qq] == 0:
	    qq+=1

	fl = table[q][qq][0]
	r[fl-1] = 1
	for k in range(len(table)):
	    if table[k] == 0 or table[k] <= 2:
		continue
	    else:
		for kk in range(len(table[k])):
		    if table[k] <= 2:
			continue
		    if table[k][kk] == 0:
			continue
		    if (table[k][kk][0] == fl and table[k][kk][1] == 1):
			table[k] = 1
		    elif (table[k][kk][0] == fl and table[k][kk][1] == 0):
			table[k][kk] = 0
	q = check()

    if q < -1:
	return "IMPOSSIBLE"
    else:
	return ' '.join(map(str, r))

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
