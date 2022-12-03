import System.Environment
import Data.List

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

splitHalf :: String -> (String, String)
splitHalf l = splitAt ((length l + 1) `div` 2) l

score :: String -> Int
score l = let (x, y) = splitHalf l
              inter = elemIndex ((intersect x y) !! 0) alph in 
          case inter of 
            Just v -> v + 1
            Nothing -> 0
          

main :: IO ()
main = do
  args <- getArgs
  content <- readFile (args !! 0)

  let fileLines = lines content
  putStrLn $ show $ sum $ map score fileLines