#!/usr/bin/ruby
#
# Problem: Ping Pong Balls
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out
# Comments: Times out on large.


def txc(x, y)
  return $x0 + x*$vx1 + y*$vx2
end
  
def tyc(x, y)
  return $y0 + x*$vy1 + y*$vy2
end

def inbounds(x, y)
  tx = txc(x, y)
  ty = tyc(x, y)
  if (tx < 0) or (tx >= $w) or (ty < 0) or (ty >= $h) then
    return false
  end
  return true
end
   
def compute()
  $w, $h = readline.split.map(&:to_i)
  $vx1, $vy1 = readline.split.map(&:to_i)
  $vx2, $vy2 = readline.split.map(&:to_i)
  $x0, $y0 = readline.split.map(&:to_i)
 
  if $vx1*$vy2 - $vx2*$vy1 == 0 then
    v = Hash.new
    q = [[$x0, $y0]]

    while q.length > 0
      x, y = q.pop
      if v[[x, y]] == nil then
        v[[x, y]] = 1
        if (x+$vx1 >= 0) and (x+$vx1 < $w) and
            (y+$vy1 >= 0) and (y+$vy1 < $h) then
          q.push([x+$vx1, y+$vy1])
        end
        if (x+$vx2 >= 0) and (x+$vx2 < $w) and
            (y+$vy2 >= 0) and (y+$vy2 < $h) then
          q.push([x+$vx2, y+$vy2])
        end
      end
    end
    return v.length
    
  else
    j = 0
    l = 0
    u = 0
    c = 0
    while inbounds(j, u+1)
      u += 1
    end
    c += (u-l)+1

    j += 1
    while true
      while not inbounds(j, l)
        l += 1
        if l > u
          return c
        end
      end

      if inbounds(j, u) then
        while inbounds(j, u)
          u += 1
        end
        u -= 1
      else
        while not inbounds(j, u)
          u -= 1
        end
      end

      c += u-l+1
      j += 1
    end
  end
end

for $i in 1 .. gets.to_i:
    print "Case \##$i: %s\n" % compute()
end
