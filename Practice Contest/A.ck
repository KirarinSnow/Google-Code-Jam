// Problem: Old Magician
// Language: ChucK
// Author: KirarinSnow
// Usage: chuck thisfile.ck <input.in >output.out
// Comments: See http://chuck.cs.princeton.edu/


FileIO stdin, stdout;
stdout.open("/dev/stdout", FileIO.WRITE);
stdin.open("/dev/stdin", FileIO.READ);

fun string compute()
{
    stdin.readInt(16) => int w;
    stdin.readInt(16) => int b;
    return b % 2 == 0 ? "WHITE" : "BLACK";
}

stdin.readInt(8) => int total;
for(1 => int i; i <= total; i++)
{
    stdout.write("Case #" + i + ": " + compute() + "\n");
}

stdin.close();
stdout.close();
