#!/usr/bin/perl
#
# Problem: Triangle Trilemma
# Language: Perl
# Author: KirarinSnow
# Usage: perl thisfile.pl <input.in >output.out


$n = <>;

for ($i = 1; $i <= $n; $i+=1)
{
    print "Case #$i: ";
    
    $line = <>;
    ($x1,$y1,$x2,$y2,$x3,$y3) = split(/\s+/, $line);
    
    $s12 = sqrt(($x1-$x2)**2 + ($y1-$y2)**2);
    $s13 = sqrt(($x1-$x3)**2 + ($y1-$y3)**2);
    $s23 = sqrt(($x2-$x3)**2 + ($y2-$y3)**2);

    if ($s12 == 0 || $s13 == 0 || $s23 == 0)
    {
	print "not a triangle\n";
    }
    else
    {
	$a1 = ( $s23**2 - $s12**2 - $s13**2 ) / (-2 * $s12 * $s13);
	$a2 = ( $s13**2 - $s12**2 - $s23**2 ) / (-2 * $s12 * $s23);
	$a3 = ( $s12**2 - $s13**2 - $s23**2 ) / (-2 * $s23 * $s13);
	if (check($a1 - 1) || check($a2 -1) || check($a3 -1))
	{
	    print "not a triangle\n";
	}
	else
	{
	    if (check($s12 - $s13) || check($s13 - $s23) || check($s12 - $s23))
	    {
		print "isosceles ";
	    }
	    else
	    {
		print "scalene ";
	    }
	    
	    if (check($a1) || check($a2) || check ($a3))
	    {
		print "right ";
		
	    }
	    elsif ($a1 < 0 || $a2 < 0 || $a3 < 0)
	    {
		print "obtuse ";
	    }
	    else
	    {
		print "acute ";
	    }

	    print "triangle\n";
	}
    }
}

sub check {
    $a = shift;
    if ($a < 10**(-5) && $a > -10**(-5))
    {
	return 1;
    }
    else
    {
	return 0;
    }
}
