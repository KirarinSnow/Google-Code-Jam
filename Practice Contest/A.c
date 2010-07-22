/* 
 * Problem: Old Magician
 * Language: C
 * Author: KirarinSnow
 * Usage: gcc thisfile.c -o executable && ./executable <input.in >output.out
 */


#include <stdio.h>

char* solve()
{
    int b, w;
    scanf("%d %d", &b, &w);
    
    return w % 2 == 0 ? "WHITE" : "BLACK";
}

int main()
{
    int cases;
    scanf("%d", &cases);

    int i;
    for (i = 1; i <= cases; i++)
    {
	printf("Case #%d: %s\n", i, solve());
    }
    
    return 0;
}
