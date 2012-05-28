// Problem: Marbles
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out
// Comments: Indirect adaptation from reference solution.


#include <cstdio>
#include <iostream>
#include <string.h>
#include <map>

using namespace std;

int MAX = 1<<20;
int cache[1000][501];
int evcache[1000][1000][2];
int evsize[1000];
int vis[500];
int n = 0;
int marbles[1000];
int where[500][2];

bool cross(int m1, int m2) 
{
    bool b =
	(where[m1][0] < where[m2][0] &&
	 where[m2][0] < where[m1][1] &&
	 where[m1][1] < where[m2][1]) ||
	(where[m2][0] < where[m1][0] &&
	 where[m1][0] < where[m2][1] &&
	 where[m2][1] < where[m1][1]);
    return b;
}

void dfs(int m, int sign) 
{
    if (vis[m] == sign) return;
    if (vis[m] == -sign) throw 0;
    vis[m] = sign;
    for (int i = 0; i < n; i++) 
    {
	if (i != m && cross(m, i)) {
	    dfs(i, -sign);
	}
    }
}

void events(int startx) 
{
    if (evsize[startx] > 0) return;
    
    for (int i = 0; i < n; i++) vis[i] = 0;
    
    dfs(marbles[startx], 1);
    int xp = 0;
    for (int x = 0; x < 2*n; x++) 
    {
	int m = marbles[x];
	if (vis[m] == 0) continue;
	int nr = 0;
	if (where[m][nr] != x) nr += 1;
	
	evcache[startx][xp][0] = x;
	evcache[startx][xp][1] = 1-vis[m]+nr;
	xp++;
    }
    evsize[startx] = xp;
    return;
}

int h2(int a, int b, int h1) 
{
    if (h1 < 0) return MAX;
    if (a == b) return 0;
    int &res = cache[a][h1];
    if (res != -1) return res;
    
    events(a);
    int evs = evsize[a];
    
    res = MAX;
    for (int mask = 0; mask <= 2; mask += 2) 
    {
	int top = 0;
	int bot = 0;
	int H2 = 0;
	for (int i = 0; i <= evs; i++) 
	{
	    int alpha = (i == 0) ? a : evcache[a][i-1][0] + 1;
	    int beta = (i == evs) ? b : evcache[a][i][0];
	    
	    H2 = max(H2, h2(alpha, beta, h1-top) + bot);
	    if (i != evs) {
		switch (evcache[a][i][1] ^ mask) {
		case 0: ++top; break;
		case 1: --top; break;
		case 2: ++bot; break;
		case 3: --bot; break;
		}
	    }
	}
	res = min(res, H2);
    }
    return res;
}

int solve() 
{
    char b[30];
    cin >> n;
    
    map<string, int> d;
    int size = 0;
    
    for (int i = 0; i < 2*n; i++) 
    {
	int m = -1;
	scanf("%s", b);
	string z = b;
	map<string, int>::iterator it = d.find(z);
	if (it == d.end()) 
	{
	    m = size;
	    size++;
	    d[z] = m;
	    where[m][0] = i;
	}
	else 
	{
	    m = it->second;
	    where[m][1] = i;
	}
	marbles[i] = m;
    }
    
    for (int i = 0; i < 2*n; i++) 
    {
	for (int j = 0; j <= n; j++) 
	{
	    cache[i][j] = -1;
	}
	for (int j = 0; j < 2*n; j++) 
	{
	    evcache[i][j][0] = -1;
	    evcache[i][j][1] = -1;
	}
	evsize[i] = 0;
    }
    
    int res = MAX;
    try 
    {
	for (int h1 = 0; h1 <= n; h1++) 
	{
	    res = min(res, h1 + h2(0, 2*n, h1));
	}
    } 
    catch (int) 
    {
	return -1;
    }
    if (res == MAX) res = -1;
    return res;
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
