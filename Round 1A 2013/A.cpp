// Problem: Bullseye
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out
// Comments: Does not work for large.


#include <iostream>
#include <string>

using namespace std;


int main()
{
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++)
    {
      int r, t;
      cin >> r >> t;
      
      int c = 0;
      while (t >= 0)
      {
	t -= (r+c+1)*(r+c+1) - (r+c)*(r+c);
	c += 2;
      }
      
      cout << "Case #" << i << ": " << c/2-1 << endl;
    }
    
    return 0;
}
