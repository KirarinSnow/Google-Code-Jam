NB. Problem: Old Magician
NB. Language: J
NB. Author: KirarinSnow
NB. Usage: jc thisfile.ijs <input.in >output.out



load 'strings'

NB. Read entire input; extract number of cases
read =. ;:1!:1[3
cases =. ".>0{read


NB. Create array of input values
input =. ".>(2*i.cases){(}.}.read)

NB. Array of mod values; output is corresponding answer
mods =. 2|((2*i.cases)+1){;input
answer =. mods{>'WHITE';'BLACK'


NB. Format output: print "Case #" then case number then ": " then answer

prefix =. (0*i.cases){>((10{a.),'Case_#');''
casenumber =. 8!:2((cases,1)$1+i.cases)
colon =. (0*i.cases){>': ';''
rj =. (|.~ i.&' ')"1
lj =. (|.~ i.&'C')"1

exit stdout lj '_ ' charsub (rj prefix,.casenumber),.colon,.answer
