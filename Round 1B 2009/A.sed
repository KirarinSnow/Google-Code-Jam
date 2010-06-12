#!/bin/sed
#
# Problem: Decision Tree
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed < input.in > output.out



# Initiate case counter
1 {s/.*/0YX/; h; d}

# On line preceding decision tree, store decision tree to hold space
/^[0-9]\+$/ {
    # Increment case counter
    x
    s/99Y/Y00/
    s/9Y/Y0/
    s/8Y\(.*\)X/9\1ZX/
    s/7Y\(.*\)X/8\1ZX/
    s/6Y\(.*\)X/7\1ZX/
    s/5Y\(.*\)X/6\1ZX/
    s/4Y\(.*\)X/5\1ZX/
    s/3Y\(.*\)X/4\1ZX/
    s/2Y\(.*\)X/3\1ZX/
    s/1Y\(.*\)X/2\1ZX/
    s/0\?Y\(.*\)X/1\1ZX/
    s/ZX.*/YX/
    x

    # Print case number
    s/.*/Case /
    G
    y/\n/#/
    s/YX.*/:/
    p

    # Store decision tree to hold space
    s/.*//
    :p
    N
    /[()]/{
    y/()/<>/
    s/[ \n]\+//g}
    tp
    H
    d
}

# On lines corresponding to each animal, compute cuteness
s/^[a-z]\+ [0-9]\+ \?/ /
G
s/\n[^<]*//
s/[^<>]*$//
s/</ %</

# Recursive descent:
#   interchanges <...> and (...) to identify top level
#   removes incorrect branch based on matching of top-level feature
:c
s/<\([.0-9]\+\)\(.*\)>/\2@\1/
/%@/ {bd}

:b
/<[^<>]*>/ {
    s/T//
    s/<\([^<>]*\)>/T(\1)/
}
tb

/ \([a-z]\+\) .*%\1(/ {
    s/%[a-z]*(/%(/
    s/T.*)//
    by
}
s/%.*T/%/

:y
y/()/<>/
tc

# Descent complete: clean up; remove 1.0; strip leading '0.' from numbers
:d
s/[^@]*@/@/
s/@1[^@]*//g
s/@0./@/g

# Perform pairwise multiplication
:r
/@.*@/{
    s/@\([0-9]*\)@\([0-9]*\)$/@(\1@\2)/

    # For each digit in left operand
    :s
    s/(\([0-9]\)\(.*\))/\1(\2)~/
    s/"\([0-9]*\)/"\10/g

    # For each digit in right operand
    :t

    # Isolate digits to be multiplied
    s/\([0-9]\)(\(.*\)\([0-9]\))\(.*\)~/\1(\2)\3\4~\1\3/
    Tf

    # Order digits
    s/~10/~01/
    s/~2\([0-1]\)/~\12/
    s/~3\([0-2]\)/~\13/
    s/~4\([0-3]\)/~\14/
    s/~5\([0-4]\)/~\15/
    s/~6\([0-5]\)/~\16/
    s/~7\([0-6]\)/~\17/
    s/~8\([0-7]\)/~\18/
    s/~9\([0-8]\)/~\19/

    # Multiply digits
    s/~0[0-9]/`0'0/
    s/~1\([0-9]\)/`0'\1/
    s/~22/`0'4/
    s/~23/`0'6/
    s/~24/`0'8/
    s/~25/`1'0/
    s/~26/`1'2/
    s/~27/`1'4/
    s/~28/`1'6/
    s/~29/`1'8/
    s/~33/`0'9/
    s/~34/`1'2/
    s/~35/`1'5/
    s/~36/`1'8/
    s/~37/`2'1/
    s/~38/`2'4/
    s/~39/`2'7/
    s/~44/`1'6/
    s/~45/`2'0/
    s/~46/`2'4/
    s/~47/`2'8/
    s/~48/`3'2/
    s/~49/`3'6/
    s/~55/`2'5/
    s/~56/`3'0/
    s/~57/`3'5/
    s/~58/`4'0/
    s/~59/`4'5/
    s/~66/`3'6/
    s/~67/`4'2/
    s/~68/`4'8/
    s/~69/`5'4/
    s/~77/`4'9/
    s/~78/`5'6/
    s/~79/`6'3/
    s/~88/`6'4/
    s/~89/`7'2/
    s/~99/`8'1/
    s/`/~/
    bt

    # Perform carrying
    :f

    # Order digits
    s/~\([0-9]\)'/~\1/
    s/\([1-9]\)0'/0\1'/
    s/\([2-9]\)1'/1\1'/
    s/\([3-9]\)2'/2\1'/
    s/\([4-9]\)3'/3\1'/
    s/\([5-9]\)4'/4\1'/
    s/\([6-9]\)5'/5\1'/
    s/\([7-9]\)6'/6\1'/
    s/\([8-9]\)7'/7\1'/
    s/98'/89'/

    # Conjoin overlapping digits
    s/0\([0-9]\)'/\1/
    s/11'/2/
    s/12'/3/
    s/13'/4/
    s/14'/5/
    s/15'/6/
    s/16'/7/
    s/17'/8/
    s/18'/9/
    s/19'/1'0/
    s/22'/4/
    s/23'/5/
    s/24'/6/
    s/25'/7/
    s/26'/8/
    s/27'/9/
    s/28'/1'0/
    s/29'/1'1/
    s/33'/6/
    s/34'/7/
    s/35'/8/
    s/36'/9/
    s/37'/1'0/
    s/38'/1'1/
    s/39'/1'2/
    s/44'/8/
    s/45'/9/
    s/46'/1'0/
    s/47'/1'1/
    s/48'/1'2/
    s/49'/1'3/
    s/55'/1'0/
    s/56'/1'1/
    s/57'/1'2/
    s/58'/1'3/
    s/59'/1'4/
    s/66'/1'2/
    s/67'/1'3/
    s/68'/1'4/
    s/69'/1'5/
    s/77'/1'4/
    s/78'/1'5/
    s/79'/1'6/
    s/88'/1'6/
    s/89'/1'7/
    s/99'/1'8/
    tf

    # Go to next digit in left operand
    s/'//
    s/)\(.*\)~/\1)"/
    ts

    # Clean up
    s/"\([0-9]*\)0/+\1/g

    # Perform pairwise addition on resulting products
    :m
    /+.*+/ {
        s/+\([0-9]*\)$/<+\1>/

        # For each pair of digits
        :k 
        s/\([0-9]\)<\(.*\)\([0-9]\)>/<\2>\1\3/
        
        # Order digits
        s/>10/>01/
        s/>2\([0-1]\)/>\12/
        s/>3\([0-2]\)/>\13/
        s/>4\([0-3]\)/>\14/
        s/>5\([0-4]\)/>\15/
        s/>6\([0-5]\)/>\16/
        s/>7\([0-6]\)/>\17/
        s/>8\([0-7]\)/>\18/
        s/>9\([0-8]\)/>\19/
 
        # Add digits
        s/>0/=/
        s/>11/=2/
        s/>12/=3/
        s/>13/=4/
        s/>14/=5/
        s/>15/=6/
        s/>16/=7/
        s/>17/=8/
        s/>18/=9/
        s/>19/=,0/
        s/>22/=4/
        s/>23/=5/
        s/>24/=6/
        s/>25/=7/
        s/>26/=8/
        s/>27/=9/
        s/>28/=,0/
        s/>29/=,1/
        s/>33/=6/
        s/>34/=7/
        s/>35/=8/
        s/>36/=9/
        s/>37/=,0/
        s/>38/=,1/
        s/>39/=,2/
        s/>44/=8/
        s/>45/=9/
        s/>46/=,0/
        s/>47/=,1/
        s/>48/=,2/
        s/>49/=,3/
        s/>55/=,0/
        s/>56/=,1/
        s/>57/=,2/
        s/>58/=,3/
        s/>59/=,4/
        s/>66/=,2/
        s/>67/=,3/
        s/>68/=,4/
        s/>69/=,5/
        s/>77/=,4/
        s/>78/=,5/
        s/>79/=,6/
        s/>88/=,6/
        s/>89/=,7/
        s/>99/=,8/
        s/\([0-9+]\)=/\1>:/
        tk

        # Clean up
        s/<+//
        s/>+//
        s/://g

        # Perform carrying
        :l
        s/0,/1/
        s/1,/2/
        s/2,/3/
        s/3,/4/
        s/4,/5/
        s/5,/6/
        s/6,/7/
        s/7,/8/
        s/8,/9/
        s/9,/,0/
        tl

	# Clean up
        s/[<>]//g
        s/+,/+1/g
        /,/ {bl}
    }

    # Continue with next pairwise addition
    /+.*+/ {bm}
}

# Continue with next pairwise multiplication
s/@[0-9]*(@.*)+/@/
tr

# Append '0.' to result
s/@/0./

# 1.0 case
s/^$/1.0/