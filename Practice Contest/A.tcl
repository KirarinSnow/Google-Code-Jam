#!/usr/bin/tcl
#
# Problem: Old Magician
# Language: Tcl
# Author: KirarinSnow
# Usage: tcl -f thisfile.tcl <input.in >output.out 


proc Compute {} {      
    set line [gets stdin]
    scan $line "%d %d" w b
    
    if {$b%2 == 0} {return "WHITE"} else {return "BLACK"}
}

set cases [gets stdin]

for {set i 1} {$i <= $cases} {incr i} {
    set sol [Compute]
    puts "Case #$i: $sol"
}
