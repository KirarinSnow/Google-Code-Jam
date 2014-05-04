// Problem: Different Sum
// Language: C++
// Author: KirarinSnow
// Usage: g++ thisfile.cpp -o executable && ./executable <input.in >output.out


#include <iostream>
#include <string>
#include <math.h>
#include <string.h>

using namespace std;

const long long int MOD = 1000000007;

const int MAXB = 70;
int nn[60];
long long int ch[MAXB+1][MAXB+1];
long long int fact[MAXB+1];
long long int d[MAXB][MAXB+1][MAXB*MAXB];
long long int c2[MAXB+1][MAXB*MAXB+1];
long long int c[60][MAXB][MAXB+1][2];


int main() {
  ch[0][0] = 1;
  for (int i = 0; i <= MAXB; i++) {
    ch[i][0] = 1;
    ch[i][i] = 1;
    for (int j = 1; j < i; j++) {
      ch[i][j] = ch[i-1][j-1]+ch[i-1][j];
      ch[i][j] %= MOD;
    }
  }
    
  fact[0] = 1;
  for (int i = 1; i <= MAXB; i++) {
    fact[i] = fact[i-1]*i;
    fact[i] %= MOD;
  }

  int cases;
  cin >> cases;
  
  for (int cas = 1; cas <= cases; cas++) {
    long long int n;
    int b;
    cin >> n >> b;
    int mb = b*(b-1)/2;
    int w = 0;
    while (n > 0) {
      nn[w++] = n%b;
      n /= b;
    }

    memset(d, 0, sizeof d);
    d[0][0][0] = 1;
    for (int nw = 1; nw < b; nw++) {
      for (int np = 0; np < nw; np++) {
	int mn = np*(np+1)/2+1;
	if (mb-nw+1 < mn)
	  mn = mb-nw+1;
	for (int k = 0; k <= np; k++) {
	  for (int s = 0; s < mn; s++) {
	    d[nw][k+1][s+nw] += d[np][k][s];
	    d[nw][k+1][s+nw] %= MOD;
	  }
	}
      }
    }
    memset(c2, 0, sizeof c2);
    for (int k = 0; k <= b; k++) {
      for (int s = 0; s <= mb; s++) {
	for (int nw = 0; nw < b; nw++) {
	  c2[k][s] += d[nw][k][s];
	  c2[k][s] %= MOD;
	}
      }
    }
    
    memset(c, 0, sizeof c);
    for (int k = 0; k <= b; k++) {
      c[0][0][k][0] = 1;
    }
    for (int i = 0; i < w; i++) {
      int z = nn[i];
      for (int k = 0; k <= b; k++) {
	for (int v = 0; v < b; v++) {
	  for (int v2 = 0; v2 < b; v2++) {
	    if (v2 >= mb)
	      continue;
	    int s = v2*b+z-v;
	    
	    if (i == 0) {
	      for (int g = 0; g < 2; g++) {
		if (k-g >= 0) {
		  long long int kk = c[i][v][k][0];
		  kk *= c2[k-g][s];
		  kk %= MOD;
		  c[i+1][v2][k][g] += kk;
		  c[i+1][v2][k][g] %= MOD;
		}
	      } 
	      continue;
	    }
	    
	    for (int p = 0; p <= k; p++) {
	      long long int t = 0;
	      for (int f = 0; f < 2; f++) {
		if (p-f >= 0) {
		  long long int kk = c[i][v][k][f]*ch[k-f][p-f];
		  kk %= MOD;
		  t += kk;
		  t %= MOD;
		}
	      }
	      
	      for (int g = 0; g < 2; g++) {
		if (p-g >= 0) {
		  long long int kk = t;
		  kk *= fact[p];
		  kk %= MOD;
		  kk *= c2[p-g][s];
		  kk %= MOD;
		  c[i+1][v2][p][g] += kk;
		  c[i+1][v2][p][g] %= MOD;
		}
	      }
	    }
	  }
	}
      }
    }
		    
    long long int ans = 0;
    for (int i = 0; i <= b; i++) {
      ans += c[w][0][i][0];
      ans %= MOD;
    }
    cout << "Case #" << cas << ": " << ans << endl;
  }
    
  return 0;
}
