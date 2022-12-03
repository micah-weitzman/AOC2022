import System.Environment

getScore :: String -> Int
getScore l =
  let hd:tl:[] = words l in
  case [tl, hd] of
    ["X", "A"] -> 3
    ["X", "B"] -> 1
    ["X", "C"] -> 2

    ["Y", "A"] -> 4
    ["Y", "B"] -> 5
    ["Y", "C"] -> 6
    
    ["Z", "A"] -> 8
    ["Z", "B"] -> 9
    ["Z", "C"] -> 7
    _ -> 0


main :: IO ()
main = do
  args <- getArgs
  content <- readFile (args !! 0)

  let fileLines = lines content
  putStrLn $ show $ sum (map getScore fileLines)

