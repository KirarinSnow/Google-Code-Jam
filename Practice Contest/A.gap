# Problem: Old Magician
# Language: GAP
# Author: KirarinSnow
# Usage: gap -b -q thisfile.py <input.in >output.out 


stdin := InputTextUser();
total := Int(Chomp(ReadLine(stdin)));

for i in [1 .. total] do;
    b := Int(SplitString(Chomp(ReadLine(stdin)), " ")[2]);
    if RemInt(b, 2) = 0 then
        ans := "WHITE";
    else
        ans := "BLACK";
    fi;
    Print("Case #", i, ": ", ans, "\n");
od;

QUIT;
