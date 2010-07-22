// Problem: Old Magician
// Language: Java
// Author: KirarinSnow
// Usage: javac thisfile.java && java thisfile <input.in >output.out


import java.io.*;

public class A {

    public static String solve(BufferedReader reader) throws IOException {
	int b;

	String s = reader.readLine();
	b = Integer.valueOf(s.substring(s.length()-1));
		
	if (b % 2 == 0) {
	    return "WHITE";
	}
	else {
	    return "BLACK";
	}
    }

    public static void main(String[] args) {

	InputStream in = null;
	try {
	    in = System.in;
	    BufferedReader reader =
		new BufferedReader(new InputStreamReader(in));
	    
	    int cases = Integer.valueOf(reader.readLine());
	    for (int i = 1; i <= cases; i++) {   
		System.out.print("Case #");
		System.out.print(i);
		System.out.print(": ");
		System.out.println(solve(reader));
	    }
	} catch (IOException x) {
	    System.err.println(x);
	} catch (NumberFormatException x) {
	    System.err.println(x);
	}
    }    
}
