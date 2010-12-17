# Problem: Your Rank is Pure
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out
# Comments: Runs out of time on large.


#modify as appropriate
maxsize <- 25

B <- matrix(0, maxsize, maxsize)
for (x in 1:maxsize)
{
  for (y in 1:maxsize)
  {
     B[x,y] = choose(x-1, y-1)
  }
}

rchoose <- function(a, b) {
  if (a < 0 || b < 0)
     0
  else
     B[a+1, b+1]
}

A <- matrix(0, maxsize, maxsize)


for (x in 2:maxsize)
{
  for (y in 1:x-1)
  {
     if (y == 1)
     {
        A[x, y] <- 1
     }
     else
     {
        z = 0
        for (i in 1:y)
	{
	   d <-  A[y, i] * rchoose(x-y-1, y-i-1)
	   z = (z+d) %% 100003
	}
	  
	A[x, y] <- z
     }
  }
}


compute <- function()
{
  n <- buffer[current]
  current <<- current + 1

  sum(A[n,]) %% 100003
}

buffer <- scan('/dev/stdin')

cases <- buffer[1]
current <- 2

for (i in 1:cases)
{
  cat(sprintf('Case #%d: %d\n', i, compute()))
}
