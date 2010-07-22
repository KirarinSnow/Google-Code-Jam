# Problem: Old Magician
# Language: CoffeeScript
# Author: KirarinSnow
# Usage: coffee -c thisfile.coffee && smjs thisfile.js <input.in >output.out
# Comments: For smaller inputs, use CoffeeScript directly:
#             coffee thisfile.coffee <input.in >output.out


compute: (i, line, p) ->
    out = if (line.split(' ')[1] % 2 == 0) then 'WHITE' else 'BLACK'
    p 'Case #' + i + ': ' + out


# USE THIS FOR SMALLER INPUTS, BUFFER GETS CUT OFF

coffee: () ->
    stdin: process.openStdin()
    stdin.setEncoding('ascii')
    stdin.addListener('data', (stuff) ->
         
        lines: (stuff).split('\n')
        for i in [1 .. lines[0]]
            compute(i, lines[i], puts)
    )


# USE THIS FOR LARGER INPUTS

smjs: () ->
    for i in [1 .. readline()]
        compute(i, readline(), print)


coffee() if puts?
smjs() if not(puts?)
