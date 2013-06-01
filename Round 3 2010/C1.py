#!/usr/bin/env python
#
# Problem: Hot Dog Proliferation
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Implementation of O(C) H-segment solution in contest analysis.


from math import *

for case in range(int(raw_input())):
    c = int(raw_input())
    h = sorted([map(int, raw_input().split()) for i in range(c)])

    s = []
    q = 0
    for p, m in h:
        p += 2*10**7 # adjust negatives
        q -= m*p*p
        x, y, z = (p-m/2, [p, p+m/2+1][m%2], p+m/2+m%2)
        s.append((x, y, z))

        while len(s) > 1:
            if s[-2][2] < s[-1][0]: # if no overlap
                break

            # compute merger
            x, y, z = s.pop()
            u, v, w = s.pop()

            t = z*(z+1)/2-x*(x-1)/2+w*(w+1)/2-u*(u-1)/2-y-v
            k = z-x+w-u

            nx = int(floor(t*2.0/k+1-k)/2.0)
            nz = nx+k
            ny = nz*(nz+1)/2-nx*(nx-1)/2-t

            s.append((nx, ny, nz))

    # compute change in sum of squared positions
    for x, y, z in s:
        q += z*(z+1)*(2*z+1)/6-x*(x-1)*(2*x-1)/6-y*y

    ans = q/2

    print "Case #%d: %s" % (case+1, ans)
