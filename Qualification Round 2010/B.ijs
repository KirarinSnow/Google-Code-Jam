NB. Problem: Fair Warning
NB. Language: J
NB. Author: KirarinSnow
NB. Usage: jc thisfile.ijs <input.in >output.out

NB. Comments: J can be downloaded for free at http://jsoftware.com/
NB.           The solutions to all cases are computed on the second line
NB.           (using no intermediate variables and no alphabetic characters).
NB.           The third line handles the formatted output. This could
NB.           probably be done on just one line without needing to use
NB.           'printf', but it's already given me enough of a headache.
NB.           Also, this (most likely) won't work on the large set. J's
NB.           big ints are just not cool enough.


load 'printf'
s=.(+./@([-<./)|-@(0{[))@}.@".&.>}.<;._2]1!:1[3
exit(;($s)#<'Case #%d: %d\n')printf;|:(>:i.$s),:;s


NB. What the above does:
NB. Read in lines. Discard first line (number of cases). For each line,
NB. evaluate string to obtain integers; ignore first integer; subtract
NB. the minimum from all elements; compute the gcd; take modulo(-min, gcd).
NB. Assign resulting values to s; print s with corresponding case numbers.
