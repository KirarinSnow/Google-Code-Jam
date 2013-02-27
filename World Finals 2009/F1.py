#!/usr/bin/python
#
# Problem: Lights
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: I have finally cracked this problem. This version solves both
#           small and large inputs, and manages to do it in about 15 seconds
#           for the large input, compared to the 6 minutes taken by GCJ 2009
#           champion ACRush's C++ solution. I had more time to prepare this
#           though, so this is not a fair comparison. The code also generates
#           PostScript documents depicting the room layout for each test case.
#           This was initially for debugging purposes, but the graphical output
#           looks nice and makes the underlying algorithm quite clear, so I
#           have left it in.


from math import *


MAX = 1<<20
ERR = 1e-12
ERR2 = 20*ERR

def compute(case):
    def norm(a):
        return a%(2*pi)
        
    def offset(d, k):
        return asin(k/d)

    def center(ii, jj, i, j):
        return atan2(i-ii, j-jj)
   
    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

    def coord(lx, ly, a, d):
        return (lx+d*sin(a), ly+d*cos(a))

    def intm(m):
        il = []
        for pk, (cx, cy, cr) in enumerate(p):
            if cx-cr-ERR < m < cx+cr+ERR:
                ix, iy = intpil(m, 0.0, 0.0, pk)
                iy2 = 2*cy-iy
                il.append((iy, 4, pk))
                il.append((iy2, 0, pk))

        for lw in range(2):
            l = [lr, lg][lw]
            for lk, lx in enumerate(l):
                ip = intline(*(lx+(m, 0.0, m, 100.0)))
                if ip != None:
                    d, ix, iy = ip
                    il.append((iy, 2+lw, lk))

        il.append((0.0, 1, 0))
        il.append((100.0, 1, 1))
                       
        return sorted(il)

    def intpil(px, py, a, hk):
        cx, cy, cr = p[hk]
        ca = center(px, py, cx, cy)
        d = dist(px, py, cx, cy)
        th = ca-a
        disc = cr**2-d**2*sin(th)**2
        if -ERR2 < disc < 0:
            disc = 0
        if disc <= -ERR2:
            return None
        x = d*cos(th)-sqrt(disc)
        ix, iy = coord(px, py, a, x)
        return (ix, iy)
    
    def intedge(px, py, a):
        cs = [(0.0, 0.0), (0.0, 100.0), (100.0, 100.0), (100.0, 0.0)]
        q = []
        for i in range(4):
            sx, sy = cs[i]
            tx, ty = cs[(i+1)%4]
            qx = px+142*sin(a)
            qy = py+142*cos(a)
            ip = intline(px, py, qx, qy, sx, sy, tx, ty)
            if ip != None:
                q.append(ip)
        q.sort()
        return q[0][1:]

    def intline(ax, ay, bx, by, cx, cy, dx, dy):
        a1 = center(ax, ay, bx, by)
        a2 = center(cx, cy, dx, dy)
        dnum = ax*cos(a1)-ay*sin(a1)-cx*cos(a1)+cy*sin(a1)
        dden = sin(a2)*cos(a1)-cos(a2)*sin(a1)
        if -ERR < dden < ERR:
            return None
        else:
            d = dnum/dden
            ix = cx+d*sin(a2)
            iy = cy+d*cos(a2)
            d1 = dist(ax, ay, ix, iy)
            d1x = dist(bx, by, ix, iy)
            e1 = dist(ax, ay, bx, by)
            d2 = dist(cx, cy, ix, iy)
            d2x = dist(dx, dy, ix, iy)
            e2 = dist(cx, cy, dx, dy)

            if d1 < e1+ERR and d1x < e1+ERR and d2 < e2+ERR and d2x < e2+ERR:
                return (d1, ix, iy)
            else:
                return None

    def partition(x, a):
        pre = []
        i = 0
        while i < len(x) and x[i][0] < a:
            pre.append(x[i])
            i += 1
        return x[i:] + pre

    def current(lx, ly, a):
        cs = []
        for pillar in range(len(p)):
            cx, cy, cr = p[pillar]
            d = dist(lx, ly, cx, cy)
            cv = center(lx, ly, cx, cy)
            av = offset(d, cr)
            la = cv-av
            ra = cv+av
            if la <= a < ra or la <= a+2*pi < ra or la <= a-2*pi < ra:
                cs.append((d, pillar))
        return sorted(cs)

    def moments():
        ms = set()
        ms.add(0.0)
        ms.add(100.0)
        for cx, cy, cr in p:
            ms.add(cx-cr)
            ms.add(cx+cr)
        for l in (lr, lg):
            for x1, y1, x2, y2 in l:
                ms.add(x1)
                ms.add(x2)
        for l1 in lr:
            for l2 in lg:
                ip = intline(*(l1+l2))
                if ip != None:
                    ms.add(ip[1])
        return sorted(list(ms))

    def area(x1, x2, l1, h1, l2, h2, tl, th):
        ta = (x2-x1)*(h1-l1+h2-l2)/2
        for w, (t, k) in enumerate((tl, th)):
            if t == 0 or t == 4:
                cx, cy, cr = p[k]
                y1 = (l1, h1)[w]
                y2 = (l2, h2)[w]
                chs = (x2-x1)**2 + (y2-y1)**2
                a = acos(1-chs/(2*cr**2))
                sa = cr**2*(a-sin(a))/2
                if t == 4*w:
                    ta -= sa
                else:
                    ta += sa
        return ta

    def color(px, py):
        col = 3
        for hk in range(len(p)):
            cx, cy, cr = p[hk]
            dc = dist(px, py, cx, cy)
            if dc < cr:
                return -1
        for co in range(2):
            lx, ly = [(rx, ry), (gx, gy)][co]
            a = center(px, py, lx, ly)
            d = dist(px, py, lx, ly)
            for hk in range(len(p)):
                ip = intpil(px, py, a, hk)
                if ip != None:
                    ix, iy = ip
                    di = dist(px, py, ix, iy)
                    ds = dist(lx, ly, ix, iy)
                    if di < d+ERR and ds < d+ERR:
                        col ^= 1+co
                        break
        return col            

    def segs(lx, ly):
        ret = []
        pps = []
        ca = None
        cd = MAX
        dists = []
        for pillar in range(len(p)):
            cx, cy, cr = p[pillar]
            d = dist(lx, ly, cx, cy)
            dists.append(d)

            sep = d-cr
            cv = center(lx, ly, cx, cy)

            av = offset(d, cr)
            
            ad = cr/tan(av)
            
            if sep < cd:
                cd = sep
                ca = norm(cv)

            pps.append((norm(cv-av), ad, pillar, 0))
            pps.append((norm(cv+av), ad, pillar, 1))
 
        pps.sort()
        
        pps = partition(pps, ca)
        
        stack = current(lx, ly, ca)

        for a, d, pk, t in pps:
            px, py = coord(lx, ly, a, d)
            if len(stack) == 0 or (pk == stack[0][1] and len(stack) == 1):
                ix, iy = intedge(px, py, a)
                ret.append((px, py, ix, iy))
            else:
                hd, hk = stack[0]
                if pk == hk:
                    hd, hk = stack[1]

                ix, iy = intpil(px, py, a, hk)
                di = dist(lx, ly, ix, iy)
                dp = dist(lx, ly, px, py)
                if dp < di + ERR:
                    ret.append((px, py, ix, iy))
           
            if t == 0:
                stack.append((dists[pk], pk))
                stack.sort()
            else:
                for v in range(len(stack)):
                    if stack[v][1] == pk:
                        del stack[v]
                        break

        return ret


    rx, ry = map(int, raw_input().split())
    gx, gy = map(int, raw_input().split())
    n = int(raw_input())
    p = [map(int, raw_input().split()) for i in range(n)]

    fi = open('testcase-%d.ps' % case, 'w')
    
    fi.write('%!PS\n')
    fi.write('4 4 scale\n')
    fi.write('20 80 translate\n')
    fi.write('newpath 0 0 moveto\n')
    fi.write('0 100 lineto 100 0 rlineto 0 -100 rlineto\n-100 0 rlineto\n')
    fi.write('closepath\n0 0 0 setrgbcolor\n0.1 setlinewidth\nstroke\n')
    
    for cx, cy, cr in p:
        fi.write('%d %d %d 0 360 arc closepath fill\n' % (cx, cy, cr))

    lr = segs(rx, ry)
    lg = segs(gx, gy)

    fi.write('0.1 setlinewidth\n')
    fi.write('1 0 0 setrgbcolor\n')
    fi.write('%f %f 0.5 0 360 arc closepath fill\n' % (rx, ry))
    for txy in lr:
        fi.write('newpath %f %f moveto %f %f lineto closepath stroke\n' % txy)
    fi.write('0 1 0 setrgbcolor\n')
    fi.write('%f %f 0.5 0 360 arc closepath fill\n' % (gx, gy))
    for txy in lg:
        fi.write('newpath %f %f moveto %f %f lineto closepath stroke\n' % txy)

    fi.write('0.05 setlinewidth\n')
    fi.write('0.5 setgray\n')

    ms = moments()
    ms2 = []
    for j in ms:
        if len(ms2) == 0 or j > ms2[-1]+ERR:
            ms2.append(j)
            fi.write('newpath %f 0 moveto 0 100 rlineto closepath stroke\n' % j)

    ar = [0]*5
    ct = [0]*5

    mx = 0.0
    il = intm(mx)
    for m in ms2[1:]:
        iln = intm(m)
        pairs = dict()
        for lk, l in enumerate((il, iln)):
            for y, t, k in l:
                if (t, k) not in pairs:
                    pairs[(t, k)] = []
                pairs[(t, k)].append((lk, y))
        
        segs = []
        for tk in pairs.keys():
            if len(pairs[tk]) == 2:
                y1, y2 = map(lambda x: x[1], sorted(pairs[tk]))
                midx = (m+mx)/2.0
                t, k = tk
                if t == 0 or t == 4:
                    cx, cy, cr = p[k]
                    v = cr**2 - (midx-cx)**2
                    if -ERR2 < v < 0:
                        v = 0
                    if t == 0:
                        midy = cy + sqrt(v)
                    else:
                        midy = cy - sqrt(v)
                else:                   
                    midy = (y1+y2)/2
                segs.append((midy, y1, y2, tk))
        segs.sort()

        fi.write('0.1 setlinewidth\n')
        
        for sk, seg in enumerate(segs[:-1]):
            segn = segs[sk+1]
            pa = area(mx, m, seg[1], segn[1], seg[2], segn[2], seg[3], segn[3])
            midx = (m+mx)/2.0
            midy = (seg[0]+segn[0])/2.0
            pc = color(midx, midy)
            if pc == 0:
                fi.write('0 0 0.75 setrgbcolor\n')
            elif pc == 1:
                fi.write('0.75 0 0 setrgbcolor\n')
            elif pc == 2:
                fi.write('0 0.75 0 setrgbcolor\n')
            elif pc == 3:
                fi.write('0.75 0.75 0 setrgbcolor\n')
            else:
                fi.write('0.75 0.75 0.75 setrgbcolor\n')
            fi.write('%f %f 0.25 0 360 arc closepath fill\n' % (midx, midy))
            
            ar[pc] += pa
            ct[pc] += 1

        il = iln
        mx = m

    for x in ar[:-1]:
        print x

    fi.write('showpage\n')
    fi.close() 


for i in range(int(raw_input())):
    print "Case #%d:" % (i+1)
    compute(i+1)
