// Problem: Doubly-sorted Grid
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

const int MOD = 10007;

int d[1<<20][26][11];
bool b[1<<20][26][11];
char g[10][10];

int row, col;


int dp(int p, int c, int k)
{
    if (b[p][c][k] == false)
    {
	int t = 0;
	if (p == (((1<<row)-1)<<col))
	{
	    t = 1;
	}
	else
	{
	    if (k < 0)
	    {
		if (c != 0)
		{
		    t += dp(p, c-1, col-1);
		}
	    }
	    else
	    {	
		t += dp(p, c, k-1);
		
		int pp = p;
		int x = col;
		int y = 0;
		int z = 0;
		while (x > k)
		{
		    if (pp%2 == 0)
		    {
			x--;
		    }
		    else
		    {
			z++;
		    }
		    y++;
		    pp /= 2;
		}
		
		
		if ((y >= 2) && (((p%(1<<y))>>(y-2)) == 1))
		{
		    char ch = g[z-1][k];
		    if (ch == '.' || ch == (char)((int)'a'+c))
		    {
			int flip = (pp << y) + (2 << (y-2)) + (p%(1<<(y-2)));
			t += dp(flip, c, k);
		    }
		}
		
	    }
	}
	d[p][c][k] = t%MOD;
	b[p][c][k] = true;
    }
    return d[p][c][k];
}

int solve()
{
    memset(d, 0, sizeof d);
    memset(b, false, sizeof b);
    memset(g, 0, sizeof g);

    cin >> row >> col;

    for (int i = 0; i < row; i++)
    {
	for (int j = 0; j < col; j++)
	{
	    cin >> g[i][j];
	}
    }

    return dp((1<<row)-1, 25, col-1);
}

int main()
{
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++)
    {
	printf("Case #%d: %d\n", i, solve());
    }
    
    return 0;
}
