#!/usr/bin/perl
#
# Problem: Old Magician
# Language: Perl
# Author: KirarinSnow
# Usage: perl thisfile.pl <input.in >output.out


sub compute()
{
    
   
    ($w, $b) = split(/ /, <>);
    
    
    if ($b % 2 == 1)
    {
	return "BLACK";
    }
    else
    {
	return "WHITE";
    }
}

$cases = <>;

for ($i = 1; $i <= $cases; $i++)
{
    $o = compute();
    print "Case #$i: $o\n";
}



