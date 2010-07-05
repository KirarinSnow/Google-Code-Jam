// Problem: Shopping Plan
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <limits>
#include <list>
#include <math.h>
#include <float.h>
#include <vector>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

typedef pair<double, int> pdi;


class State
{
public:
    State() {}

    vector<int> neighbors;
    vector<double> weight;
};


const int MS = 101<<15;
State states[MS];
bool visited[MS];
double distances[MS];
int xs[MS];
int ys[MS];


int index(int store, bool perish, int mask, int ni)
{
    return ((2*store+(int)perish+1) << ni) + mask;
}

double dist(int index1, int index2)
{
    int x1 = xs[index1];
    int x2 = xs[index2];
    int y1 = ys[index1];
    int y2 = ys[index2];
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}


double solve()
{
    int ni, ns, pg;
    bool perish[15];
    
    vector<string> items;
    
    int xpos[50];
    int ypos[50];
    int mask[50];
    vector<int> prices[50];
    
    cin >> ni >> ns >> pg;
    
    
    // get items, perish
    for (int i = 0; i < ni; i++)
    {
	string f;
	cin >> f;
	perish[i] = false;
	if (f[f.size()-1] == '!')
	{
	    f = f.substr(0, f.length()-1);
	    perish[i] = true;
	}
	items.push_back(f);
    }
    
    // get store inventories, prices
    for (int i = 0; i < ns; i++)
    {
	vector<string> storeinv;
	vector<int> storeprices;
	vector<int> pv;
	
	int sx, sy;
	cin >> sx >> sy;
	xpos[i] = sx;
	ypos[i] = sy;
	mask[i] = 0;
	
	char line[10000];
	cin.getline(line, 10000);
	stringstream ss;
	ss << line;
	
	string pair;

	while (ss >> pair)
	{
	    pair[pair.find(':')] = ' ';
	    char name[1000];
	    int price;
	    sscanf(pair.c_str(), "%s %d", name, &price);
	    
	    storeinv.push_back(name);
	    storeprices.push_back(price);
	}

	
	for (int j = 0; j < ni; j++)
	{
	    mask[i] <<= 1;
	    int pr = -1;
	    for (int k = 0; k < storeinv.size(); k++)
	    {
		if (storeinv[k].compare(items[j]) == 0)
		{
		    mask[i] |= 1;
		    pr = storeprices[k];
		    break;
		}
	    }

	    pv.push_back(pr);
	}

	prices[i] = pv;
    }
    
    
    // create graph
    // each vertex is a tuple <N, B>
    //   N = 0 (home)
    //   N > 0 (store #N with no perishable items in cart
    //   N < 0 (store #-N with perishable items in cart
    //   B is a integer in which the ith bit == 1 iff ith item is obtained
    // edge has weight corresponding to either price of gas between locations
    //   or cost of purchasing a single item


    // home
    for (int m = 0; m < (1<<ni); m++)
    {
	states[m] = State();
	visited[m] = false;
	distances[m] = DBL_MAX;
	xs[m] = 0;
	ys[m] = 0;
    }

    // stores, +/- perishable
    for (int i = 0; i < ns; i++)
    {
	for (int k = 0; k <= 1; k++)
	{
	    for (int m = 0; m < (1<<ni); m++)
	    {
		int ind = index(i, (bool) k, m, ni);
		states[ind] = State();
		xs[ind] = xpos[i];
		ys[ind] = ypos[i];
		
		visited[ind] = false;
		distances[ind] = DBL_MAX;
	    }
	}
    }

    // edges
    
    // same mask: between locations
    for (int m = 0; m < (1<<ni); m++)
    {
	// home to store
	for (int i = 0; i < ns; i++)
	{
	    int neighbor = index(i, false, m, ni);
	    states[m].neighbors.push_back(neighbor);
	    states[m].weight.push_back(pg*dist(m, neighbor));
	}
	
	// store to home
	for (int k = 0; k < 2; k++) // both perish settings
	{
	    for (int i = 0; i < ns; i++)
	    {
		int store = index(i, (bool) k, m, ni);
		states[store].neighbors.push_back(m);
		states[store].weight.push_back(pg*dist(store,m));
	    }
	}
       
	// between stores, only if nonperishable
	for (int i = 0; i < ns; i++)
	{
	    for (int j = 0; j <= i; j++)
	    {
		int store1 = index(i, false, m, ni);
		int store2 = index(j, false, m, ni);
		double d = pg*dist(store1, store2);
		states[store1].neighbors.push_back(store2);
		states[store1].weight.push_back(d);
		states[store2].neighbors.push_back(store1);
		states[store2].weight.push_back(d);
	    }
	}
    }

    //    purchase item
    for (int store = 0; store < ns; store++)
    {
	for (int m = 0; m < (1<<ni); m++)
	{
	    for (int i = 0; i < ni; i++)
	    {
		int item = ni-1-i;
		if ((!(m & (1 << i))) && (mask[store] & (1<<i)))
		    // if ith item is not in prior state
		    // and store has it
		{
		    
		    // previously nonperish -> perish if applicable
		    states[index(store, false, m, ni)].neighbors.push_back(
			index(store, perish[item], m | (1<<i), ni));
		    states[index(store, false, m, ni)].weight.push_back(
			prices[store][item]);
		    

		    // previously perish -> perish
		    states[index(store, true, m, ni)].neighbors.push_back(
			index(store, true, m | (1<<i), ni));
		    states[index(store, true, m, ni)].weight.push_back(
			prices[store][item]);
		       
		}
	    }
	}
    }
		 
   
   

    // run Dijkstra's
    // start is <0, 0>
    // end is <0, 2^ni-1>
    // result is minimum cost of trip


    distances[0] = 0.0;

    priority_queue<pdi, vector<pdi>, greater<pdi> > queue;
    queue.push(make_pair(distances[0], 0));

    while (!queue.empty())
    {
	int u = queue.top().second;
	queue.pop();

	if (visited[u]) continue;
	visited[u]=true;

	for (int vv = 0; vv < states[u].neighbors.size(); vv++)
	{
	    int v = states[u].neighbors[vv];
	    double w = states[u].weight[vv];
	    if (!(visited[v]) &&
		distances[u] + w < distances[v])
	    {
		distances[v] = distances[u] + w;
		queue.push(make_pair(distances[v], v));
	    }
	}
    }

    return distances[(1<<ni)-1];
}


int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 1; i <= cases; i++)
    {
	printf("Case #%d: %0.7f\n", i, solve());
    }
    
    return 0;
}
