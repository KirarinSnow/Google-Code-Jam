#!/usr/bin/env python
#
# Problem: Watersheds
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():
    def nxt(sink):
        r, c = sink
        mn = mp[r][c]
        dest = False
        if (r > 0 and mp[r-1][c] < mn):
            mn = mp[r-1][c]
            dest = (r-1, c)
        if (c > 0 and mp[r][c-1] < mn):
            mn = mp[r][c-1]
            dest = (r, c-1)
        if (c < w-1 and mp[r][c+1] < mn):
            mn = mp[r][c+1]
            dest = (r, c+1)
        if (r < h-1 and mp[r+1][c] < mn):
            mn = mp[r+1][c]
            dest = (r+1, c)
        return dest

    def label(sink, lt):
        q = [sink]
        while q:
            r, c = q.pop(0)
            if out[r][c] == 0:
                out[r][c] = lt
                if (r > 0 and nxt((r-1, c)) == (r, c)):
                    q.append((r-1, c))
                if (c > 0 and nxt((r, c-1)) == (r, c)):
                    q.append((r, c-1))
                if (c < w-1 and nxt((r, c+1)) == (r, c)):
                    q.append((r, c+1))
                if (r < h-1 and nxt((r+1, c)) == (r, c)):
                    q.append((r+1, c))
            

    h, w = map(int, raw_input().split())
    mp = [map(int, raw_input().split()) for i in range(h)]

    out = table(h, w)

    lt = 97
    for r in range(h):
        for c in range(w):
            if out[r][c] == 0:
                # find sink
                sink = (r, c)
                while nxt(sink):
                    sink = nxt(sink)
                # BFS
                label(sink, lt)
                lt += 1

    s = ''
    for r in range(h):
        s += '\n' + ' '.join([chr(min(122, out[r][c])) for c in range(w)])
    return s
        
for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
