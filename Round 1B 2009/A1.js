// Problem: Decision Tree
// Language: JavaScript
// Author: KirarinSnow
// Usage: smjs thisfile.js <input.in >output.out


function compute()
{
    var d = '';
    for ( var x = readline(); x--; )
	d += readline();

    for ( var x = readline(); x--; )
	print(eval(
	    d.replace(/([a-z]+)/g,
		      '*({' + readline().replace(/ /g, ':1,z') + ':1}.z$1?')
		.replace(/\) *\(/g, '):')));
}

var cases = readline();

for ( var i = 1; i <= cases; i++ )
{
    print('Case #' + i + ':');
    compute();
}
