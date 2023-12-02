import Data.List(stripPrefix)

acc :: (String, Int)Int
acc = 0

parseLine ::String -> (String, Int)
parseLine line = (take 3 line, 

main :: IO ()
main = do putStrLn "Hi"
