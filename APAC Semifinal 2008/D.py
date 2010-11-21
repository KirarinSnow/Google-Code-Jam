#!/usr/bin/env python
#
# Problem: Modern Art Plagiarism
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


# Tree is list of vertices, where each vertex is
# [Depth, Parent, Children]
def tree(nv, edges, root):
    t = [[0, None, []] for i in range(nv)]
    q = [root]
    seen = [False] * nv
    while q:
        v = q.pop()
        seen[v] = True
        for p in edges:
            if v == p[0]-1:
                w = p[1]-1
            elif v == p[1]-1:
                w = p[0]-1
            else:
                continue
            if not seen[w]:
                t[v][2].append(w)
                t[w][1] = v
                t[w][0] = t[v][0]+1
                q.append(w)
    return t

def levels(t, nv):
    l = [[] for i in range(nv)]
    for i in range(nv):
        l[t[i][0]].append(i)
    return l

def matching(left, right, edges, k):
    def dfs(node): # search for available match
        if node not in visited: # not yet seen
            visited[node] = True
            for y in right:
                if (node, y) in edges:
                    if (y not in ms) or dfs(ms[y]):
                        ms[node] = y
                        ms[y] = node
                        return True
        return False

    # unique ids
    right = map(lambda x: k+x, right)

    ms = {}
    for x in left:
        visited = {}
        if not dfs(x):
            return False
    return True

def compute(i):
    n = input()
    large = [map(int, raw_input().split()) for i in range(n-1)]
    m = input()
    small = [map(int, raw_input().split()) for i in range(m-1)]
    
    st = tree(m, small, 0)
    sl = levels(st, m)

    if m <= 3:
        return "YES"

    # Iterate over possible roots of large tree
    for x in range(n):
       # print x
        match = set()
        lt = tree(n, large, x)
        ll = levels(lt, n)
        for level in range(len(sl))[::-1]:
            for sv in sl[level]:
                for lv in ll[level]:
                    if st[sv][2]:
                        if matching(st[sv][2], lt[lv][2], match, m):
                            if sv == 0 and lv == x:
                                return "YES"
                            match.add((sv, m+lv))
                    else: # leaf in small tree
                        match.add((sv, m+lv))
                        
    return "NO"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute(i))
