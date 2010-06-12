// Problem: Old Magician
// Language: JavaScript
// Author: KirarinSnow
// Usage: smjs thisfile.js <input.in >output.out

function compute(i)
{
    var wb = readline().split(' ');

    var b = wb[1];
    if (b % 2 == 1)
	return 'BLACK';
    else
	return 'WHITE';
}


var cases = readline();

for ( var i = 1; i <= cases; i++ )
{
    print('Case #' + i + ': ' + compute(i));
}
