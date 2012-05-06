#!/usr/bin/python
#
# Problem: Marbles
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Adapted from reference solution. Takes too long for large input.


MAX = 1<<20

cache = []
evcache = []
vis = []
n = 0
marbles = []
where = []

def h2(a, b, h1):
    if h1 < 0: return MAX
    if a == b: return 0    
    res = cache[a][h1]
    if res != -1: return res

    ev = events(a)
    res = MAX
    for mask in (0, 2):
        top = 0
        bot = 0
        H2 = 0
        for i in xrange(len(ev)+1):
            if i == 0:
                alpha = a
            else:
                alpha = ev[i-1][0] + 1
            if i == len(ev):
                beta = b
            else:
                beta = ev[i][0]
            H2 = max(H2, h2(alpha, beta, h1-top) + bot)
            if i != len(ev):
                z = ev[i][1] ^ mask
                if z == 0:
                    top += 1
                elif z == 1:
                    top -= 1
                elif z == 2:
                    bot += 1
                else:
                    bot -= 1
        res = min(res, H2)
    return res

def events(startx):
    global vis, evcache
    res = evcache[startx]
    if len(res) > 0:
        return res
    vis = [0]*n
    dfs(marbles[startx], 1)
    for x in xrange(2*n):
        m = marbles[x]
        if vis[m] == 0: continue
        nr = 0
        if where[m][nr] != x: nr += 1
        res.append((x, 1-vis[m]+nr))
    evcache[startx] = res
    return res

def dfs(m, sign):
    if vis[m] == sign: return
    if vis[m] == -sign: raise 0
    vis[m] = sign
    for i in xrange(n):
        if i != m and cross(m, i):
            dfs(i, -sign)
    
def cross(m1, m2):
    return where[m1][0] < where[m2][0] < where[m1][1] < where[m2][1] or \
        where[m2][0] < where[m1][0] < where[m2][1] < where[m1][1]

def compute():
    global cache, evcache, n, marbles, where
    n = int(raw_input())
    z = raw_input().split()

    marbles = []
    where = [[] for i in xrange(n)]
    d = {}
    for i in z:
        if i in d:
            m = d[i]
        else:
            m = len(d)
            d[i] = m
        where[m].append(len(marbles))
        marbles.append(m)
    
    cache = []
    evcache = []
    for i in xrange(2*n):
        cache.append([-1]*(n+1))
        evcache.append([])

    res = MAX
    try:
        for h1 in range(n+1):
            res = min(res, h1 + h2(0, 2*n, h1))
    except:
        return -1

    return res
    

for i in range(int(raw_input())):
    print "Case #%d: %d" % (i+1, compute())
