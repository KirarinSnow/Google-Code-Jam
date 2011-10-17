#!/usr/bin/python
#
# Problem: Football Team
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def check():
        for x, y in vs:
            l = [i[0] for i in vs if i[1] == y and i[0] < x]
            r = [i[0] for i in vs if i[1] == y and i[0] > x]
            u = [i[0] for i in vs if i[1] == y-1 and i[0] > x]
            d = [i[0] for i in vs if i[1] == y+1 and i[0] > x]
            if l and r and u and d:
                uu = [i[0] for i in vs if i[1] == y-1 and max(l) < i[0] < x]
                dd = [i[0] for i in vs if i[1] == y+1 and max(l) < i[0] < x]
                if (len(uu)+len(dd))%2 == 1:
                    return 4
        return 3

    n = input()
    vs = [tuple(map(int, raw_input().split())) for i in range(n)]
    
    es = []
    g = {}
    for v in vs:
        g[v] = []
    for v in vs:
        x, y = v
        for yy in [y-1, y, y+1]:
            cs = filter(lambda u: u[1] == yy and u[0] > x, vs)
            if cs:
                c = min(sorted(cs))
                es.append([v, c])
                g[v].append(c)
                g[c].append(v)
    
    if es:
        r = list(vs)
        d = {}
        while r:
            q = [r[0]]
            while q:
                v = q.pop()
                if v in d:
                    return check()
                d[v] = g[v]
                for u in d[v]:
                    if u not in d:
                        q.append(u)
                    elif v not in d[u]:
                        q.append(u)
            r = filter(lambda x: x not in d, r)
        return 2
        
    else:
        return 1


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
