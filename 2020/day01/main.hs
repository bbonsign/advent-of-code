
main :: IO ()
main
  = do input <- getContents
       putStrLn $ show $ take 3 $ findProducts $ readInts input

readInts :: String -> [Int]
readInts s = map read (lines s)

findProducts :: [Int] -> [Int]
findProducts xs = [x * y * z | x <- xs, y <- xs, z <- xs, x + y + z == 2020]

