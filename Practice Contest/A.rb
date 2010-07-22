#!/usr/bin/ruby
#
# Problem: Old Magician
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out


def compute()
  $w, $b = readline.split
  return $b.to_i % 2 == 0 ? 'WHITE' : 'BLACK'
end

for $i in 1 .. gets.to_i:
  print "Case \##$i: %s\n" % compute()
end
