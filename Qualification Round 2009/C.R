# Problem: Welcome to Code Jam
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out


infile <- file('/dev/stdin')

buffer <- scan(infile, 'character', sep='\n')
cases <- type.convert(buffer[1])
current <- 2


compute <- function()
{
    chars <- buffer[current]
    current <<- current + 1
    
    width <- nchar(chars)
    
    ct <- array(0, nchar(wc)+1)
    ct[1] <- 1
    
    for (j in 1:width)
    {
        ch <- substr(chars, j, j)
        for (k in 1:nchar(wc))
        {
            if (ch == substr(wc, k, k))
            {
                ct[k+1] <- (ct[k+1] + ct[k]) %% 10000
            }
        }
    }

    sprintf('%04d', ct[nchar(wc)+1])
}

wc <- 'welcome to code jam'

for (i in 1:cases)
{
    cat(sprintf('Case #%d: %s\n', i, compute()))
}
