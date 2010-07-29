// Problem: Old Magician
// Language: C#
// Author: KirarinSnow
// Usage: mcs thisfile.cs && ./thisfile.exe <input.in >output.out


class GCJ
{
    static string Compute()
	{
	    int b = int.Parse(System.Console.ReadLine().Split(' ')[1]);
	    return b % 2 == 0 ? "WHITE" : "BLACK";
	}
    
    static void Main()
	{
	    int cases = int.Parse(System.Console.ReadLine());
	    for (int i = 1; i <= cases; i++)
	    {
		System.Console.WriteLine("Case #" + i + ": " + Compute());
	    }
	}
}
