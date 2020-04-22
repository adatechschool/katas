data Color = White | Black deriving (Show, Eq)

data Square = Square { x :: Int
                     , y :: Int
                     , color :: Color
                     }

type World = [Square]
