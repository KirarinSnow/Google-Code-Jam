#!/usr/bin/python
#
# Problem: Polygraph
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    n, m = map(int, raw_input().split())
    p = [raw_input().split() for x in range(m)]
    a = [0]*m
    for i, l in enumerate(p):
        v = map(int, [l[0]] + l[2:])
        for j in v:
            a[i] ^= 1 << j
        if l[1] == 'S' or l[1] == 'L':
            a[i] ^= 1

    for j in range(1, n+1):
        f = filter(lambda x: (x >> j) % 2 == 1 and x & ((1 << j) - 2) == 0, a)
        if len(f) > 0:
            s = f[0]
            a = map(lambda x: x ^ (0, s)[x != s and (x >> j) % 2 == 1], a)
          
    a.sort()
    v = ['-']*n
    x = 1
    c = 0
    while len(a) > 0:
        while x < a[0]/2:
            x *= 2
            c += 1
        z = a.pop(0)

        if z/2 == x:
            v[c] = ('L', 'T')[z%2]

    return ' '.join(v)


for i in range(int(raw_input())):
    print "Case #%d: %s" % (i+1, compute())
