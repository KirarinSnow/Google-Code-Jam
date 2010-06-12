<?php

# Problem: Triangle Areas
# Language: PHP
# Author: KirarinSnow
# Usage: php thisfile.php < input.in > output.out 

function compute()
{
    fscanf(STDIN, "%d %d %d\n", $n, $m, $a);
    if ($a > $n * $m)
    {
	return "IMPOSSIBLE";
    }
    else
    {
	$x = ($a - 1)%$n + 1;
	$y = floor(($a - 1)/$n) + 1;
	return "0 1 $n 0 $x $y";
    }
}

fscanf(STDIN, "%d\n", $cases);

for ($i = 1; $i <= $cases; $i++)
{
    $o = compute();
    echo "Case #$i: $o\n";
}

?>
