// Problem: Ping Pong Balls
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <iostream>
#include <set>
#include <vector>

using namespace std;


long long int w, h, vx1, vy1, vx2, vy2, x0, y0;

bool inbounds(long long int x, long long int y)
{
    long long int tx = x0 + x*vx1 + y*vx2;
    long long int ty = y0 + x*vy1 + y*vy2;
    if ((tx < 0) || (tx >= w) || (ty < 0) || (ty >= h))
	return false;
    return true;
}

long long int compute()
{
    cin >> w >> h >> vx1 >> vy1 >> vx2 >> vy2 >> x0 >> y0;
    
    if (vx1*vy2 == vx2*vy1)
    {
	long long int c = 0;
	set<pair<long long int, long long int> > v;
	vector<pair<long long int, long long int> > q;
	q.push_back(make_pair(x0, y0));

	while (q.size() > 0)
	{
	    pair<long long int, long long int> p = q.back();
	    q.pop_back();
	    long long int x = p.first;
	    long long int y = p.second;
	    if (v.find(make_pair(x, y)) == v.end())
	    {
		v.insert(make_pair(x, y));
		if ((x+vx1 >= 0) && (x+vx1 < w) &&
		    (y+vy1 >= 0) && (y+vy1 < h))
		    q.push_back(make_pair(x+vx1, y+vy1));
		if ((x+vx2 >= 0) && (x+vx2 < w) &&
		    (y+vy2 >= 0) && (y+vy2 < h))
		    q.push_back(make_pair(x+vx2, y+vy2));
	    }
	}
	return v.size();
    }
    else
    {
	long long int j, l, u, c;
	j = l = u = c = 0;
	while (inbounds(j, u+1))
	    u++;
	c += (u-l)+1;

	for(long long int j = 1; ; j++)
	{
	    while (!inbounds(j, l))
	    {
		l++;
		if (l > u)
		    return c;
	    }
	    if (inbounds(j,u))
		while (inbounds(j, u+1))
		    u++;
	    else
		while (!inbounds(j, u))
		    u--;
	    c += u-l+1;
	}	   
    }
}

int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
    {
	printf("Case #%d: %lld\n", i, compute());
    }
    
    return 0;
}
