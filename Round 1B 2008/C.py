#!/usr/bin/python
#
# Problem: Mousetrap
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large set.


def compute():
    k = input()
    r = map(int, raw_input().split())
    n = r.pop(0)
    sn = range(k)
    a = [0]*k
    c = 0
    i = 1
    cc = 0
    p=0
    dexp = range(k)
    dex = sorted(dexp)
    while i <=k:
	rd = k-i+1
	
	v = (p+i-1)%rd
	a[dex[v]] = i
	p = dex.index(dex[v])
	del dex[v]
	i = i+1

    return ' '.join(map(str, [a[j-1] for j in r]))


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
