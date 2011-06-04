// Problem: Spinning Blade
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string>

using namespace std;

int mb[500][500][3];
int m[3];
int s[500][500][3];
int g[500][500];

string compute()
{
    int r, c, d;
    cin >> r >> c >> d;
    for (int i = 0; i < r; i++)
    {
	for (int j = 0; j < c; j++)
	{
	    char ch;
	    cin >> ch;
	    g[i][j] = (int)ch - 48;
	}
    }
    for (int i = 0; i < r; i++)
    {
	for (int j = 0; j < c; j++)
	{
	    int mi = g[i][j] + d;
	    mb[i][j][0] = mi;
	    mb[i][j][1] = i*mi;
	    mb[i][j][2] = j*mi;
	}
    }
    for (int k = 0; k < 3; k++)
    {
	for (int i = 0; i < r; i++)
	{
	    for (int j = 0; j < c; j++)
	    {
		if (i == 0 && j == 0)
		    s[i][j][k] = mb[i][j][k];
		else if (i == 0)
		    s[i][j][k] = s[i][j-1][k] + mb[i][j][k];
		else if (j == 0)
		    s[i][j][k] = s[i-1][j][k] + mb[i][j][k];
		else
		    s[i][j][k] = s[i-1][j][k] + s[i][j-1][k]
			         - s[i-1][j-1][k] + mb[i][j][k];
	    }
	}
    }
    int tm = -1;
    for (int r1 = 0; r1 < r; r1++)
    {
	for (int c1 = 0; c1 < c; c1++)
	{
	    for (int r2 = r1+2; r2 < r; r2++)
	    {
		if (c1 + (r2-r1) < c)
		{
		    int c2 = c1 + r2 - r1;
		    for (int k = 0; k < 3; k++)
		    {
			m[k] = s[r2][c2][k];
			if (r1 >= 1)
			{
			    m[k] -= s[r1-1][c2][k];
			    if (c1 >= 1)
			    {
				m[k] += s[r1-1][c1-1][k];
			    }
			}
			if (c1 >= 1)
			{
			    m[k] -= s[r2][c1-1][k];
			}
			
			m[k] -= mb[r1][c1][k] + mb[r1][c2][k]
			        + mb[r2][c1][k] + mb[r2][c2][k];
			if (m[0] > 0 && (r1+r2)*m[0] == 2*m[1]
			             && (c1+c2)*m[0] == 2*m[2])
			{
			    if (r2-r1+1 > tm)
			    {
				tm = r2-r1+1;
			    }
			}
		    }
		}
	    }
	}
    }
    if (tm < 0)
    {
	cout << "IMPOSSIBLE" << endl;
    }
    else
    {
	cout << tm << endl;
    }
}

int main()
{
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++)
    {
	cout << "Case #" << i << ": ";
	compute();
    }
    
    return 0;
}
