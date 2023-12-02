import Input

main :: IO ()
main = do putStr $ show $ ("part1", part1 input, "part2", part2 input)

part1 :: [((Int, Int), Char, String)] -> Int
part1 xs = count True $ map isValid1 xs

part2 :: [((Int, Int), Char, String)] -> Int
part2 xs = count True $ map isValid2 xs

count :: (Eq a) => a -> [a] -> Int
count x xs = length $ filter (\ e -> e == x) xs

isValid1 :: ((Int, Int), Char, String) -> Bool
isValid1 ((min, max), char, password) = min <= c && c <= max
  where c = count char password

isValid2 :: ((Int, Int), Char, String) -> Bool
isValid2 ((i1, i2), char, password) = c == 1
  where c = count True
              [char == (password !! (i1 - 1)), char == (password !! (i2 - 1))]
