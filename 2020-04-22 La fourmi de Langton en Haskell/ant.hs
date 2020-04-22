import Data.List

data Color = White | Black deriving (Show, Eq)

data Square = Square { x :: Int
                     , y :: Int
                     , color :: Color
                     } deriving (Show, Eq)

type World = [Square]
