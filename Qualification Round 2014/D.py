#!/usr/bin/env python
#
# Problem: Deceitful War
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compare(l, p):
    s = 0
    m = 0
    for x, y in l:
        s += [1, -1][y == p]
        m = max(m, s)
    return m
        

for case in range(int(raw_input())):
    n = int(raw_input())
    N = zip(*[map(float, raw_input().split()), [0]*n])
    K = zip(*[map(float, raw_input().split()), [1]*n])
    C = sorted(N+K)
    
    w = compare(C, 0)
    d = n-compare(C, 1)

    print "Case #%d: %d %d" % (case+1, d, w)
