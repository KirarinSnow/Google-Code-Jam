-- Problem: Old Magician
-- Language: SQL
-- Author: KirarinSnow
-- Usage: createdb db
--        psql -d db -q -t -f thisfile.sql <input.in >output.out
--        dropdb db


CREATE TABLE tab (S varchar);
\COPY tab FROM '/dev/stdin';
SELECT CONCAT('Case #', (row_number() OVER ())-1, ': ',
              CASE WHEN CAST(CONCAT('0', split_part(S, ' ', 2)) AS integer)%2=1
              THEN 'BLACK' ELSE 'WHITE' END) FROM tab OFFSET 1;
