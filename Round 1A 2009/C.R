# Problem: Collecting Cards
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R < input.in > output.out


infile <- file('/dev/stdin')

buffer <- scan(infile)
cases <- buffer[1]
current <- 2


compute <- function()
{

    c <- buffer[current]
    n <- buffer[current + 1]
    current <<- current + 2
    
    
    if (n == c)
    {
	# If N = C, only one pack needed.
        1
    }
    else
    {
	# Compute transition matrix
	tm <- matrix(0, c-n+1, c-n+1)
	cnc <- choose(c,n)
	for (k in 0:(c-n))
	{
	    for (m in k:(c-n))
	    {
		# Probability of advancing from having k cards beyond
		# the first N cards to having m cards beyond the first
		# N cards
		tm[m+1,k+1] <- choose(n+k,n-m+k)*choose(c-n-k,m-k)/cnc
	    }
	}


	# Prepare vector of probabilities of having k cards
	# beyond the first N cards with the second pack
	v <- array(0, c-n+1)
	for (k in 0:(c-n))
	{
	    v[k+1] <- choose(n, n-k) * choose(c-n, k) / cnc
	}


	# Initialize expected value accumulator and pack counter
	e <- v[c-n+1]*2
	s <- 2
	
	# Advance to next state vector until probability of
	# having all cards is approx. 1
	while (1-v[c-n+1] > 0.0000001)
	{
	    # Save previous probability of having all cards
	    prev <- v[c-n+1]

	    # Apply matrix multiplication
	    v <- tm %*% v

	    # Update expected value with difference in probability
	    # of having all cards
	    e <- e + (s+1)*(v[c-n+1]-prev)

	    # Increment pack counter
	    s <- s + 1
	}

	# Return final expected value
	e
    }
}

# Iterate through cases
for (i in 1:cases)
{
    cat(sprintf('Case #%d: %f\n', i, compute()))
}
