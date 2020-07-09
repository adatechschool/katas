module Exerice exposing (decoder)

decoder : String -> String -- Lui donner un param (->)et ce qu'il va donner en retour.
decoder chaine =

  if String.length(chaine) == 1 then
    if chaine == "1" then
      "I"
    else if chaine == "5" then
      "S"
    else if chaine == "0" then
      "O"
    else
      chaine
  else
    decoder(String.left 1 chaine) ++ decoder(String.right (String.length chaine - 1) chaine)
