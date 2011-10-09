#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 問題: ビット数 
# 言語: Python
# 著者: KirarinSnow
# 使い方: python thisfile.py <input.in >output.out



for case in range(1, input()+1):
    n = input()
    ans = 0

    c = True

    while n > 0:
        while n % 2 == 0 :
            n /= 2
            ans += 1
            c = False
        n -= 1
        ans += 1
        if c:
            n /= 2        
                    
    print "Case #%d: %d" % (case, ans)
