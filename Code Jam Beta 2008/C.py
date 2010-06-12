#!/usr/bin/python
#
# Problem: Random Route
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys
import heapq
from math import *
from string import *

MAX = 100000000000


def grab():
    return int(file.readline())

def grabs():
    return map(int,file.readline().split())

def removechars(str, chars):
    return str.translate(maketrans('',''),chars)

def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():

    def countroutes(v, x, s): # num of routes into x toward v
        if v in counts[x]:
            return
        if x[0] == s:
            counts[x][v] = 1
        elif x[0] not in pred:
            counts[x][v] = 0
        else:
            pp = pred[x[0]]
            num = 0
            for i in pp:
                pv = i
                countroutes(v, pv, s)
                num += counts[pv][v]
            counts[x][v] = num
                
    def countr2(v, x, s): # num of routes out of x toward v
        if v in scounts[x]:
            return
        if x[1] not in succ:
            scounts[x][v] = 0
        else:
            pp = succ[x[1]]
            num = 0
            for i in pp:
                countr2(v, i, s)
                num += scounts[i][v]
            scounts[x][v] = num

    nr = int(buffer.pop(0))
    source = buffer.pop(0)
    edges = []
    vertices = dict()
    pred = dict()
    succ = dict()

    for i in xrange(nr):
        a,b,c = buffer.pop(0),buffer.pop(0),int(buffer.pop(0))
        edges.append((a,b,c,i))
        if a not in vertices: #[d, inedge->{v->num}, outedges, v->total]
            vertices[a] = [MAX,dict(),[],dict()]
        if b not in vertices:
            vertices[b] = [MAX,dict(),[],dict()]
        vertices[a][2].append(edges[i])
        vertices[b][1][edges[i]] = dict()
        
    vertices[source][0] = 0 #d[s] = 0

    q = map(lambda k: (vertices[k][0], k), vertices.keys())
    
    heapq.heapify(q)

    s = set()

    # Dijkstra
    while q:
        node = heapq.heappop(q)
        if node[0] == vertices[node[1]][0]: # valid key
            s.add(node)
            u = node[1]
            for adj in vertices[u][2]:
                w = adj[2]
                v = adj[1]
                if vertices[v][0] > vertices[u][0] + w:
                    vertices[v][0] = vertices[u][0] + w
                    heapq.heappush(q,(vertices[v][0],v)) # replace key
                    pred[v] = [adj]
                elif vertices[v][0] == vertices[u][0] + w:
                    pred[v].append(adj)

    for v in vertices:
        if v in pred:
            for e in pred[v]:
                u = e[0]
                if u not in succ:
                    succ[u] = []
                succ[u].append(e)

    nv = len(pred)

    counts = dict()
    scounts = dict()

    for e in edges:
        counts[e] = dict()
        scounts[e] = dict()

    totals = dict()

    for v in vertices:

        if v in pred:
            for kk in pred[v]:
                scounts[kk][v] = 1

    for v in vertices:
        totals[v] = 0.0
        if v in pred:
            for e in pred[v]:
                countroutes(v, e, source)
                totals[v] += counts[e][v]
        if source in succ:
            for e in succ[source]:
                countr2(v, e, source)

    edgecounts = len(edges)*[0]

    for e in edges:
        edgecounts[e[3]] = 0.0

    for v in vertices:
        for e in edges:
            i = e[3]
            u = e[0]
            if v in counts[e] and v in scounts[e]:
                edgecounts[i] = edgecounts[i] + (0.0 + counts[e][v]*scounts[e][v]) / totals[v] / (nv)
    
    return ' '.join(map(lambda x: '%(#)0.7f' % {'#' : x}, edgecounts))


file = sys.stdin

n = int(file.readline())
buffer = file.read().split()

for i in range(n):

    print "Case #" + str(i+1) + ":",
    print compute()
