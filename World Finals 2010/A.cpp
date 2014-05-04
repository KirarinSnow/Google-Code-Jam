// Problem: Letter Stamper
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string>
#include <string.h>

using namespace std;

const int MAX = 1<<20;
int b[7001][6][7001];
char s[7000];
const char *P[6] = {"ABC", "BCA", "CAB", "ACB", "BAC", "CBA"};

int main() {
  int cases;
  cin >> cases;
  
  for (int cas = 1; cas <= cases; cas++) {
    cin >> s;
    int n = strlen(s);

    memset(b, 0, sizeof b);
    for (int p = 0; p < 6; p++) {
      for (int l = 0; l <= n; l++) {
	b[n][p][l] = l;
      }
    }

    for (int k = n-1; k >= 0; k--) {
      char c = s[k];
      for (int p = 0; p < 6; p++) {
	for (int l = 0; l <= n; l++) {
	  if (l == 0) {
	    int v = MAX;
	    for (int pp = 0; pp < 6; pp++) {
	      string sp = P[pp];
	      int d = sp.find(c);
	      if (l+d+1 <= n) {
		int w = 2+d+b[k+1][pp][l+d+1];
		if (w < v) v=w;
	      }
	    }
	    b[k][p][l] = v;
	  }
	  else {
	    int t = P[p][(l-1)%3];
	    if (c == t) {
	      b[k][p][l] = 1+b[k+1][p][l];
	    }
	    else {
	      int v = MAX;
	      if (c == P[p][l%3]) {
		if (l+1 <= n) {
		  int w = 2+b[k+1][p][l+1];
		  if (w < v) v=w;
		}
	      }
	      else {
		if (l+2 <= n) {
		  int w = 3+b[k+1][p][l+2];
		  if (w < v) v=w;
		}
		if (l == 1) {
		  if (l+1 <= n) {
		    int w = 2+b[k+1][(p+3)%6][l+1];
		    if (w < v) v=w;
		  }
		}
	      }
	      if (l >= 2 && c == P[p][(l-2)%3]) {
		int w = 2+b[k+1][p][l-1];
		if (w < v) v=w;
	      }
	      if (l >= 3 && c == P[p][l%3]) {
		int w = 3+b[k+1][p][l-2];
		if (w < v) v=w;
	      }
	      b[k][p][l] = v;
	    }
	  }
	}
      }
    }
    
    int ans = MAX;
    for (int p = 0; p < 6; p++) {
      int w = b[0][p][0];
      if (w < ans) ans = w;
    }

    cout << "Case #" << cas << ": " << ans << endl;
  }
    
  return 0;
}
