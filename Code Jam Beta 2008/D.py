#!/usr/bin/python
#
# Problem: Hexagon Game
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Requires the munkres module: http://bmc.github.com/munkres/



from munkres import Munkres

def solve(s, init, val, final, pos):
    # get distances
    dist = []
    for i in range(s):
        ir, ic = pos[init[i]]
        ic = ic + max(0, ir-(s-1)/2)
        dist.append([])
        for j in range(s):
            jr, jc = final[j]
            jc = jc + max(0, jr-(s-1)/2)

            d = abs(ir - jr)

            if d == 0:
                d = abs(ic - jc)
            else:
                if jr > ir:
                    minc = ic
                    maxc = ic + (jr-ir)
                else:
                    maxc = ic
                    minc = ic - (ir-jr)
            
                if jc < minc:
                    d += minc-jc
                elif jc > maxc:
                    d += jc-maxc
                
            dist[i].append(d * val[i])

    
    # Hungarian algorithm, via munkres module
    total = 0
    for r, c in Munkres().compute(dist):
        total += dist[r][c]
    
    return total


def compute():
    init = map(int, raw_input().split())
    val = map(int, raw_input().split())
    s = len(init)

    pos = [0]
    rows = range((s+1)/2, s+1) + range((s+1)/2, s)[::-1]
    for i in range(1, (3*s*s+1)/4+1):
        # get position
        row = 0
        while i > rows[row]:
            i -= rows[row]
            row += 1
        pos.append((row, i))

    sols = [solve(s, init, val, final, pos) for final in [
            [((s-1)/2, x+1) for x in range(s)], # horizontal
            [(x, min((s+1)/2, x+1)) for x in range(s)], # \ diag
            [(s-1-x, min((s+1)/2, x+1)) for x in range(s)]  # / diag
           ]]
    return min(sols)
    

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
