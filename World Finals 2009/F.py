#!/usr/bin/python
#
# Problem: Lights
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Uses http://mpmath.googlecode.com for arbitrary precision.
#           Some incorrect answers for large input set.


from mpmath import *

mp.dps = 20

ERR = 1e-18
ERR2 = 200*ERR

corners = [(0, 0), (0, 100), (100, 100), (100, 0)]

def compute():
    def sqrm(x):
        return sqrt(max(0, x))
    
    def angle(ii, jj, i, j, k):
        return asin(k/dist(ii, jj, i, j))

    def center(ii, jj, i, j):
        return atan2(i-ii, j-jj)
   
    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

    def lines(lx, ly, ox, oy):
        l = []
        l.append(center(lx, ly, ox, oy))
        for i, j in corners:
            l.append(center(lx, ly, i, j))
        for i, j, k in p:
            av = angle(lx, ly, i, j, k)
            cv = center(lx, ly, i, j)
            l.append((cv-av))
            l.append((cv+av))
        l = map(lambda li: li%(2*pi), l)
        return sorted(l)

    def triangle(ip):
        d1 = dist(ip[0][0], ip[0][1], ip[1][0], ip[1][1])
        d2 = dist(ip[0][0], ip[0][1], ip[2][0], ip[2][1])
        a1 = center(ip[0][0], ip[0][1], ip[1][0], ip[1][1])
        a2 = center(ip[0][0], ip[0][1], ip[2][0], ip[2][1])
        ang = sep(a1, a2)
        ar = d1*d2*sin(ang)/2
        return ar
    
    def quad(ip):
        ar = 0
        for a, b, c in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
            ar += triangle([ip[a], ip[b], ip[c]])
        ar /= 2
        return ar

    def pentagon(ip):
        ar = 0
        cx, cy = ip[0]
        pa = map(lambda x: (center(cx, cy, x[0], x[1]), x), ip[1:])
        pa.sort()
        for i in range(4):
            pq = pa[i]
            pr = pa[i-1]
            incr = (pq[0]-pr[0])%(2*pi)
            if incr < pi:
                ar += triangle([(cx, cy), pq[1], pr[1]])
        return ar

    def polygon(ip):
        if len(ip) > 4:
            return pentagon(ip)
        elif len(ip) == 4:
            return quad(ip)
        elif len(ip) == 3:
            return triangle(ip)
        else:
            return 0
        
    def between(a, x, y):
        dx = sep(a, x)
        dy = sep(a, y)
        dd = sep(x, y)
        return abs(dx+dy - dd) < ERR

    def sep(a, b):
        return min(abs(a-b), abs(a-b+2*pi), abs(a-b-2*pi))

    def intersect(x1, y1, x2, y2, x3, y3, x4, y4, a2=0):
        spec = (x2 == None)
        if not spec:
            a2 = center(x1, y1, x2, y2)

        a3 = center(x1, y1, x3, y3)
        a4 = center(x1, y1, x4, y4)

        cz = center(x3, y3, x4, y4)
        czp = center(x4, y4, x3, y3)
        
        if abs(a2-cz) < ERR or abs(a2-czp) < ERR:
            return None
        elif not between(a2, a3, a4):
            return None
        else:
            ang = sep(a3, a4)
            ang3 = sep(a2, a3)
            ang4 = sep(a2, a4)
            d3 = dist(x1, y1, x3, y3)
            d4 = dist(x1, y1, x4, y4)
            if not spec:
                d2 = dist(x1, y1, x2, y2)

            dn = sin(ang3)*d3+sin(ang4)*d4
            if dn < ERR:
                dm = 0
            else:
                dm = sin(ang)*d3*d4/dn
            if not spec and dm > d2 + ERR2:
                return None
            else:
                xo = x1 + sin(a2)*dm
                yo = y1 + cos(a2)*dm
                return (xo, yo)

    def hits(lx, ly, l):
        t = [None]*len(l)
        for d in range(len(l)):
            aa = l[d]%(2*pi)
            bb = l[d-1]%(2*pi)
            for i, j, k in p:
                c = center(lx, ly, i, j)
                o = angle(lx, ly, i, j, k)%(2*pi)
                la = c-o
                ua = c+o
                if between(aa, ua, la) and between(bb, ua, la):
                    f = sqrt((lx-i)**2 + (ly-j)**2)
                    av = sep(aa, c)
                    aw = sep(bb, c)
                    hv = f*sin(av)
                    hw = f*sin(aw)
                    v = sqrt(f**2-hv**2)-sqrm(k**2-hv**2)
                    w = sqrt(f**2-hw**2)-sqrm(k**2-hw**2)
                    ang = sep(aa, bb)
                    tar = sin(ang)*v*w/2
                    chord = sqrm(v**2+w**2-2*v*w*cos(ang))
                    md = sqrt(k**2 - chord**2/4)
                    sa = abs(2*acos(md/k))
                    sar = pi*k**2*sa/(2*pi) - k**2*sin(sa)/2
                    ar = tar-sar
                    xv = sin(aa)*v+lx
                    yv = cos(aa)*v+ly
                    xw = sin(bb)*w+lx
                    yw = cos(bb)*w+ly
                    
                    if t[d] == None or f < t[d][3]:
                        t[d] = [1, ar, (xv, yv, xw, yw), f, (i, j, k)]
            if t[d] == None:
                for co in range(len(corners)):
                    xi, yi = corners[co]
                    xj, yj = corners[co-1]
                    ai = center(lx, ly, xi, yi)
                    aj = center(lx, ly, xj, yj)
                    if between(aa, ai, aj) and between(bb, ai, aj):
                        if xi == xj:
                            da = (lx-xi)/sin(aa)
                            db = (lx-xi)/sin(bb)
                            xv = xi
                            yv = ly-cos(aa)*da
                            xw = xi
                            yw = ly-cos(bb)*db
                        else:
                            da = (ly-yi)/cos(aa)
                            db = (ly-yi)/cos(bb)
                            xv = lx-sin(aa)*da
                            yv = yi
                            xw = lx-sin(bb)*db
                            yw = yi
                        ang = sep(aa, bb)
                        ar = sin(ang)*abs(da)*abs(db)/2
                        t[d] = [0, ar, (xv, yv, xw, yw)]
                    
        return t

    def common(rx, ry, hr, gx, gy, hg):
        total = 0

        for tr in hr:
            prx1, pry1, prx2, pry2 = tr[2]
            for tg in hg:
                pgx1, pgy1, pgx2, pgy2 = tg[2]
                


                ip = []
                
                for r1, r2, r3, r4 in [(rx, ry, prx1, pry1),
                                       (rx, ry, prx2, pry2),
                                       (prx1, pry1, prx2, pry2)]:
                    for g1, g2, g3, g4 in [(gx, gy, pgx1, pgy1),
                                           (gx, gy, pgx2, pgy2),
                                           (pgx1, pgy1, pgx2, pgy2)]:
                        
                        ipp = intersect(r1, r2, r3, r4, g1, g2, g3, g4)
                        if ipp != None:
                            cl = False
                            for pt in ip:
                                if abs(pt[0]-ipp[0]) < ERR2 and \
                                        abs(pt[1]-ipp[1]) < ERR2:
                                    cl = True
                                    break
                            else:
                                ip.append(ipp)

                if tr[0] == 1 and tg[0] == 1:
                    if tr[4] != tg[4]:
                        total += polygon(ip)
                    else:
                        i, j, k = tr[4]
                        ds = map(lambda x: dist(x[0], x[1], i, j), ip)
    
                        if len(ip) >= 3 and len(filter(lambda z: z<k, ds)) == 0:
                            total += polygon(ip)
                        elif len(ip) >= 2:
                            dp = filter(lambda x: dist(x[0], x[1], i, j)>k, ip)
                            vr1 = center(i, j, prx1, pry1)
                            vr2 = center(i, j, prx2, pry2)
                            vg1 = center(i, j, pgx1, pgy1)
                            vg2 = center(i, j, pgx2, pgy2)

                            if (vg2-vr2)%(2*pi)<pi:
                                cr1 = (prx2, pry2)
                                v1 = vr2
                            else:
                                cr1 = (pgx2, pgy2)
                                v1 = vg2
                            if (vg1-vr1)%(2*pi)<pi:
                                cr2 = (pgx1, pgy1)
                                v2 = vg1
                            else:
                                cr2 = (prx1, pry1)
                                v2 = vr1
                            dp.append(cr1)
                            dp.append(cr2)

                            ang = sep(v2, v1)
                            sar = k*k*pi*(ang/(2*pi))
                            d1 = dist(i, j, cr1[0], cr1[1])
                            d2 = dist(i, j, cr2[0], cr2[1])
                            tar = d1*d2*sin(ang)/2
                            seg = sar - tar

                            total += polygon(dp)-seg
                            
                else:
                    total += polygon(ip)

        return total
           
    rx, ry = map(int, raw_input().split())
    gx, gy = map(int, raw_input().split())
    n = int(raw_input())
    p = [map(int, raw_input().split()) for i in range(n)]
    
    lr = lines(rx, ry, gx, gy)
    lg = lines(gx, gy, rx, ry)

    hr = hits(rx, ry, lr)
    hg = hits(gx, gy, lg)

    ar = sum(map(lambda x: x[1], hr))
    ag = sum(map(lambda x: x[1], hg))

    arg = common(rx, ry, hr, gx, gy, hg)

    ar -= arg
    ag -= arg

    par = 0
    for i, j, k in p:
        par += k**2
    bl = 10000 - ar - ag - arg - par*pi

    print max(0, bl)
    print ar
    print ag
    print arg

    
for i in range(int(raw_input())):
    print "Case #%d:" % (i+1)
    compute()
