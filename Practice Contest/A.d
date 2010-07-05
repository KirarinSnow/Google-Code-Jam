/+ 
 + Problem: Old Magician
 + Language: D
 + Author: KirarinSnow
 + Usage: gdc thisfile.d -o executable && ./executable <input.in >output.out
 +/


import std.stdio;
import std.cstream;
import std.conv;
import std.string;

string compute()
{
    string line = din.readLine();
    int b = std.conv.toInt(line.split(" ")[1]);
    return b % 2 == 1 ? "BLACK" : "WHITE";
}

int main()
{
    int cases = std.conv.toInt(din.readLine());
    for (int i = 1; i <= cases; i++)
    {
	writefln("Case #%d: %s", i, compute());
    }

    return 0;
}
