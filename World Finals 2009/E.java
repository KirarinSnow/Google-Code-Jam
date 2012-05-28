// Problem: Marbles
// Language: Java
// Author: KirarinSnow
// Usage: javac thisfile.java && java thisfile <input.in >output.out
// Comments: Works only on small input. Adapted from reference solution.


import java.io.*;
import java.util.HashMap;

public class E {
    public static int MAX = 1<<20;
    public static int[][] cache = new int[1000][501];
    public static int[][][] evcache = new int[1000][1000][2];
    public static int[] evsize = new int[1000];
    public static int[] vis = new int[500];
    public static int n = 0;
    public static int[] marbles = new int[1000];
    public static int[][] where = new int[500][2];

    public static int h2(int a, int b, int h1) throws RuntimeException {
	if (h1 < 0) return MAX;
	if (a == b) return 0;
	int res = cache[a][h1];
	if (res != -1) return res;
	
	events(a);
	int evs = evsize[a];

	res = MAX;
	for (int mask = 0; mask <= 2; mask += 2) {
	    int top = 0;
	    int bot = 0;
	    int H2 = 0;
	    for (int i = 0; i <= evs; i++) {
		int alpha = (i == 0) ? a : evcache[a][i-1][0] + 1;
		int beta = (i == evs) ? b : evcache[a][i][0];
		
		H2 = Math.max(H2, h2(alpha, beta, h1-top) + bot);
		if (i != evs) {
		    switch (evcache[a][i][1] ^ mask) {
		    case 0: ++top; break;
		    case 1: --top; break;
		    case 2: ++bot; break;
		    case 3: --bot; break;
		    }
		}
	    }
	    res = Math.min(res, H2);
	}
	return res;
    }

    public static void events(int startx)
	throws RuntimeException {

	if (evsize[startx] > 0) return;
 
	for (int i = 0; i < n; i++) vis[i] = 0;

	dfs(marbles[startx], 1);
	int xp = 0;
	for (int x = 0; x < 2*n; x++) {
	    int m = marbles[x];
	    if (vis[m] == 0) continue;
	    int nr = 0;
	    if (where[m][nr] != x) nr += 1;

	    evcache[startx][xp][0] = x;
	    evcache[startx][xp][1] = 1-vis[m]+nr;
	    xp++;
	}
	evsize[startx] = xp;
	return;
    }
   
    public static void dfs(int m, int sign) throws RuntimeException {
	if (vis[m] == sign) return;
	if (vis[m] == -sign) throw new RuntimeException();
	vis[m] = sign;
	for (int i = 0; i < n; i++) {
	    if (i != m && cross(m, i)) {
		dfs(i, -sign);
	    }
	}
    }
   
    public static boolean cross(int m1, int m2) {
	boolean b =
	    (where[m1][0] < where[m2][0] &&
	     where[m2][0] < where[m1][1] &&
	     where[m1][1] < where[m2][1]) ||
	    (where[m2][0] < where[m1][0] &&
	     where[m1][0] < where[m2][1] &&
	     where[m2][1] < where[m1][1]);
	return b;
    }

    public static int solve(BufferedReader reader) throws IOException {
	n = Integer.valueOf(reader.readLine());

        String z[] = reader.readLine().split(" ");

	HashMap<String, Integer> d = new HashMap<String, Integer>();
	for (int i = 0; i < 2*n; i++) {
	    int m = -1;
	    if (d.containsKey(z[i])) {
		m = d.get(z[i]);
		where[m][1] = i;
	    }
	    else {
		m = d.size();
		d.put(z[i], m);
		where[m][0] = i;
	    }
	    marbles[i] = m;
	}
	
	for (int i = 0; i < 2*n; i++) {
	    for (int j = 0; j <= n; j++) {
		cache[i][j] = -1;
	    }
	    for (int j = 0; j < 2*n; j++) {
		evcache[i][j][0] = -1;
		evcache[i][j][1] = -1;
		
	    }
	    evsize[i] = 0;
	}

	int res = MAX;
	try {
	    for (int h1 = 0; h1 <= n; h1++) {
		res = Math.min(res, h1 + h2(0, 2*n, h1));
	    }
	} catch (RuntimeException x) {
	    return -1;
	}
	return res;
    }

    public static void main(String[] args) {
	InputStream in = null;
	try {
	    in = System.in;
	    BufferedReader reader =
		new BufferedReader(new InputStreamReader(in));
	    
	    int cases = Integer.valueOf(reader.readLine());
	    for (int i = 1; i <= cases; i++) {   
		System.out.println("Case #" + i + ": " + solve(reader));
	    }
	} catch (IOException x) {
	    System.err.println(x);
	} catch (NumberFormatException x) {
	    System.err.println(x);
	}
    }    
}
