#!/usr/bin/env python
#
# Problem: Ocean View
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n = int(raw_input())
    x = map(int, raw_input().split())

    z = [None]*n
    y = 0
    for i in range(n):
        l = 0
        u = y+1

        while u-l > 1:
            m = (u+l)/2
            if x[z[m-1]] < x[i]:
                l = m
            else:
                u = m

        j = l
        if j == y or x[i] < x[z[j]]:
            z[j] = i
            y = max(y, j+1)

    ans = n-y
    print "Case #%d: %s" % (case+1, ans)
