// Problem: What are Birds?
// Language: JavaScript
// Author: KirarinSnow
// Usage: smjs thisfile.js <input.in >output.out

function compute()
{
    var n = readline();
    var bx = [];
    var by = [];
    var nbx = [];
    var nby = [];

    // Populate bird and not-bird arrays
    for (var nl = 0; nl < n; nl++ )
    {
	var a = readline().split(' ');
	if (a[2] == "NOT")
	{
	    nbx.push(a[0]);
	    nby.push(a[1]);
	}
	else
	{
	    bx.push(a[0]);
	    by.push(a[1]);
	}
    }

    // Compute min and max
    var xmin = Math.min.apply(Math,bx);
    var xmax = Math.max.apply(Math,bx);
    var ymin = Math.min.apply(Math,by);
    var ymax = Math.max.apply(Math,by);

    if (xmax == -Infinity || xmax == Infinity)
    {
	// Case where there are no birds; only points identical to not-birds
	// are certainly not-birds
	var points = [];
	for (var i = 0; i < nbx.length; i++)
	{
	    points[" "+nbx[i][0]+" "+nbx[i][1]] = true;
	}
	var m = readline();
	for (var i = 0; i < m; i++)
	{
	    a = readline().split(' ');
	    if (a in points)
	    {
		print('NOT BIRD');
	    }
	    else
	    {
		print('UNKNOWN');
	    }
	}
    }
    else
    {
	// Normal case
	var xp = -1;
	var yp = -1;
	var xq = 1000001;
	var yq = 1000001;
	
	// Adjust not-bird certainty bounds
	for (var i = 0; i < nbx.length; i++)
	{
	    if (nbx[i] <= xmax && nbx[i] >= xmin)
	    {
		if (nby[i] > ymax)
		    yq = Math.min(yq, nby[i]);
		else if (nby[i] < ymin)
		    yp = Math.max(yp, nby[i]);
		else
		    ;
	    }
	    if (nby[i] <= ymax && nby[i] >= ymin)
	    {
		if (nbx[i] > xmax)
		    xq = Math.min(xq, nbx[i]);
		else if (nbx[i] < xmin)
		    xp = Math.max(xp, nbx[i]);
		else
		    ;
	    }
	}
	
	var m = readline();
	for (var i = 0; i < m; i++)
	{
	    a = readline().split(' ');
	    if (a[0] >= xmin && a[0] <= xmax && a[1] >= ymin && a[1] <= ymax)
	    {
		// Within range: bird
		print('BIRD');
	    }
	    else if (a[0] <= xp || a[0] >= xq || a[1] <= yp || a[1] >= yq)
	    {
		// Within not-bird certainty bounds: not bird
		print('NOT BIRD');
	    }
	    else
	    {
		if ((a[0] < xmin && a[0] > xp && a[1] <= ymax && a[1] >= ymin)||
		    (a[0] > xmax && a[0] < xq && a[1] <= ymax && a[1] >= ymin)||
		    (a[1] < ymin && a[1] > yp && a[0] <= xmax && a[0] >= xmin)||
		    (a[1] > ymax && a[1] < yq && a[0] <= xmax && a[0] >= xmin))
		{
		    //  Strictly between bounds: unknown
		    print('UNKNOWN');
		}
		else
		{
		    // Corner case: Create array with potential point as bird,
		    // test with all not-birds
		    var cx = bx.slice(0);
		    var cy = by.slice(0);
		    
		    cx.push(a[0]);
		    cy.push(a[1]);
		    
		    var xmax1 = Math.max.apply(Math, cx);
		    var xmin1 = Math.min.apply(Math, cx);
		    var ymax1 = Math.max.apply(Math, cy);
		    var ymin1 = Math.min.apply(Math, cy);

		    var t = 0;
		    for (var j = 0; j < nbx.length; j++)
		    {
			if (nbx[j] <= xmax1 && nbx[j] >= xmin1 &&
			    nby[j] <= ymax1 && nby[j] >= ymin1)
			    t++;
		    }

		    if (t > 0)
			print('NOT BIRD');
		    else
			print('UNKNOWN');
		}
	    }
	}
    }
}


var cases = readline();

for ( var i = 1; i <= cases; i++ )
{
    print('Case #' + i + ':');
    compute();
}
