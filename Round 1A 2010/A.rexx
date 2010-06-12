/*
 * Problem: Rotate
 * Language: REXX
 * Author: KirarinSnow
 * Usage: regina thisfile.rexx <input.in >output.out
 */


do case=1 to linein()
    call compute case
end
exit

compute:
    out = 'Case #' || i || ': ' 
    c = linein()
    n = subword(c, 1, 1)
    k = subword(c, 2, 1)
    do i=0 to n-1
        line = linein()
        do j=0 to n-1
            A.i.j = substr(line, j+1, 1)
        end
    end

    do i=0 to n-1
        e=n-1
	do while e>=0 & A.i.e \= '.'
	    e=e-1
    	end
        p=e-1
        do while p>=0
	    if A.i.p \= '.' then
	    do
	        A.i.e = A.i.p
		A.i.p = '.'
		e=e-1
	    end
	    p=p-1
	end
    end

    rwin = 0
    bwin = 0

    /* rows */
    do i=0 to n-1
        cr=0
	cb=0
	do j=0 to n-1
	    select 
	    when A.i.j = 'R' then
	    do
	        cr=cr+1
		cb=0
	    end
	    when A.i.j = 'B' then
	    do
	        cb=cb+1
		cr=0
 	    end
	    otherwise
    	    do
	        cb=0
		cr=0
	    end
	    end

	    if cr>=k then
	        rwin = 1
 	    if cb>=k then
	        bwin = 1
	end
    end
    
    /* cols */
    do i=0 to n-1
        cr=0
	cb=0
	do j=0 to n-1
	    select 
	    when A.j.i = 'R' then
	    do
	        cr=cr+1
		cb=0
	    end
	    when A.j.i = 'B' then
	    do
	        cb=cb+1
		cr=0
 	    end
	    otherwise
    	    do
	        cb=0
		cr=0
	    end
	    end

	    if cr>=k then
	        rwin = 1
 	    if cb>=k then
	        bwin = 1
	end
    end
    
    /* diagonals */
    do i=-n+1 to n-1
        cr=0
	cb=0
	do j=0 to n-1
	    ii=j+i
    	    if ii>=0 & ii<n then
	    do
	    select 
	    when A.ii.j = 'R' then
	    do
	        cr=cr+1
		cb=0
	    end
	    when A.ii.j = 'B' then
	    do
	        cb=cb+1
		cr=0
 	    end
	    otherwise
    	    do
	        cb=0
		cr=0
	    end
	    end

	    if cr>=k then
	        rwin = 1
 	    if cb>=k then
	        bwin = 1
            end
	end
    end

    /* inverse diagonals */
    do i=0 to 2*n-2
        cr=0
	cb=0
	do j=0 to n-1
	    ii=i-j
    	    if ii>=0 & ii<n then
	    do
	    select 
	    when A.ii.j = 'R' then
	    do
	        cr=cr+1
		cb=0
	    end
	    when A.ii.j = 'B' then
	    do
	        cb=cb+1
		cr=0
 	    end
	    otherwise
    	    do
	        cb=0
		cr=0
	    end
	    end

	    if cr>=k then
	        rwin = 1
 	    if cb>=k then
	        bwin = 1
            end
	end
    end

    out = 'Neither'
    if rwin then
        out = 'Red'
    if bwin then
        out = 'Blue'
    if bwin & rwin then
        out = 'Both'

    say 'Case #' || arg(1) || ':' out
    return
