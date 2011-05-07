#!/usr/bin/python
#
# Problem: Bot Trust
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: I really really wanted to submit a solution for A-small in a
#           language with a name starting with A, to complete the
#           abecedarian challenge. I tried it with ALGOL 68 and Arc, but
#           unfortunately failed on both, and now have run out of time.
#           I didn't even get to submit this one.


class Robot:
    def __init__(self, name, robots, buttons):
        self.next = 0
        self.pos = 1
        self.robots = robots
        self.buttons = buttons
        self.name = name

    def advance(self, pushed):
        try:
            self.next = self.robots.index(self.name)
            if not pushed and self.next == 0 and self.buttons[0] == self.pos:
                self.buttons.pop(0)
                self.robots.pop(0)
                return True
            else:
                self.pos += cmp(self.buttons[self.next], self.pos)
                return False
        except:
            return False
        

def compute():
    line = raw_input().split()
    n = int(line[0])

    robots = []
    buttons = []
    for j in range(1, 2*n, 2):
        robots.append(line[j])
        buttons.append(int(line[j+1]))

    blue = Robot('B', robots, buttons)
    orange = Robot('O', robots, buttons)
    count = 0
    
    while robots:
        orange.advance(blue.advance(False))
        count += 1
        
    return count
        

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
