#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 문제: 새로운 달력
# 언어: Python
# 저자: KirarinSnow
# 사용: python thisfile.py <input.in >output.out


for case in range(1, input()+1):
    n, m, w = map(int, raw_input().split())
    
    s = {}
    u = {}
    d = 0
    t = 0
    f = None
    i = 0
    while i < n:
        t += (m+d-1)/w+1
        d = (m+d)%w
        if d not in s:
            s[d] = i
            u[d] = t
        else:
            f = i-s[d]
            g = t-u[d]
            break
        i += 1
            
    if f != None:
        r = n-i-1
        t += g*(r/f)
        for i in range(r%f):
            t += (m+d-1)/w+1
            d = (m+d)%w
    ans = t

    print "Case #%d: %d" % (case, ans)
