#!/usr/bin/ruby
#
# Problem: Welcome to Code Jam
# Language: Ruby
# Author: KirarinSnow
# Usage: ruby thisfile.rb <input.in >output.out


def compute()
    $chars = readline.to_a[0]

    $ct = [0] * ($wc.length + 1)
    $ct[0] = 1
    
    for $j in 0 ... $chars.length
        $ch = $chars[$j]
	for $k in 0 ... $wc.length
            if $wc[$k] == $ch
                $ct[$k+1] = ($ct[$k] + $ct[$k+1])
                $ct[$k+1] %= 10000
            end
        end
    end

    return $ct[$wc.length]
end

$wc = 'welcome to code jam'.to_a[0]

for $i in 1 .. readline.to_i
    print "Case \##$i: %04d\n" % compute()
end
