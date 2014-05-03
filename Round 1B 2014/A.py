#!/usr/bin/env python
#
# Problem: The Repeater
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n = int(raw_input())
    z = [raw_input() for i in range(n)]

    p = True

    a = []
    b = []
    for i in range(n):
        a.append([])
        b.append([])
        for j, c in enumerate(z[i]):
            if j == 0 or c != a[i][-1][0]:
                a[i].append([c, 1])
                b[i].append(c)
            else:
                a[i][-1][1] += 1
        if i > 0 and b[i] != b[i-1]:
            p = False
            ans = "Fegla Won"
            break

    if p:
        s = 0
        t = zip(*a)
        for u in t:
            m = 1<<32
            for k in range(1, 101):
                m = min(m, sum(map(lambda x: abs(k-x[1]), u)))
            s += m
        ans = s
    
    print "Case #%d: %s" % (case+1, ans)
