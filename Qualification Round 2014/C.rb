#!/usr/bin/ruby
#
# Problem: Minesweeper Master
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out


(1 .. gets.to_i).each do |x|
  puts "Case \##{x}:"
  r, c, m = readline.split.map(&:to_i)
  
  tr = false
  if r > c then
    tr = true
    r, c = c, r
  end
  
  f = Array.new(r){['*']*c}
  v = r*c-m
  
  possible = true
  if v == 0 then
    possible = false
  elsif v == 1 then
    f[0][0] = '.'
  else
    if r == 1 then
      v.times do |i|
        f[0][i] = '.'
      end
    elsif r == 2 then
      if v%2 == 0 and v >= 4 then
        (v/2).times do |i|
          f[0][i] = f[1][i] = '.'
        end
      else
        possible = false
      end
    else
      if v == 4 or v == 6 then
        (v/2).times do |i|
          2.times do |j|
            f[i][j] = '.'
          end
        end
      elsif v <= 7 then
        possible = false
      else
        if v <= 2*c+3 then
          (v/2-1).times do |j|
            f[0][j] = f[1][j] = '.'
          end
          f[2][0] = f[2][1] = '.'
          if v%2 == 1 then
            f[2][2] = '.'
          end
        else
          v.times do |i|
            f[i/c][i%c] = '.'
          end
          if v%c == 1 then
            f[v/c][1] = '.'
            f[v/c-1][c-1] = '*'
          end
        end
      end
    end
  end
  
  if possible then
    f[0][0] = 'c'
    if tr then
      f = f.transpose
    end
    puts f.map(&:join)
  else
    puts "Impossible"
  end
end
