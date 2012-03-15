#!/usr/bin/python
#
# Problem: Wi-fi Towers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Using graph-tool: http://projects.skewed.de/graph-tool/


from graph_tool.all import *

MAX = 1<<20

def compute():
    n = int(raw_input())
    z = [map(int, raw_input().split()) for i in range(n)]

    g = Graph()
    cap = g.new_edge_property("int")

    s = g.add_vertex()
    t = g.add_vertex()

    vl = []

    ps = 0
    for i in range(n):
        xi, yi, r, sc = z[i]

        v = g.add_vertex()
        vl.append(v)

        if sc >= 0:
            e = g.add_edge(s, v)
            cap[e] = sc
            ps += sc
        else:
            e = g.add_edge(v, t)
            cap[e] = -sc

    for i in range(n):
        xi, yi, r, sc = z[i]
        vi = vl[i]

        for j in range(n):
            if i != j:
                xj, yj = z[j][:2]
                if (xi-xj)**2 + (yi-yj)**2 <= r**2:
                    vj = vl[j]
                    e = g.add_edge(vi, vj)
                    cap[e] = MAX

    res = push_relabel_max_flow(g, s, t, cap)
    res.a = cap.a - res.a

    m = sum(res[e] for e in s.out_edges())

    return ps - m
    
 
for i in range(int(raw_input())):
    print "Case #%d: %d" % (i+1, compute())
