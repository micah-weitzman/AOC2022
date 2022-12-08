import Data.List
import qualified Data.Set as Set

l = 14

get_answer :: String -> Int -> Int
get_answer s i =
  let size = Set.size $ Set.fromList $ take l s in
    if size == l then 
      i + l
    else
      get_answer (tail s) $ i + 1



main :: IO ()
main = do
  content <- readFile "file.txt"
  putStrLn $ show $ get_answer ((lines content) !! 0) 0