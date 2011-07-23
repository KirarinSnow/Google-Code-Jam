// Problem: Watering Plants
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <math.h>
#include <stdio.h>
#include <iostream>

using namespace std;

int px[40];
int py[40];
int pr[40];
double cx[3500];
double cy[3500];

double out(int v, int w, double r)
{
    double xd = px[v]-cx[w];
    double yd = py[v]-cy[w];
    return sqrt(xd*xd + yd*yd) > r - pr[v] + 1.0e-6;
}

double solve()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
	cin >> px[i] >> py[i] >> pr[i];
    }

    double l = 0.0;
    double u = 708.0;
    while (u-l > 1.0e-6)
    {
	double r = (l+u)/2.0;

	int cc = 0;
	for (int c1 = 0; c1 < n; c1++)
	{
	    for (int c2 = c1+1; c2 < n; c2++)
	    {
		double x1 = px[c1];
		double x2 = px[c2];
		double y1 = py[c1];
		double y2 = py[c2];
		double r1 = pr[c1];
		double r2 = pr[c2];

		double x0 = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
		double xp = ((r-r1)*(r-r1) - (r-r2)*(r-r2))/2.0/x0 + x0/2.0;

		double yps = (r-r1)*(r-r1) - xp*xp;
		if (yps >= 0)
		{
		    double yp = sqrt(yps);
		    double cos = (x2-x1)/x0;
		    double sin = (y2-y1)/x0;
		   
		    cx[cc] = cos*xp - sin*yp + x1;
		    cy[cc] = cos*yp + sin*xp + y1;
		    cc++;

		    if (yps > 0)
		    {
			double yn = -yp;
			cx[cc] = cos*xp - sin*yn + x1;
			cy[cc] = cos*yn + sin*xp + y1;
			cc++;
		    } 
		}
	    }
	}

	for (int i = 0; i < n; i++)
	{
	    cx[cc] = px[i];
	    cy[cc] = py[i];
	    cc++;
	}

	for (int d = 0; d < cc; d++)
	{
	    for (int e = 0; e < cc; e++)
	    {
		bool f = true;
		for (int z = 0; z < n; z++)
		{
		    if (out(z, d, r) && out(z, e, r))
		    {
			f = false;
			break;
		    }
		}
		if (f) goto resume;
	    }
	}
	l = r;
	continue;

    resume:
	u = r;
    }

    return u;
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
