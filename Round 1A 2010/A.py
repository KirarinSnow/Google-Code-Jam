#!/usr/bin/python
#
# Problem: Rotate
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    n, k = map(int, raw_input().split())
    c = []
    for i in range(n):
        c.append(list(raw_input()))

    # rotate
    for i in range(n):
        e = n-1
        while e >= 0 and c[i][e] != '.':
            e -= 1
        p = e-1
        while p >= 0:
            if c[i][p] != '.':
                c[i][e] = c[i][p]
                c[i][p] = '.'
                e -= 1
            p -= 1

    rwin = False
    bwin = False

    
    # count maxR, maxB per row
    for i in range(n):
        cR = 0
        cB = 0
        for j in range(n):
            if c[i][j] == 'R':
                cR+=1
                cB=0
            elif c[i][j] == 'B':
                cB+=1
                cR=0
            else:
                cB = 0
                cR = 0
            if cR >= k:
                rwin = True
            if cB >= k:
                bwin = True
                
     # count maxR, maxB per col
    for i in range(n):
        cR = 0
        cB = 0
        for j in range(n):
            if c[j][i] == 'R':
                cR+=1
                cB=0
            elif c[j][i] == 'B':
                cB+=1
                cR=0
            else:
                cB = 0
                cR = 0
            if cR >= k:
                rwin = True
            if cB >= k:
                bwin = True
    
    # count maxR, maxB per diag
    for i in range(-n+1,n):
        cR = 0
        cB = 0
        for j in range(n):
            ii = j + i
            if ii < 0 or ii >= n:
                continue
            if c[ii][j] == 'R':
                cR+=1
                cB=0
            elif c[ii][j] == 'B':
                cB+=1
                cR=0
            else:
                cB = 0
                cR = 0
            if cR >= k:
                rwin = True
            if cB >= k:
                bwin = True

    # count maxR, maxB per inverse diag
    for i in range(2*n-1):
        cR = 0
        cB = 0
        for j in range(n):
            ii = i-j
            if ii < 0 or ii >= n:
                continue
            if c[ii][j] == 'R':
                cR+=1
                cB=0
            elif c[ii][j] == 'B':
                cB+=1
                cR=0
            else:
                cB = 0
                cR = 0
            if cR >= k:
                rwin = True
            if cB >= k:
                bwin = True
    

    
    if rwin and bwin:
        result = 'Both'
    elif rwin:
        result = 'Red'
    elif bwin:
        result = 'Blue'
    else:
        result = 'Neither'
        
    return result

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
