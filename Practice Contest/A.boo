# Problem: Old Magician
# Language: Boo
# Author: KirarinSnow
# Usage: booi thisfile.boo <input.in >output.out 


for i in range(1, int.Parse(gets())+1):
    b = int.Parse(gets().Split()[1])
    print "Case #$i: $(['WHITE', 'BLACK'][b%2])"
