// Problem: Old Magician
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string>

using namespace std;

string compute()
{
    int b, w;
    cin >> b >> w;
    
    return w % 2 == 0 ? "WHITE" : "BLACK";
}

int main()
{
    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; i++)
    {
	cout << "Case #" << i << ": " << compute() << endl;
    }
    
    return 0;
}
