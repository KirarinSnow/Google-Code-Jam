// Problem: Old Magician
// Language: Pike
// Author: KirarinSnow
// Usage: pike thisfile.pike <input.in >output.out


import Stdio;

string s = stdin.read();

int readint()
{
  int x;
  sscanf(s, "%d%s", x, s);
  return x;
}

string compute()
{
  int w = readint();
  int b = readint();
  return b % 2 == 1 ? "BLACK" : "WHITE";
}

int main()
{
  int cases = readint();
  for (int i = 1; i <= cases; i++)
    {
      write(sprintf("Case #%d: %s\n", i, compute()));
    }
  return 0;
}
