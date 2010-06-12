#!/usr/bin/ruby
#
# Problem: Old Magician
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out


def compute()
	$w, $b = $file.readline.split
	if $b.to_i % 2 == 0
		return 'WHITE'
	else
		return 'BLACK'
	end
end

$file = open('/dev/stdin')
$cases =  $file.readline.to_i

for $i in 1 .. $cases:
	print "Case \##$i: "
	print compute()
	print "\n"
end


