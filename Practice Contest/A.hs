-- Problem: Old Magician
-- Language: Haskell
-- Author: KirarinSnow
-- Usage: ghc thisfile.hs -o executable && ./executable <input.in >output.out 


solve :: Int -> String
solve b
    | b `mod` 2 == 1  = "BLACK"
    | otherwise       = "WHITE"

compute :: Int -> IO () 
compute casenum =
    getLine >>= (\line -> putStrLn ("Case #" ++ show casenum ++ ": " ++
        solve (last (map read (words line)))))

main :: IO ()
main = getLine >>= (\line -> mapM_ compute [1 .. read line])
