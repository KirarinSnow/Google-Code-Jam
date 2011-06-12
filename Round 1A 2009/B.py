#!/usr/bin/python
#
# Problem: Crossing the Road
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from heapq import *

MAX = 1<<30

def compute():
    n, m = map(int, raw_input().split())
    b = [zip(*[iter(map(int, raw_input().split()))]*3) for i in range(n)]
    d = {}
    q = []
    
    for i in range(2*n):
        for j in range(2*m):
            if i == 2*n-1 and j == 0:
                heappush(q, [0, (i, j)])
            else:
                heappush(q, [MAX, (i, j)])

    while q:
        z, u = heappop(q)
        if u in d:
            continue
        d[u] = z
        vs = []
        s, w, t = b[u[0]/2][u[1]/2]
        a = (z-t)%(s+w)
        if u[0] > 0:
            v = (u[0]-1, u[1])
            if u[0]%2 == 0:
                vs.append([z+2, v])
            else:
                if a < s:
                    vs.append([z+1, v])
                else:
                    vs.append([z+s+w-a+1, v])
        if u[0] < 2*n-1:
            v = (u[0]+1, u[1])
            if u[0]%2 == 1:
                vs.append([z+2, v])
            else:
                if a < s:
                    vs.append([z+1, v])
                else:
                    vs.append([z+s+w-a+1, v])
        if u[1] > 0:
            v = (u[0], u[1]-1)
            if u[1]%2 == 0:
                vs.append([z+2, v])
            else:
                if a >= s:
                    vs.append([z+1, v])
                else:
                    vs.append([z+s-a+1, v])
        if u[1] < 2*m-1:
            v = (u[0], u[1]+1)
            if u[1]%2 == 1:
                vs.append([z+2, v])
            else:
                if a >= s:
                    vs.append([z+1, v])
                else:
                    vs.append([z+s-a+1, v])
        for v in vs:
            heappush(q, v)

    return d[(0, 2*m-1)]
    

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
