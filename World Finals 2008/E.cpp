// Problem: The Year of Code Jam
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <vector>
#include <deque>
#include <string.h>


using namespace std;


char grid[52][52];
int E[52*52+2][5];
int C[52*52+2][52*52+2];
int F[52*52+2][52*52+2];
int P[52*52+2];
int M[52*52+2];
int n, m;

const int MAX = 1<<20;


int solve()
{
    cin >> n >> m;
    memset(E, 0, sizeof(E));
    memset(C, 0, sizeof(C));

    int nn = n+3;
    int mm = m+3;
    if (n%2 == 0)
	nn--;
    if (m%2 == 0)
	mm--;

    int s = nn*mm;
    int t = s+1;
    
    for (int i = 0; i < nn; i++)
    {
	for (int j = 0; j < mm; j++)
	{
	    if (i == 0 || i > n || j == 0 || j > m)
	    {
		grid[i][j] = '.';
	    }
	    else
	    {
		cin >> grid[i][j];
	    }
	    
	    if (grid[i][j] != '?' && (i+j)%2 == 1)
	    {
		grid[i][j] = grid[i][j] == '#' ? '.' : '#';
	    }
	}	
    }

    vector<int> left;
    
    for (int i = 0; i < nn ; i++)
    {
	for (int j = 0; j < mm; j++)
	{
	    if (grid[i][j] == '#')
	    {
		left.push_back(i*mm+j);
		C[s][i*mm+j] = MAX;
	    }
	    else if (grid[i][j] == '.')
	    {
		E[i*mm+j][4] = t;
		C[i*mm+j][t] = MAX;
	    }
	    
	    for (int z = 0; z < 4; z++)
	    {
		int x = (z/2) + (z%2) - 1 + i;
		int y = (z/2) - (z%2) + j;
		x += nn; x %= nn;
		y += mm; y %= mm;
		E[i*mm+j][z] = x*mm+y;
		C[i*mm+j][x*mm+y] = 1;
	    }
	}
    }

    int f = 0;
    int r = 0;
    memset(F, 0, sizeof(F));

    while (true)
    {
	memset(P, -1, sizeof(P));
	P[s] = -2;
	memset(M, 0, sizeof(M));
	M[s] = MAX;
	
	deque<int> q;
	q.push_back(s);
	while (q.size() > 0)
	{
	    int u = q.front();
	    q.pop_front();

	    vector<int> next;
	    if (u == s)
	    {
		next = left;
	    }
	    else
	    {
		for (int j = 0; j < 4; j++)
		{
		    next.push_back(E[u][j]);
		}
		if (E[u][4] == t)
		{
		    next.push_back(t);
		}
	    }
	    for (int j = 0; j < next.size(); j++)
	    {
		int v = next[j];
		int cmf = C[u][v] - F[u][v];
		if (cmf > 0 && P[v] == -1)
		{
		    P[v] = u;
		    M[v] = M[u] <= cmf ? M[u] : cmf;
		    if (v != t)
		    {
			q.push_back(v);
		    }
		    else
		    {
			r = M[t];
			goto resume;
		    }
		}
	    }
	}
	r = 0;
	
    resume:
	if (r == 0)
	    break;
	f += r;
	int v = t;
	while (v != s)
	{
	    int u = P[v];
	    F[u][v] += r;
	    F[v][u] -= r;
	    v = u;
	}	
    }
    
    return 2*nn*mm-f;
}


int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
	cout << "Case #" << i << ": " << solve() << endl;
    
    return 0;
}
