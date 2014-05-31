#!/usr/bin/env pypy
#
# Problem: Trie Sharding
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out


from itertools import *

def total(w):
    s = set()
    for x in w:
        for j in range(len(x)+1):
            s.add(x[:j])
    return len(s)

for case in range(int(raw_input())):
    m, n = map(int, raw_input().split())
    s = [raw_input() for i in range(m)]

    mm = 0
    ww = 0
    for c in range(n**m):
        k = [[] for j in range(n)]
        for i in range(m):
            a = (c/(n**i))%n
            k[a].append(s[i])
        t = 0
        for j in range(n):
            t += total(k[j])
        if t > mm:
            ww = 1
            mm = t
        elif t == mm:
            ww += 1

    ans = ' '.join(map(str, (mm, ww)))
    
    print "Case #%d: %s" % (case+1, ans)
