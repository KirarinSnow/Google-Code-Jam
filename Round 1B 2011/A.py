#!/usr/bin/python
#
# Problem: RPI
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    n = input()
    t = [raw_input() for i in range(n)]
    w = []
    wx = []
    for x in range(n):
        w.append(len(filter(lambda c: c == '1', t[x]))*1.0 / 
                 len(filter(lambda c: c != '.', t[x])))
        
        p = []
        for y in range(n):
            if t[x][y] != '.':
                u = 0
                v = 0
            
                for z in range(n):
                    if z!=x:
                        if t[y][z] == '1':
                            u += 1
                        if t[y][z] != '.':
                            v += 1
                p.append(u*1.0/v)
        wx.append(sum(p)/len(p))
    
    wy = []
    for x in range(n):
        p = []
        for y in range(n):
            if t[x][y] != '.':
                p.append(wx[y])
        wy.append(sum(p)/len(p))

    for x in range(n):
        print 0.25*w[x] + 0.5*wx[x] + 0.25*wy[x]

for i in range(input()):
    print "Case #%d:" % (i+1)
    compute()
