#!/usr/bin/env pypy
#
# Problem: Fence
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out


MAX = 1<<99

for case in range(int(raw_input())):
    l, n = map(int, raw_input().split())
    b = sorted(map(int, raw_input().split()))

    a = b.pop()
    p = l/a
    q = l%a

    g = [(0)]
    v = [MAX]*a
    w = [False]*a
    m = MAX

    e = []
    for i in range(a):
        e.append([])
        for j in range(n-1):
            e[i].append((0, 1)[i+b[j] < a])
    
    z = (a-1)*(n-1)

    v[0] = 0
    while g:
        i = g.pop(0)
        if w[i]:
            continue
        if v[i] > z:
            break
        h = [i]
        while h:
            i = h.pop()
            if i == q:
                m = min(m, v[i]+p)
                break
            for j in range(n-1):
                k = (i+b[j])%a
                x = v[i]+e[i][j]
                if x < v[k]:
                    v[k] = x
                    if x > v[i]:
                        g.append(k)
                    else:
                        h.append(k)
        else:
            continue
        break

    ans = m if m < MAX else "IMPOSSIBLE"

    print "Case #%d: %s" % (case+1, ans)
