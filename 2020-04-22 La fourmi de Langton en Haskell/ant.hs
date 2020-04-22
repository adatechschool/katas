import Data.List

data Direction = Droite | Gauche
      deriving (Show, Eq, Enum)

data Case = Case { x :: Int
                 , y :: Int
                 } deriving (Show, Eq)

goto :: Eq a => a -> [a] -> [a]
goto pos inBlackSq
  | pos `elem` inBlackSq = inBlackSq 
  | otherwise = pos:inBlackSq
