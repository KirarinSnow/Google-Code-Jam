#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 問題: カードシャッフル
# 言語: Python
# 著者: KirarinSnow
# 使い方: python thisfile.py <input.in >output.out



for case in range(1, input()+1):
    m, c, w = map(int, raw_input().split())
    a, b = zip(*[map(int, raw_input().split()) for i in range(c)])
    
    s = [(1, m)]

    for i in range(c):
        for j in range(2):
            val = [a[i]-1, a[i]+b[i]-1][j]
            seen = 0
            p = 0
            while p < len(s) and seen <= val:
                seen += s[p][1]-s[p][0]+1
                p += 1
            over = seen-val
            under = s[p-1][1]-s[p-1][0]+1-over
            int1 = (s[p-1][0], s[p-1][0]+under-1)
            int2 = (s[p-1][0]+under, s[p-1][1])
            r = list(s[:p-1])
            if j == 0:
                pre = list(r)
            if int1[1] >= int1[0]:
                r.append(int1)
            if int2[1] >= int2[0]:
                r.append(int2)
            r.extend(s[p:])
            s = r

        seen = 0
        p = 0
        while seen < a[i]-1:
            seen += s[p][1]-s[p][0]+1
            p += 1
        start = p
        while seen < a[i]+b[i]-1:
            seen += s[p][1]-s[p][0]+1
            p += 1
        end = p
        s = s[start:end] + s[:start] + s[end:]       
       
    p = 0
    seen = 0
    while seen < w:
        seen += s[p][1]-s[p][0]+1
        p += 1
    done = seen - (s[p-1][1]-s[p-1][0]+1)
    ans = s[p-1][0]+(w-done)-1
            
    print "Case #%d: %d" % (case, ans)
