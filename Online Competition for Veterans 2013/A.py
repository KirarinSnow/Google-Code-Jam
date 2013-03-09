#!/usr/bin/env python
#
# Problem: Hedgemony
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n = int(raw_input())
    l = map(int, raw_input().split())

    for i in range(1, n-1):
        t = (l[i-1]+l[i+1])/2.0
        if t < l[i]:
            l[i] = t
    
    ans = l[n-2]
    
    print "Case #%d: %f" % (case+1, ans)
