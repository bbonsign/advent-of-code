import Input
import Test

-- main :: IO ()
-- main

data Passport = Passport {
   byr :: String,  -- (Birth Year)
   -- iyr :: String,  -- (Issue Year)
   -- eyr :: String,  -- (Expiration Year)
   -- hgt :: String,  -- (Height)
   -- hcl :: String,  -- (Hair Color)
   -- ecl :: String,  -- (Eye Color)
   -- pid :: String,  -- (Passport ID)
   cid :: Maybe [Char]   -- (Country ID)
                         }
                         deriving (Show, Eq, Read)


-- parsePassports :: String -> Passport
-- parsePassports str = pstrs
--   where pstrs = filter (\l -> l/="") $ lines str
