#!/usr/bin/python
#
# Problem: Hall of Mirrors
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Works only on small input.


from fractions import gcd

def sqdist(i, j):
    return (i-R)**2 + (j-C)**2

def update(ii, jj, dist):
    g = abs(gcd(ii, jj))
    i = ii/g
    j = jj/g
    print (i, j), 
    sd.add((i, j))

for case in range(int(raw_input())):
    h, w, d = map(int, raw_input().split())
    b = [raw_input() for i in range(h)]
    
    r = 0
    c = 0
    for i in range(h):
        for j in range(w):
            if b[i][j] == 'X':
                r = i
                c = j

    R = 2*(r-1)+1
    C = 2*(c-1)+1
    W = 2*(w-2)
    H = 2*(h-2)
    D = 2*d

    mc = -D/W-1
    Mc = D/W+2
    mr = -D/H-1
    Mr = D/H+2

    sd = set()

    corners = set()
    
    for i in range(mr+1, Mr):
        for j in range(mc+1, Mc):
            corners.add((i*H, j*W))
    
    reflections = set()
    for i in range(mr, Mr):
        for j in range(mc, Mc):
            ar = (R, H-R)[i%2]
            ac = (C, W-C)[j%2]
            reflections.add((i*H+ar, j*W+ac))

    for i, j in corners:
        rd = i - R
        cd = j - C
        dist = 4*sqdist(i, j)
        if dist <= D*D:
            update(rd, cd, dist)
 
    
    for i, j in reflections:
        rd = i - R
        cd = j - C
        dist = sqdist(i, j)
        if (i, j) != (R, C) and dist <= D*D:
            update(rd, cd, dist)


    print "Case #%d: %d" % (case+1, len(sd))
