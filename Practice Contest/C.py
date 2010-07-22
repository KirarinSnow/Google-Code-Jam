#!/usr/bin/python
#
# Problem: Cycles
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out



MAX = 100000000000
RMOD = 9901


fact = range(305)
fact[0] = 1
fact[1] = 1
fact[2] = 1
for i in range(3,len(fact)):
    fact[i] = (fact[i-1]*fact[i])%RMOD


def compute():
    n, k = map(int, raw_input().split())
    le = []
    for i in range(k):
        le.append(tuple(map(int, raw_input().split())))
    
    t = 0
    for s in range(1<<k):
        b = 1
        e = 0
        vc = [0]*n

        ss = s
        ll = []
        pl = 0
        while ss > 0:
            if ss%2 == 1:
                ll.append(le[k-pl-1])
                e += 1
            pl += 1
            ss >>= 1
            
        for ed in ll:
            vc[ed[0]-1] += 1
            vc[ed[1]-1] += 1
            if vc[ed[0]-1] > 2 or vc[ed[1]-1] > 2:
                b = 0
                break

        bx = 1
        b2 = 1
        h = 0
        d = 0
        z = 0
        for v in vc:
            if v == 1:
                h += 1
            elif v == 2:
                d += 1
            elif v == 0:
                z += 1
            else:
                if b != 0:
                    print v

        # Detect and count cycles
        ll2 = []
        for ed in ll:
            if ed[0] < ed[1]:
                ll2.append(ed)
            else:
                ll2.append((ed[1],ed[0]))
        ll2.sort()
        changed = 1
        bx = 0
        while changed == 1:
            changed = 0
            for li in range(len(ll2)-1):
                aa = ll2[li]
                bb = ll2[li+1]
                if aa[0] == bb[0] and aa[1] == bb[1]:
                    bx += 1
                    b2 = 0
                    del ll2[li+1]
                    del ll2[li]
                    changed = 1
                    break
                elif aa[0] == bb[0]:
                    cc = aa[1]
                    dd = bb[1]
                    if cc < dd:
                        cd = (cc,dd)
                    else:
                        cd = (dd,cc)
                    del ll2[li+1]
                    del ll2[li]
                    ll2.append(cd)
                    ll2.sort()
                    changed = 1
                    break
                
        if z > 0 and h == 0 and d > 0: # not Hamiltonian
            b = 0

        if bx > 1:
            b = 0
        if h == 0 and z == 0 and bx == 1: # single forbidden cycle
            c = 0
            b2 = 1
        elif h/2 == 1 and z <= 1:
            c = 0
        elif h/2 == 2 and z == 0:
            c = 1
        else:
            c = h/2

        q = (1<<c)
        q *= b * b2

        if n-e >= 3:
            rr = fact[n-e-1]
        else:
            rr = 1

        q *= rr
        q %= RMOD
        
        q *= (-1)**e
        
        t += q 
        t %= RMOD
    return t

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
