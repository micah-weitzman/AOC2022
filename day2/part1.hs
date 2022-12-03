import System.Environment

getScore :: String -> Int
getScore l =
  let hd:tl:[] = words l in
  case [tl, hd] of
    ["X", "A"] -> 4
    ["X", "B"] -> 1
    ["X", "C"] -> 7

    ["Y", "A"] -> 8
    ["Y", "B"] -> 5
    ["Y", "C"] -> 2
    
    ["Z", "A"] -> 3
    ["Z", "B"] -> 9
    ["Z", "C"] -> 6
    _ -> 0


main :: IO ()
main = do
  args <- getArgs
  content <- readFile (args !! 0)

  let fileLines = lines content
  putStrLn $ show $ sum (map getScore fileLines)

