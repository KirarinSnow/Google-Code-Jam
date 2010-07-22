#!/usr/bin/python
#
# Problem: Portal
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():

    def check(i,j):
        return i >= 0 and j >= 0 and i < r and j < c and room[i][j] != '#' 

    r, c = map(int, raw_input().split())

    room  = [raw_input() for i in range(r)]

    source = -1
    cake = -1
    noportal = [-1, -1]

    for i in range(r):
        for j in range(c):
            if room[i][j] != '#':
                if room[i][j] == 'O':
                    source = [[i, j], noportal]
                if room[i][j] == 'X':
                    cake = [[i, j], noportal]

    nodes = [[-2, 0], source]
    vis = []
    dist = 0

    while len(nodes) > 0:
        
        currentp = nodes.pop(0)
        
        if currentp[0] == -2:
            dist = currentp[1]
            continue

        vis.append(currentp)
        current = [currentp[0][0], currentp[0][1]]
        portal = currentp[1]

        if current == cake[0]:
            return str(dist)
        ck = [noportal, portal]

        for z in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            zz = [current[0], current[1]]
            while check(zz[0]+z[0], zz[1]+z[1]):
                zz[0] += z[0]
                zz[1] += z[1]
            if zz not in ck and zz != current:
                ck.append(zz)
   
        nodes.append([-2, dist+1])
        for z in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            dest = [z[0]+current[0], z[1]+current[1]]
            if check(dest[0], dest[1]):
                for i in range(len(ck)):
                    if [dest, ck[i]] not in vis and [dest, ck[i]] not in nodes:
                        nodes.append([dest, ck[i]])

        p = 0
        for z in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            if not check(z[0]+current[0], z[1]+current[1]):
                p += 1
        if p > 0:
            for i in range(len(ck)):
                if [ck[i], noportal] not in vis and \
                        [ck[i], noportal] not in nodes and ck[i] != noportal:
                    nodes.append([ck[i],noportal])

    return "THE CAKE IS A LIE"


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
