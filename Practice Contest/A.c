/* 
 * Problem: Old Magician
 * Language: C
 * Author: KirarinSnow
 * Usage: gcc thisfile.c -o executable
 *        ./executable <input.in >output.out
 */

#include <stdio.h>

void solve()
{
  int b, w;
  scanf("%d %d",&b,&w);

  if (w % 2 == 0)
  {
    printf("WHITE");
  }
  else
  {
    printf("BLACK");
  }
}

int main()
{
  int cases;
  scanf("%d",&cases);

  int i;
  for (i = 1; i <= cases; i++)
  {
    printf("Case #%d: ", i);
    solve();
    printf("\n");
  }

  return 0;
}
