#!/usr/bin/env python
#
# Problem: Mixing Bowls
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def s(m, r):
        if m in r:
            return r[m]
        
        if len(a[m]) == 0:
            r[m] = 1
        else:
            b = map(lambda x: s(x, r), a[m])
            b.sort()
            b = b[::-1]
            
            r[m] = max(len(b)+1, max(map(lambda x: x+b[x], range(len(b)))))
            
        return r[m]
        
    n = input()
    a = dict()
    r = dict()
    for i in range(n):
        v = raw_input().split()
        if i == 0:
            q = v[0]
        a[v[0]] = filter(lambda x: 'A' <= x <= 'Z', v[2:])

    return s(q, r)


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
