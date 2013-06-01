#!/usr/bin/env python
#
# Problem: Many Prizes
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n, p = map(int, raw_input().split())

    a = 0
    b = 0
    x = bin((1<<n)+p-1)[3:]

    y = 0
    k = 2
    while y < len(x) and x[y] == '1':
        y += 1
        a += k
        k *= 2
    if y == len(x):
        a = 2**n-1
    if y == len(x)-1:
        a = 2**n-2       

    k = 1<<n
    j = 1
    while j <= p:
        j *= 2
        k >>= 1
        b += k

    b -= k
    
    ans = ' '.join(map(str, [a, b]))
    print "Case #%d: %s" % (case+1, ans)
