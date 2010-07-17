#!/usr/bin/python
#
# Problem: Minimum Scalar Product
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    nn = input()
    q = map(int, raw_input().split())
    r = map(int, raw_input().split())
    q.sort()
    r.sort()
    v = 0
    for p in range(nn):
	v += q[p] * r[nn-p-1]
    return v


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
