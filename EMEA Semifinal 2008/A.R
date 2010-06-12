# Problem: Scaled Triangle
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out


buffer <- scan(file('/dev/stdin'))

cases <- buffer[1]
pt <- 2

for (i in 1:cases)
{
    s <- buffer[pt : (pt+5)]
    t <- buffer[(pt+6) : (pt+11)]
    pt <- pt + 12

    lhs <- t(matrix(ncol=6, nrow=6, c(
	s[1:2], 0, 0, 1, 0,
	0, 0, s[1:2], 0, 1,
	s[3:4], 0, 0, 1, 0,
	0, 0, s[3:4], 0, 1,
	s[5:6], 0, 0, 1, 0,
	0, 0, s[5:6], 0, 1)))
    rhs <- matrix(ncol=1, nrow=6, t)

    coef <- MASS::ginv(lhs) %*% rhs

    l <- t(matrix(ncol=2, nrow=2, c(
	coef[1]-1, coef[2],
	coef[3], coef[4]-1)))
    r <- matrix(ncol=1, nrow=2, -coef[5:6])
    
    sol <- MASS::ginv(l) %*% r

    cat(sprintf('Case #%d: %f %f\n', i, sol[1], sol[2]))
}
