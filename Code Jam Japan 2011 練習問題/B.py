#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 問題: 数の集合
# 言語: Python
# 著者: KirarinSnow
# 使い方: python thisfile.py <input.in >output.out 
# コメント: Round 1B 2008の「Number Sets」という問題の解答と同じ。


from math import *


MAX = 1000000
prime = [True]*(MAX+1)
for n in xrange(2, int(sqrt(MAX))+1):
    for i in xrange(2*n, MAX+1, n):
        prime[i] = False

parent = [0]*(MAX+1)
size = [0]*(MAX+1)


def compute():
    a, b, p = map(int, raw_input().split())
    
    for i in xrange(b-a+1):
        parent[i] = i
        size[i] = 1

    count = b-a+1

    n = p
    while n <= min(b, MAX):
        if prime[n]:
            f = (n - a%n)%n

            for g in xrange(f+n, b-a+1, n):
                
                head = g
                while parent[head] != head:
                    head = parent[head]
                
                while parent[f] != f:
                    f = parent[f]

                if f != head:
                    count -= 1
                    if size[f] < size[head]:
                        parent[f] = head
                        size[head] += size[f]
                    else:
                        parent[head] = f
                        size[f] += size[head]
        n += 1            
    return count
 

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
