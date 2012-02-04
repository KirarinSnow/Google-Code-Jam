// Problem: Min Perimeter
// Language: Java
// Author: KirarinSnow
// Usage: javac thisfile.java && java thisfile <input.in >output.out
// Comments: Adapted from reference solution.


import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.*;


public class B {
    public class Point {
	public long x;
	public long y;
	
	public Point(long x, long y) {
	    this.x = x;
	    this.y = y;
	}
    }

    public static Point mid (Point a, Point b) {
	B t = new B();
	return t.new Point((a.x+b.x)/2, (a.y+b.y)/2);
    }

    public class CmpX implements Comparator<Point> {
	public int compare(Point p1, Point p2) {
	    long x1 = p1.x;
	    long x2 = p2.x;
	    long y1 = p1.y;
	    long y2 = p2.y;

	    if (p1.x != p2.x) {
		if (x1 < x2) return -1;
		else if (x1 > x2) return 1;
		else return 0;
	    }	    	    
	    if (y1 < y2) return -1;
	    else if (y1 > y2) return 1;
	    else return 0;    
	}
    }

    public class CmpY implements Comparator<Point> {
	public int compare(Point p1, Point p2) {
	    long y1 = p1.y;
	    long y2 = p2.y;
	    long x1 = p1.x;
	    long x2 = p2.x;
	    if (p1.y != p2.y) {
		if (y1 < y2) return -1;
		else if (y1 > y2) return 1;
		else return 0;
	    }
	    if (x1 < x2) return -1;
	    else if (x1 > x2) return 1;
	    else return 0;
	}
    }	
    
    public static double perimeter(Point a, Point b, Point c) {
	return dist(a, b) + dist(b, c) + dist(c, a);
    }
    
    public static double dist(Point a, Point b) {
	return Math.sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
    }
    
    public static double calc(int n, List<Point> points) {
	n = points.size();
	if (n < 3) return 1e20;
	int left = n/2;
	int right = n-left;
	Point split = mid(points.get(left-1), points.get(left));
	
	B t = new B();
	CmpX cmpx = t.new CmpX();
	
	List<Point> pleft = new ArrayList<Point>();
	List<Point> pright = new ArrayList<Point>();
	for (int i = 0; i < n; i++) {
	    if (cmpx.compare(points.get(i), split) <= 0)
		pleft.add(points.get(i));
	    else
		pright.add(points.get(i));
	}
	
	double res = 1e20;
	res = Math.min(res, calc(left, pleft));
	res = Math.min(res, calc(right, pright));
	List<Point> close = new ArrayList<Point>();
	long margin = 0L;
	if (res > 1e20/2) {
	    margin = 2000000000L;
	}
	else {
	    margin = (long) res/2;
	}
	
	
	int start = 0;
	for (int k = 0; k < n; k++) {
	    Point p = points.get(k);
	    if (Math.abs(p.x - split.x) > margin) continue;
	    while (start < close.size() && p.y - close.get(start).y > margin) {
		start++;
	    }

	    for(int i = start; i < close.size(); i++) {
		for(int j = i+1; j < close.size(); j++) {
		    res = Math.min(res,
				   perimeter(p, close.get(i), close.get(j)));
		}
	    }
	    close.add(p);
	}
	return res;
    }

    public static double compute(BufferedReader reader) throws IOException {
	int n = Integer.parseInt(reader.readLine());
	
	B t = new B();

	ArrayList<Point> points = new ArrayList<Point>();

	for (int i = 0; i < n; i++) {
	    StringTokenizer st = new StringTokenizer(reader.readLine());
	    long a = (long) 2*Integer.parseInt(st.nextToken());
	    long b = (long) 2*Integer.parseInt(st.nextToken());
	    Point p = t.new Point(a, b);
	    points.add(p);
	}

	Collections.sort(points, t.new CmpX());
	Collections.sort(points, t.new CmpY());
	
	return calc(n, points)/2;
    }

    public static void main(String[] args) {

	InputStream in = null;
	try {
	    in = System.in;
	    BufferedReader p =
		new BufferedReader(new InputStreamReader(in));
	    PrintWriter comp = new PrintWriter(new FileWriter("Input.java"));
	    
	    String s;
	    while ((s = p.readLine()) != null) {
		comp.println(s);
	    }
	    comp.close();
	   
	    
	    Runtime run = Runtime.getRuntime();

	    Process prc = run.exec("javac Input.java");
	    try {  
		prc.waitFor();  

		
		Class c = ClassLoader.getSystemClassLoader().loadClass("Input");
		
		Method m = c.getMethod("main", new Class[]{args.getClass()});
		
		String[] nextArgs = new String[0];
		
		
		File file  = new File("tmp");
		PrintStream tmp = new PrintStream(new FileOutputStream(file));

		PrintStream save = System.out;
		System.setOut(tmp);
		
		m.invoke(null, new Object[] { nextArgs});

		tmp.close();
		
		System.setOut(save);


		BufferedReader rd =
		    new BufferedReader(new FileReader("tmp"));
		
		int t = Integer.parseInt(rd.readLine());
		
		for (int i = 1; i <= t; i++)
		{
		    System.out.printf("Case #%d: %.9f\n", i, compute(rd));
		}

		rd.close();

	    } catch (InterruptedException x) {
		System.err.println(x);
	    }
	    catch (ClassNotFoundException x) {
		System.err.println(x);
	    }
	    catch (NoSuchMethodException x) {
		System.err.println(x);
	    }
	    catch (IllegalAccessException x) {
		System.err.println(x);
	    }
	    catch (InvocationTargetException x) {
		System.err.println(x);
	    }
	   
	} catch (IOException x) {
	    System.err.println(x);
	} catch (NumberFormatException x) {
	    System.err.println(x);
	}
    }    
}
