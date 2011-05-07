#!/usr/bin/python
#
# Problem: Magicka
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    x = raw_input().split()
    cc = int(x[0])
    cs = x[1:cc+1]
    oc = int(x[cc+1])
    os = x[cc+2:cc+oc+2]
    invoke = x[-1]

    combine = {}
    for j in cs:
        combine[(j[0], j[1])] = j[2]
        combine[(j[1], j[0])] = j[2]
    
    opposed = {}
    for j in os:
        if j[0] not in opposed:
            opposed[j[0]] = set()
        opposed[j[0]].add(j[1])
        if j[1] not in opposed:
            opposed[j[1]] = set()
        opposed[j[1]].add(j[0])
       
    el = []
    for e in invoke:
        if len(el) > 0 and (e, el[-1]) in combine:
            el.append(combine[(e, el.pop())])
        elif e in opposed and len(opposed[e].intersection(el)) > 0:
            el = []
        else:
            el.append(e)
    
    return ', '.join(el)

for i in range(input()):
    print "Case #%d: [%s]" % (i+1, compute())
