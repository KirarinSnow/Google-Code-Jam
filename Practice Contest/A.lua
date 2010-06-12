-- Problem: Old Magician
-- Language: Lua
-- Author: KirarinSnow
-- Usage: lua thisfile.lua <input.in >output.out 


function compute ()
    w = io.read("*number")
    b = io.read("*number")
   
    if b % 2 == 0 then
       return "WHITE"
    else
       return "BLACK"
    end
end

cases = io.read("*number")

for i=1,cases do
    print("Case #" .. tostring(i) .. ": " .. tostring(compute()))
end
