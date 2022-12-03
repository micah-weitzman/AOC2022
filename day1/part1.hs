import System.Environment
import Data.List

splitSpace :: [String] -> [[String]]
splitSpace [] = []
splitSpace (hd:lst) = 
  case hd of
    "" -> splitSpace lst
    _ -> (takeWhile (\x -> 0 /= length x)  $ hd:lst): splitSpace (dropWhile (\y -> 0 /= length y) $ hd:lst)


toInts :: [String] -> [Int]
toInts = map read


findMax :: [String] -> Int
findMax lst = maximum (map sum $ map toInts (splitSpace lst))


main = do
  args <- getArgs
  content <- readFile (args !! 0)
  let fileLines = lines content
      all_data = findMax fileLines
  putStrLn $ show all_data