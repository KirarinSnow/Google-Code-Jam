// Problem: PermRLE
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <iostream>

using namespace std;

const int MAX = 16;
const int INTMAX = 100000000;

int D[1<<MAX][MAX];
int G[MAX][MAX];


int compute()
{
    int k;
    cin >> k;
    string s;
    cin >> s;
    int len = s.length();

    int min = INTMAX;
    // over all fixed start positions
    for (int start = 0; start < k; start++)
    {
	// construct graph
	for (int i = 0; i < k; i++)
	{
	    for (int j = 0; j < k; j++)
	    {
		if (i == j)
		{
		    G[i][j] = 0;
		    continue;
		}
		
		// edge weight i -> j
		int cost = 0;
		if (j == start) // connecting to next block
		{
		    for (int iter = 0; iter+k < len; iter+=k)
		    {
			if (s[iter+i] != s[iter+k+j]) // different char, next
			{
			    cost++;
			}
		    }
		    cost++; // end wraparound
		}
		else // normal
		{
		    for (int iter = 0; iter < len; iter+=k)
		    {
			if (s[iter+i] != s[iter+j]) // different char
			{
			    cost++;
			}
		    }
		}
		G[i][j] = cost;
	    }
	}

	// compute shortest Hamiltonian cycle
	for (int V = 0; V < (1<<k); V++) // set of visited vertices
	{
	    for (int end = 0; end < k; end++)
	    {
		if (V == 0) // empty set
		{
		    if (end == start) // path is 0
		    {
			D[V][end] = 0;
		    }
		    else // path impossible
		    {
			D[V][end] = INTMAX;
		    }
		}
		else if ((V | (1<<end))!=V) // end not in set V
		{
		    D[V][end] = INTMAX;
		}
		else // non-empty set containing end
		{
		    int minp = INTMAX;
		    int bitcount = 0;
		    for (int c = 0; c < k; c++)
		    {
			if ((V>>c)%2 == 1) // contains c-th vertex
			{
			    bitcount++;
			    if (c == end) continue;
			    int costp = D[V^(1<<end)][c] + G[c][end];
			    if (costp < minp)
			    {
				minp = costp;
			    }
			}
		    }
		    D[V][end] = minp;
		    if (bitcount == 1) // path to first vertex
		    {
			D[V][end] = G[start][end];
		    }
		}
	    }
	}
	int newmin = D[(1<<k)-1][start];
	if (newmin < min) min = newmin;
    }
    return min;
}


int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
    {
	printf("Case #%d: %d\n", i, compute());
    }
    
    return 0;
}
