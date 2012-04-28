#!/usr/bin/env python
#
# Problem: Password Problem
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    p = map(float, raw_input().split())
    
    m = b + 2
    pr = [1]
    for i in range(a):
        pr.append(pr[i]*p[i])

    for i in range(a+1):
        pg = pr[a-i]
        exg = b-a+2*i+1
        exb = 2*b+2*i-a+2
        m = min(m, pg*exg + (1-pg)*exb)
    ans = m
    
    print "Case #%d: %0.6f" % (case+1, ans)
