#!/usr/bin/env python
#
# Problem: Safety in Numbers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    s = map(int, raw_input().split())
    n = s.pop(0)
    x = sum(s)

    a = []
    for i in range(n):
        r = []
        for j in range(n):
            if i != j:
                r.append(s[j])
        r.sort()
        
        t = 0
        M = 100
        for k in range(len(r)):
            t += r[k]
            m = (s[i]*(k+1)-t-x)*1.0/(-(k+2)*x)
            M = min(m, M)
            
        a.append(max(0, M)*100)
    
    ans = ' '.join(map(str, a))

    print "Case #%d: %s" % (case+1, ans)
