<?php

# Problem: Old Magician
# Language: PHP
# Author: KirarinSnow
# Usage: php thisfile.php <input.in >output.out 

function compute()
{
    fscanf(STDIN, "%d %d\n", $w, $b);
    if ($b % 2 == 1)
    {
	return "BLACK";
    }
    else
    {
	return "WHITE";
    }
}

fscanf(STDIN, "%d\n", $cases);

for ($i = 1; $i <= $cases; $i++)
{
    $o = compute();
    echo "Case #$i: $o\n";
}

?>
