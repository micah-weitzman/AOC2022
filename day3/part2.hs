import System.Environment
import Data.List

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


chunks :: Int -> [a] -> [[a]]
chunks n = takeWhile (not . null) . unfoldr (Just . splitAt n)

score :: [String] -> Int
score (a:b:c:[]) =
          let inter = (intersect (intersect a b) c) !! 0
              ind = elemIndex inter alph in 
          case ind of 
            Just v -> v + 1
            Nothing -> 0
          

main :: IO ()
main = do
  args <- getArgs
  content <- readFile (args !! 0)

  let fileLines = lines content
  putStrLn $ show $ sum $ map score $ chunks 3 fileLines