// Problem: Cookie Clicker Alpha
// Language: JavaScript
// Author: KirarinSnow
// Usage: smjs thisfile.js <input.in >output.out
// Comments: I'm using JavaScript for this problem only because it's
//           mentioned in the problem statement.


var cases = readline();

for (var i = 1; i <= cases; i++)
{
    var line = readline().split(' ');
    var c = parseFloat(line[0]);
    var f = parseFloat(line[1]);
    var x = parseFloat(line[2]);
    var opt = Math.max(1, Math.ceil(x/c-2/f));
    var s = (x-c)/(2+(opt-1)*f);
    for (var j = 0; j < opt; j++)
    {
	s += c/(2+j*f);
    }
    print('Case #' + i + ': ' + s);
}
