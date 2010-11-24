/*
 * Problem: King
 * Language: REXX
 * Author: KirarinSnow
 * Usage: regina thisfile.rexx <input.in >output.out
 * Comments: Adapted from the reference solution. Times out on large.
 */


do case = 1 to linein()
  parse linein r " " c
  do i = 0 to r-1
    line = linein()
    do j = 0 to c-1
      a.i.j = substr(line, j+1, 1)
      if a.i.j = 'K' then do
	kr = i
	kc = j
	end
      end
    end

  m1 = solve(0, 0, 0)
  a.kr.kc = '.'
  drop m.
  m2 = solve(0, 0, 0)
  drop m.

  say "Case #" || case || ": " || substr("BA", 1+(m2>m1), 1)

  end
exit


solve: procedure expose r c a. m.
parse arg x, y, b

if x = c then do
  x = 0
  y = y+1
  if y = r then return 0
  end

if left(m.x.y.b, 1) = 'M' then m.x.y.b = -1

if m.x.y.b \= -1 then return m.x.y.b

bb = strip(bitand(0||b, copies(1, c+1), 0), 't', '0')

if a.y.x \= '.' then do
  m.x.y.b = solve(x+1, y, bb)
  end
else do
  m.x.y.b = solve(x+1, y, add(bb, 1))
  if x\=0 & bitand(b, 1, 0)\=0 then
    m.x.y.b = max(m.x.y.b, 1+solve(x+1, y, add(bb, -2)))
  if x\=0 & bitand(b, copies(0, c)||1, 0)\=0 then
    m.x.y.b = max(m.x.y.b, 1+solve(x+1, y, bb))
  if bitand(b, copies(0, max(0, c-1))||1, 0)\=0 then
    m.x.y.b = max(m.x.y.b, 1+solve(x+1, y, add(bb, -shift(1, c))))
  if x<(c-1) & bitand(b, copies(0, max(0, c-2))||1, 0)\=0 then
    m.x.y.b = max(m.x.y.b, 1+solve(x+1, y, add(bb, -shift(1, c-1))))
  end

return m.x.y.b

add: return reverse(x2b(d2x(x2d(b2x(reverse(arg(1))))+arg(2))))

shift: return trunc(arg(1)*(2**arg(2)))
