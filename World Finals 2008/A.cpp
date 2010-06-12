// Problem: Juice
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>

int a[5000], b[5000], c[5000], h[10002], v[10002];

int solve()
{
  int n;
  scanf("%d", &n);
  
  for (int i = 0; i < n; i++)
  {
    scanf("%d %d %d", a+i, b+i, c+i);
  }
  
  int m = 0;
  for (int cc = 0; cc <= 10000; cc++)
  {
    for (int kk = 0; kk < 10002; kk++)
    {
      h[kk] = 0;
      v[kk] = 0;
    }
    for (int j = 0; j < n; j++)
    {
      if (c[j] <= cc && a[j] + b[j] + cc <= 10000)
      {
	h[b[j]]+=1;
	v[a[j]]+=1;
      }
    }
    int q = 0;
    for (int aa = -1; aa < 10000-cc; aa++)
    {
      q += v[aa+1] - h[10000-cc-aa];
      if (q > m) m = q;
    }
  }
  return m;
}


int main()
{
  int cases;
  scanf("%d",&cases);

  for (int i = 1; i <= cases; i++)
  {
    printf("Case #%d: %d\n", i, solve());
  }

  return 0;
}
