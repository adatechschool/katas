import Data.List

data Square = Square { x :: Int
                     , y :: Int
                     } deriving (Show, Eq)

moveAnt :: Eq a => a -> [a] -> [a]
moveAnt current blackSq
  | contain == [] = current:blackSq
  | otherwise = delete current blackSq
  where contain = intersect [current] blackSq
