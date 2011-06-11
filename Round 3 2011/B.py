#!/usr/bin/python
#
# Problem: Dire Straights
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    s = map(int, raw_input().split())
    n = s.pop(0)

    if n == 0:
        return 0
    else:
        u = n+1
        l = 1
        s.sort()
        h = [0]*10001
        for i in s:
            h[i] += 1
        a = []
        for i in range(1, len(h)):
            if h[i] > h[i-1]:
                a.extend([i]*(h[i]-h[i-1]))

        while u - l > 1:
            m = (u+l)/2
            hh = list(h)
            for x in a:
                for i in range(x, x+m):
                    if i > 10000 or hh[i] <= 0:
                        break
                    else:
                        hh[i] -= 1
                else:
                    continue
                u = m
                break
            else:
                l = m                    
        return l
        
        
for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
