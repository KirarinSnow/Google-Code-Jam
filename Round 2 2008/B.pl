#!/usr/bin/perl
#
# Problem: Triangle Areas
# Language: Perl
# Author: KirarinSnow
# Usage: perl thisfile.pl <input.in >output.out


sub compute()
{
    ($n, $m, $a) = split(/ /, <>);
       
    if ($a > $n * $m)
    {
	return "IMPOSSIBLE";
    }
    else
    {
	$x = ($a - 1)%$n + 1;
	$y = ($a - 1)/$n + 1;
	return sprintf("0 1 $n 0 $x %d", $y);
    }
}

$cases = <>;

for ($i = 1; $i <= $cases; $i++)
{
    $o = compute();
    print "Case #$i: $o\n";
}
