-- Problem: Old Magician
-- Language: VHDL
-- Author: KirarinSnow
-- Usage: ghdl -a thisfile.vhdl && ghdl -e jam && ./jam <input.in >output.out 


use std.textio.all;

entity jam is
end jam;

architecture code of jam is
begin
    process
        variable i, o : line;
        variable t, c, b, w: integer;
    begin
        readline(input, i);
        read(i, t);
        for c in 1 to t loop
            write(o, String'("Case #"));
            write(o, c);
            write(o, String'(": "));

            readline(input, i);
            read(i, w);
            read(i, b);

            if b mod 2 = 1 then
                write(o, String'("BLACK"));
            else
                write(o, String'("WHITE"));
            end if;
            writeline(output, o);
        end loop;
        wait;
    end process;
end code;
