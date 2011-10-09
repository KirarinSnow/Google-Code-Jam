#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 問題: 最高のコーヒー
# 言語: Python
# 著者: KirarinSnow
# 使い方: python thisfile.py <input.in >output.out



for case in range(1, input()+1):
    n, k = map(int, raw_input().split())
    vs = [map(int, raw_input().split()) for i in range(n)]
    
    done = []
    total = 0

    vs.sort(key=lambda x: x[2], reverse=True)

    for v in vs:
        c, t, s = v

        p = t
        r = c
        while p > 0:
            for d in done[::-1]:
                if d[0] < p <= d[1]:
                    p = d[0]
            q = max(p-r, 0)
            for d in done[::-1]:
                if d[1] < p:
                    q = max(p-r, d[1])
                    break

            if q < p:
                done.append([q, p])
                done.sort()
                r -= (p-q)
                total += (p-q)*s
                p = q
            else:
                break

    print "Case #%d: %d" % (case, total)
