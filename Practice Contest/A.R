# Problem: Old Magician
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out


compute <- function()
{
  b <- buffer[current+1]
  current <<- current + 2
	
  if (b %% 2 == 0)
    cat('WHITE')
  else
    cat('BLACK')
}

buffer <- scan('/dev/stdin')

cases <- buffer[1]
current <- 2

for (i in 1:cases)
{
  cat('Case #')
  cat(i)
  cat(': ')
  compute()
  cat('\n')
}
