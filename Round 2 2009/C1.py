#!/usr/bin/python
#
# Problem: Stock Charts
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def cp(a, b):
        return len(a)*[True] == map(lambda x, y: x<y, a, b)

    def dfs(x): # search for available match
        if visited[x] != label: # not yet seen
            visited[x] = label
            for y in nb[x]:
                if match[y] == None or dfs(match[y]):
                    match[x] = y
                    match[y] = x
                    return True
        return False

    n, k = map(int, raw_input().split())
    pr = [map(int, raw_input().split()) for i in range(n)]
    nb = [{} for i in range(2*n)]

    for i in range(n):
        for j in range(n):
            if cp(pr[i], pr[j]):
                nb[i][n+j] = True
                nb[n+j][i] = True

    match = [None]*2*n
    visited = [None]*2*n
    
    matching = 0
    label = 0
    for i in range(n):
        if dfs(i):
            matching += 1
        label += 1
        
    return n-matching

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
