module Main where

import Text.Regex.TDFA
-- import Text.Regex.TDFA.Text ()

import HaskellSay (haskellSay)

type Range = (Int, Int, Int, Int)

getData :: String -> Range
getData line = 
  let matches = getAllTextMatches ( line =~ "[[:digit:]]+") :: [String] in
  let helper = (\lst -> read $ "(" ++ (init.tail.show) lst ++ ")")  in 

  helper $ map (\z -> read z :: Int) matches


part1 :: Range -> Bool
part1 (l1, l2, r1, r2) = 
  (l1 >= r1 && l2 <= r2) || (r1 >= l1 && r2 <= l2)

part2 :: Range -> Bool
part2 (l1, l2, r1, r2) = 
  (l1 >= r1 && l1 <= r2) ||
  (r1 >= l1 && r1 <= l2)

main :: IO ()
main =
  do
    content <- readFile "file.txt"

    let fileLines = lines content

    putStrLn $ show $ sum $ map (\z -> if part1 $ getData z then 1 else 0) fileLines
    putStrLn $ show $ sum $ map (\z -> if part2 $ getData z then 1 else 0) fileLines
