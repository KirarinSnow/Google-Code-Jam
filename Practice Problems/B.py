#!/usr/bin/python
#
# Problem: Always Turn Left
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for i in range(input()):
    s = raw_input()
    c = 0
    r = 0
    fc = 0
    fr = 0
    dir = 0
    maxc = 0
    minc = 0
    maxr = 0
    minr = 0
    voff= 0
    hoff = 0
    exdir = 0
    for si in range(len(s)-1):
        ch = s[si]
        nt = s[si+1]
        if ch == ' ':
            fc = c
            fr = r
            exdir = dir
            dir = (dir+2)%4
            if dir %2 == 0:
                voff += 1
            else:
                hoff +=1
        else:
            if ch == 'W':
                if dir == 0:
                    r += 1
                if dir == 1:
                    c+=1
                if dir == 2:
                    r -= 1
                if dir == 3:
                    c -= 1
            if ch == 'R':
                dir = (dir + 1)%4
            if ch == 'L':
                dir = (dir - 1)%4

            if nt == 'W' or nt == 'R' or nt == 'L':
                if c > maxc:
                    maxc = c
                if c < minc:
                    minc = c
                if r > maxr:
                    maxr = r
                if r < minr:
                    minr = r

    width = maxc - minc +1
    height = maxr - minr 

    sr = 0
    sc = -minc
    
    m = []
    mm = []
    mmm = []
    for iii in range(height):
        m.append([])
        mm.append([])
        mmm.append([])
        for jjj in range(width):
            m[iii].append(['.','.','.','.'])
            mm[iii].append(0)
            mmm[iii].append(0)

    c = sc
    r = sr -1
    dir = 0
    t = 0
    oc = 'W'
    for ch in s:
        if 0 <= r < height and 0 <= c < width :
            if ch == 'W':
                m[r][c][dir%4] = 'o'
                if oc == 'R' or oc == 'W':
                    m[r][c][(dir+3)%4] = 'x'
            if ch == 'L':
                m[r][c][(dir+3)%4] = 'o'
            if ch == 'R':
                m[r][c][dir%4] = 'x'
                m[r][c][(dir+3)%4] = 'x'

        if ch == 'W':
            if dir == 0:
                r += 1
            if dir == 1:
                c += 1
            if dir == 2:
                r -= 1
            if dir == 3:
                c -= 1
        if ch == 'R':
            dir = (dir+1)%4
        if ch == 'L':
            dir = (dir-1)%4
        if ch == ' ':
            t = 1
            dir = (dir+2)%4
        oc = ch

    for iiii in range(height):
        for jjjj in range(width):
            if m[iiii][jjjj][2] == 'o':
                mm[iiii][jjjj]+=1
            if m[iiii][jjjj][0] == 'o':
                mm[iiii][jjjj]+=2
            if m[iiii][jjjj][1] == 'o':
                mm[iiii][jjjj]+=4
            if m[iiii][jjjj][3] == 'o':
                mm[iiii][jjjj]+=8 
            if mm[iiii][jjjj] <= 9:
                mmm[iiii][jjjj] = str(mm[iiii][jjjj])
            else:
                mmm[iiii][jjjj] = chr(mm[iiii][jjjj]-10+ord('a'))
    
    print "Case #%d:" % (i+1)
    
    for xx in range(height):
        print ''.join([mmm[xx][width-yy-1] for yy in range(width)])
