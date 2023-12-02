import Input
import Test

type Run = Int

type Drop = Int

type Slope = (Run, Drop)

main :: IO ()
main = do putStrLn $ show $ (part1 input, part2 input)

treeAt :: Int -> String -> Int
treeAt i s
  = case s !! i of
        '.' -> 0
        '#' -> 1

treeAt' :: Run -> (Int, String) -> Int
treeAt' run (i, string) = treeAt ((run * i) `mod` (length string)) string

countTrees :: Slope -> [String] -> Int
countTrees (run, drop) strings = sum $ map (run `treeAt'`) pairs
  where len = length strings
        keptRows = [strings!!i | i<-[0..len-1], i`mod`drop ==0 ]
        len' = length keptRows
        pairs = zip [0 .. len'-1] keptRows

part1 :: [String] -> Int
part1 strings = countTrees (3, 1) strings

part2 :: [String] -> Int
part2 strings
  = product $
      map (`countTrees` strings) [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
