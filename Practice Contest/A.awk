#!/usr/bin/awk
#
# Problem: Old Magician
# Language: awk
# Author: KirarinSnow
# Usage: awk -f thisfile.awk <input.in >output.out

BEGIN { c=0; }

/ / { c+=1;
       if ($2%2==1) {print "Case #"c": BLACK";} 
       else {print "Case #"c": WHITE";}
}