#!/usr/bin/ruby
#
# Problem: Mine Layer
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out


def compute()
  r, c = readline.split.map(&:to_i)
  v = []
  g = []
  t = []
  (1 .. r).each do |l|
    l = readline.split.map(&:to_i)
    v.push(l)
    if c % 3 == 1 then
      i = 0
    else
      i = 1
    end
    s = 0
    (i ... c).step(3).each do |j|
      s += l[j]
    end
    g.push(s)
    t.push(nil)
  end

  t[2] = g[1] - g[0]
  (5 ... r).step(3).each do |j|
    t[j] = g[j-1] - g[j-2] + t[j-3]
  end
  t[r-3] = g[r-2] - g[r-1]
  (6 .. r).step(3).each do |j|
    t[r-j] = g[r-j+1] - g[r-j+2] + t[r-j+3]
  end

  if t[r/2] then
    return t[r/2]
  else
    return g[r/2] - t[r/2+1] - t[r/2-1]
  end
end

(1 .. gets.to_i).each do |i|
  puts "Case \##{i}: #{compute}"
end
