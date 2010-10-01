// Problem: Decision Tree
// Language: JavaScript
// Author: KirarinSnow
// Usage: smjs thisfile.js <input.in >output.out


function compute()
{
    var nd = readline();
    var dt = '';
    for ( var i = 0; i < nd; i++ )
    {
	dt += readline();
    }
    
    dt = dt.replace(/\)/g,'))');
    dt = dt.replace(/ ([a-z])/g,'*("$1');
    dt = dt.replace(/([a-z])\b/g,'$10" in animal?');
    dt = dt.replace(/\) *\(/g,':(');
    dt = dt.replace(/\)$/,'');
    
    var na = readline();
    for ( var i = 0; i < na; i++ )
    {
	var v = readline().split(' ').slice(2);

	var animal = new Object();

	for ( var j = 0; j < v.length; j++ )
	{
	    eval('animal.' + v[j] + '0=0');
	}
	print(eval(dt));
	delete animal;
    }
}

var cases = readline();

for ( var i = 1; i <= cases; i++ )
{
    print('Case #' + i + ':');
    compute();
}
