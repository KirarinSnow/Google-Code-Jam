// Problem: Old Magician
// Language: Asymptote
// Author: KirarinSnow
// Usage: asy thisfile.asy <input.in >output.out


string compute () {
  int w = stdin, b = stdin;  
  return b % 2 == 1 ? "BLACK" : "WHITE";
}


int total = stdin;
for (int i = 1; i <= total; i += 1) {
  write("Case #" + (string)i + ": " + compute());
}
