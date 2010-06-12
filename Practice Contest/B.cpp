// Problem: Square Fields
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int x[15], y[15], cp[1<<15];
const int MAX = 64000;

bool isclique(int s, int n, int k)
{
  int xmax = 0;
  int ymax = 0;
  int xmin = MAX;
  int ymin = MAX;
  for (int i = 0; i < n; i++)
  {
    int ca = (s >> i)%2;
    if (ca == 1)
    {
      if (x[i] < xmin) xmin = x[i];
      if (x[i] > xmax) xmax = x[i];
      if (y[i] < ymin) ymin = y[i];
      if (y[i] > ymax) ymax = y[i];
    }
    if ((((xmax-xmin)>(ymax-ymin)) ? (xmax-xmin) : (ymax-ymin)) > k)
      return false;
  }
  return true;
}

void det(int s, int n, int k)
{
  vector<int> subs;
  subs.push_back(0);
  int numdigs = (int) (log(s)/log(2))+1;
  for (int i = 0; i < numdigs; i++)
  {
    if ((s >> (numdigs-i-1))%2 == 1)
    {
      vector<int> subs2 = subs;
      for (int j = 0; j < subs.size(); j++)
      {
	subs[j] <<= 1;
      }
      for (int j = 0; j < subs2.size(); j++)
      {
	subs2[j] <<= 1;
	subs2[j] += 1;
      }
      for (int v = 0; v < subs2.size(); v++) subs.push_back(subs2[v]);
    }
    else
    {
      for (int j = 0; j < subs.size(); j++)
      {
	subs[j]<<=1;
      }
    }
  }
  
  if (isclique(s, n, k)) cp[s] = 1;

  int minp = MAX;
  for (int sti = 0; sti < subs.size(); sti+=2)
  {
    int st = subs[sti];
    int stx = s^st;
    if (st != s && stx != s)
    {
      if (cp[st] >= MAX) det(st, n, k);
      if (cp[stx] >= MAX) det(stx, n, k);
    }
    minp = (minp < cp[st]+cp[stx])?minp:(cp[st]+cp[stx]);
  }

  cp[s] = (cp[s] < minp)?cp[s]:minp;
}


int solve()
{
  int n, bound;
  scanf("%d %d", &n, &bound);
  for (int i = 0; i < n; i++)
  {
    scanf("%d %d", x+i, y+i);
  }

  int xmax = 0;
  int ymax = 0;
  int xmin = MAX;
  int ymin = MAX;

  for (int i = 0; i < n; i++)
  {
    if (x[i] < xmin) xmin = x[i];
    if (x[i] > xmax) xmax = x[i];
    if (y[i] < ymin) ymin = y[i];
    if (y[i] > ymax) ymax = y[i];
  }

  int l = 0;
  int u = (xmax-xmin>ymax-ymin)?(xmax-xmin):(ymax-ymin);

  while (l < u)
  {
    int k = (l+u)/2;
    for (int j = 0; j < 1<<n; j++)
    {
      cp[j] = MAX;
    }
    det((1<<n)-1, n, k);
    if (cp[(1<<n)-1] <= bound) u = k;
    else l = k+1;
  }
  

  return u;
}


int main()
{
  int cases;
  scanf("%d",&cases);

  for (int i = 1; i <= cases; i++)
  {
    printf("Case #%d: %d\n", i, solve());
  }

  return 0;
}
