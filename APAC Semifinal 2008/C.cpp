// Problem: Millionaire
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <iostream>

using namespace std;

const int MAX = 1000000;

double d[16][(1<<15)+1];

double solve()
{
    int m;
    double p, x;
  
    cin >> m >> p >> x;
    
    if (x >= MAX) return 1.0;
    if (x < 1.0/(1<<m)) return 0.0;

    d[0][1] = 1.0;
    for (int j = 1; j <= m; j++)
    {
	d[j][1<<j] = 1.0;
	for (int i = 1; i < (1<<j); i++)
	{
	    double c = 0.0;
	    for (int k = (i+1)/2; k <= (1<<(j-1)); k++)
	    {
		if (i-k >= 0)
		{
		    double t = p*d[j-1][k] + (1-p)*d[j-1][i-k];
		    if (t > c) c = t;
		}
	    }
	    d[j][i] = c;
	}
    }

    return d[m][(int)((1<<m)*(x/MAX))];
    
}

int main()
{
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++)
    {
      printf("Case #%d: %0.6f\n", i, solve());
    }
    
    return 0;
}
