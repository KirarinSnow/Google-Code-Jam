# Problem: Center of Mass
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out


infile <- file('/dev/stdin')

buffer <- scan(infile)
cases <- buffer[1]
current <- 2


compute <- function()
{
    nf <- buffer[current]
    current <<- current + 1

    x <- array(0,3)
    v <- array(0,3)
    for (k in 1:nf)
    {
	x <- x + buffer[current:(current+2)]
	v <- v + buffer[(current+3):(current+5)]
	current <<- current + 6
    }

    x <- x / nf
    v <- v / nf

    t <- -(x%*%v)[1]/(v%*%v)[1]
    if (!(is.finite(t)) || t < 0)
    {
	t <- 0
    }

    d <- sqrt(((x+v*t) %*% (x+v*t))[1])

    cat(sprintf('%.8f %.8f', d, t))
}

# Iterate through cases
for (i in 1:cases)
{
    cat(sprintf('Case #%d: ', i))
    compute()
    cat('\n')
}
