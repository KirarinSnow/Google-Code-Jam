// Problem: Square Math
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;
typedef pair<pair<int, int>, int> state;

char b[20][20];

state st(int i, int j, int v)
{
    return make_pair(make_pair(i, j), v);
}

void solve()
{
    int w, q;
    cin >> w >> q;

    for (int i = 0; i < w; i++)
    {
	for (int j = 0; j < w; j++)
	{
	    cin >> b[i][j];
	}
    }
    vector<int> qs;
    set<int> qss;
    for (int i = 0; i < q; i++)
    {
	int t;
	cin >> t;
	qs.push_back(t);
	qss.insert(t);
    }
    
    map<int, string> a;
    int h = 1<<20;
    int cs = qss.size();
    
    set<state> s;
    queue<state> r;
    map<state, string> d;
    
    for (int i = 0; i < w; i++)
    {
	for (int j = 0; j < w; j++)
	{
	    if (b[i][j] >= '0')
	    {
		state t = st(i, j, (int)b[i][j]-48);
		string ss = "";
		ss += b[i][j];
		d.insert(pair<state, string>(t, ss));
		r.push(t);
	    }
	}
    }
    
    while (!r.empty())
    {
	state u = r.front();
	r.pop();
        string dd = d.find(u)->second;
	if (dd.length() > h)
	    break;
	if (s.find(u) != s.end())
	    continue;
	s.insert(u);
	int i = u.first.first;
	int j = u.first.second;
	int v = u.second;
	if (qss.find(v) != qss.end())
	{
	    if (a.find(v) != a.end())
	    {
		string av = a.find(v)->second;
		if (dd.length() <= av.length() && dd.compare(av) <= 0)
		{
		    a[v] = dd;
		}
	    }
	    else
	    {
		a[v] = dd;
	    }
	    if (a.size() == cs)
	    {
		h = dd.length();
	    }
	}

	for (int x1 = -1; x1 <= 1; x1++)
	{
	    for (int y1 = -1; y1 <= 1; y1++)
	    {
		if (x1+y1 == 1 || x1+y1 == -1)
		{
		    for (int x2 = -1; x2 <= 1; x2++)
		    {
			for (int y2 = -1; y2 <= 1; y2++)
			{
			    if (x2+y2 == 1 || x2+y2 == -1)
			    {   
				int ii = i+x1+x2;
				int jj = j+y1+y2;
				if (i+x1 >= 0 && i+x1 < w &&
				    j+y1 >= 0 && j+y1 < w &&
				    ii >= 0 && ii < w &&
				    jj >= 0 && jj < w)
				{
				    string e = dd;
				    e += b[i+x1][j+y1];
				    e += b[ii][jj];
				    int c = v;
				    if (b[i+x1][j+y1] == '-')
				    {
					c -= (int)b[ii][jj]-48;
				    }
				    else
				    {
					c += (int)b[ii][jj]-48;
				    }
				    state next = st(ii, jj, c);
				    if (d.find(next) != d.end())
				    {
					string ns = d.find(next)->second;
					if (e.length() <= ns.length() &&
					    e.compare(ns) < 0)
					{
					    d[next] = e;
					}
				    }
				    else
				    {
					d[next] = e;
				    }
				    r.push(next);
				}
			    }
			}
		    }
		}
	    }
	}
    }

    for (int i = 0; i < qs.size(); i++)
    {
	cout << a[qs[i]] << endl;
    }
}


int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
    {
	cout << "Case #" << i << ":" << endl;
	solve();
    }
    
    return 0;
}
