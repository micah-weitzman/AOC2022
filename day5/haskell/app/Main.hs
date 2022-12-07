module Main where

import Text.Regex.TDFA

data Move = Move Int Int Int deriving (Show)

type State = [[String]]

slice start end = take (end - start + 1) . drop start


getMove :: String -> Move
getMove line = 
  let matches = getAllTextMatches ( line =~ "[[:digit:]]+") :: [String] in

  case (map (\z -> read z :: Int) matches) of
    a:b:c:[] -> Move a b c
    _ -> Move 0 0 0


makeMove :: State -> Move -> State
makeMove s (Move x y z) -> 



main :: IO ()
main =
  do
    content <- readFile "file.txt"

    let fileLines = lines content in

      putStrLn $ show $ getMove (fileLines !! 12)
      -- putStrLn $ show $ sum $ map (\z -> if part1 $ getData z then 1 else 0) fileLines
