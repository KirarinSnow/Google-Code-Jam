#!/usr/bin/python
#
# Problem: Technology Planning
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def visit(k):
    if k not in v:
        v.add(k)
        for x, y in d:
            if x == k:
                visit(y)
        l.append(k)

for i in range(int(raw_input())):
    m = int(raw_input())
    d = [raw_input().split(':') for j in range(m)]
    q = int(raw_input())
    g = [raw_input() for j in range(q)]

    z = []
    v = set()

    o = {}
    
    z = map(lambda x: (x, True), g)
    while z:
        k, e = z.pop(0)
        if k not in o:
            for x, y in d:
                if x == k:
                    z.append((y, False))
        o[k] = e

    z = filter(lambda y: o[y], o)

    l = []
    for zz in z:
        visit(zz)
 
    n = len(l)
    
    print "Case #%d: %s" % (i+1, n)
    print '\n'.join(l)
