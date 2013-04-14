// Problem: Fair and Square
// Language: Pike
// Author: KirarinSnow
// Usage: pike thisfile.pike <input.in >output.out
// Comments: Works on the first large input, but not the second.


import Stdio;

string s = stdin.read();

array ps = ({});

int readint()
{
  int x;
  sscanf(s, "%d%s", x, s);
  return x;
}

int main()
{
  for (int x = 1; x <= 10000000; x++)
    {
      string xs = (string)x;
      int y = x*x;
      string ys = (string)y;
      if (xs == reverse(xs) && ys == reverse(ys))
	{
	  ps += ({y});
	}
    }

  int cases = readint();
  for (int i = 1; i <= cases; i++)
    {
      int a = readint();
      int b = readint();
      int c = 0;
      for (int j = 0; j < sizeof(ps); j++)
	{
	  if (a <= ps[j] && ps[j] <= b)
	    {
	      c += 1;
	    }
	}

      write(sprintf("Case #%d: %d\n", i, c));
    }
  return 0;
}
