#!/usr/bin/env python
#
# Problem: Travel Plan
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n = int(raw_input())
    x = map(int, raw_input().split())
    f = int(raw_input())
    
    x.sort()

    if 2*(x[n-1]-x[0]) > f:
        ans = "NO SOLUTION"
    else:
        n1 = n/2
        n2 = n-n1
        x1 = x[:n1]
        x2 = x[n1:][::-1]
 
        ans = -1
        for v in range(2, 2*n1+2, 2):
            s = []
            a = []
            for p in range(2):
                ni = (n1, n2)[p]
                y = (x1, x2)[p]
                
                s.append(set())
                k = [(0, 2)]
                for i in range(1, ni):
                    kk = []
                    for t, w in k:
                        if abs(w-v) <= 2*(ni-i):
                            tt = t+w*abs(y[i]-y[i-1])
                            for ww in range(max(2, w-2), w+4, 2):
                                kk.append((tt, ww))
                    k = kk
                for t, w in k:
                    s[-1].add(t)
                a.append(sorted(list(s[-1])))
            
            h = v*(x2[n2-1]-x1[n1-1])

            for r in a[0]:
                l = 0
                u = len(a[1])
                while l < u-1:
                    m = (l+u)/2
                    z = r+a[1][m]+h
                    if z > f:
                        u = m
                    else:
                        l = m
                c = r+a[1][l]+h
                if c <= f:
                    ans = max(ans, c)
    
    print "Case #%d: %s" % (case+1, ans)
