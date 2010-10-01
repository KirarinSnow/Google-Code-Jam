# Problem: Decision Tree
# Language: R
# Author: KirarinSnow
# Usage: R -q --slave -f thisfile.R <input.in >output.out
# Comments: Stack overflow on large input. Recompile R with larger stack to fix.


n <- 0
l <- paste(readLines('/dev/stdin'), collapse='\n')
l <- gsub('([a-z]+)', '"\\1"', l)
l <- gsub(' *("[a-z]+")\\s*\\(', '*(if(\\1%in%f)', l)
l <- gsub(')\\s*\\(', ' else ', l)
l <- gsub('" "', '","', l)
l <- gsub('\n\\(', ';n<-n+1;cat("Case #",n,":\n",sep="");d<-expression(', l)
l <- gsub('[^\n]* [0-9]+( [^\n]*|\n)', '\nf<-c(\\1);cat(eval(d),"\n")\n', l)

eval(parse(text=l))
