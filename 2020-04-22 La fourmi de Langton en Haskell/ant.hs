import Data.List

data Direction = Droite | Haut | Gauche | Bas
  deriving (Show, Eq)

data Square = Square { x :: Int
                     , y :: Int
                     } deriving (Show, Eq)

data Ant = Ant { square :: Square
               , direction :: Direction
               } deriving (Show, Eq)

goto :: Eq a => a -> [a] -> [a]
goto position inBlackSq
  | position `elem` inBlackSq = delete position inBlackSq 
  | otherwise = position:inBlackSq
