#!/usr/bin/python
#
# Problem: Square Fields
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Takes a long time on large.


from math import *

MAX = 64000

def compute():
    def isclique(s, n, k, p):
        xmax = 0
        ymax = 0
        xmin = MAX
        ymin = MAX
        for i in range(n):
            ca = (s >> i)%2
            if ca == 1:
                j = p[i]
                if j[0] < xmin:
                    xmin = j[0]
                if j[0] > xmax:
                    xmax = j[0]
                if j[1] < ymin:
                    ymin = j[1]
                if j[1] > ymax:
                    ymax = j[1]
            if max(xmax-xmin, ymax-ymin) > k:
                return False
        return True

    def det(s, n, k, p):
        subs = [0]
        numdigs = int(log(s)/log(2))+1
        for i in range(numdigs):
            if (s >> (numdigs-i-1))%2 == 1:
                subs2 = list(subs)
                for j in subs:
                    j <<= 1
                for j in subs2:
                    j <<= 1
                    j += 1
                subs.extend(subs2)
            else:
                for j in subs:
                    j <<= 1
    
        if isclique(s, n, k, p):
            cp[s] = 1

        minp = MAX
        for st in subs[::2]:
            stx = s^st
            if st != s and stx != s:
                if cp[st] >= MAX: # not in table
                    det(st, n, k, p)
                if cp[stx] >= MAX:
                    det(stx, n, k, p)
            minp = min(minp, cp[st]+cp[stx])
    
        cp[s] = min(cp[s], minp)


    n, bound = map(int, raw_input().split())
    p = []
    for i in range(n):
        v=map(int, raw_input().split())
        p.append((v[0], v[1]))
    
    xmax = 0
    ymax = 0
    xmin = MAX
    ymin = MAX
    for i in p:
        if i[0] < xmin:
            xmin = i[0]
        if i[0] > xmax:
            xmax = i[0]
        if i[1] < ymin:
            ymin = i[1]
        if i[1] > ymax:
            ymax = i[1]

    l = 0
    u = max(xmax-xmin, ymax-ymin)

    while l < u:
        k = (l+u)/2        
        cp = [MAX]*(1 << n)
        det((1 << n)-1, n, k, p)
        if cp[(1 << n)-1] <= bound:
            u = k
        else:
            l = k+1
        
    return u

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
