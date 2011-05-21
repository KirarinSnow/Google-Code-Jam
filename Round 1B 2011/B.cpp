// Problem: Revenge of the Hot Dogs
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string.h>


using namespace std;

int P[1000000];
int Q[1000000];

void solve()
{
    int c, d;
    cin >> c >> d;
    memset(P, 0, sizeof(P));

    int s = 0;
    bool g = true;
    for (int i = 0; i < c; i++)
    {
	int p, v;
	cin >> p >> v;
	if (v > 1)
	    g = false;
	
	for (int k = 0; k < v; k++)
	{
	    P[s] = p;
	    if (s > 0)
	    {
		if (P[s] - P[s-1] < d)
		    g = false;
	    }
	    s++;
	}
    }
    if (g)
    {
	cout << "0" << endl;
	return;
    }	
    for (int i = 1; i < s; i++)
    {
	Q[i] = P[i]-P[i-1];
    }
    
    long long int l = 0LL;
    long long int u = 1000000000000LL;
    while (u - l > 0)
    {	
	long long int t = (u+l)/2;
	
	long double v = -t;
	int i;
	for (i = 1; i < s; i++)
	{
	    v = v - 2*(Q[i] - d);
	    if (v < -t)
	    {
		v = -t;
	    }
	    if (v > t)
	    {
		l = t + 1;
		break;
	    }
	}
	if (i == s)
	{
	    u = t;
	}
    }
    cout << u/2 << (u%2 == 1 ? ".5" : "") << endl;
}


int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
    {
	cout << "Case #" << i << ": ";
	solve();
    }
    
    return 0;
}
