#!/usr/bin/perl
#
# Problem: Alien Numbers
# Language: Perl
# Author: KirarinSnow
# Usage: perl thisfile.pl <input.in >output.out


use POSIX qw(ceil floor);

$" = ' ';

$max = <>;

for ($n = 1; $n <= $max; $n++)
{
    print "Case #$n: ";
    $line = <>;
    chomp($line);
    @stuff = split(/ /, $line);
    @input = split(//, $stuff[0]);

    $inset = $stuff[1];
    $outset = $stuff[2];
    @outchars = split(//, $outset);
   
    $inbase = length($inset);
    $outbase = length($outset);

    $num = 0;
    for ($o = 0; $o <= $#input; $o++)
    {
	$num += index($inset, $input[$o])*($inbase**($#input - $o));
    }

    for ($j = floor(log($num)/log($outbase)); $j >=0; $j--)
    {
	print $outchars[floor($num/($outbase**$j))%$outbase];
    }

   print $/;
}
