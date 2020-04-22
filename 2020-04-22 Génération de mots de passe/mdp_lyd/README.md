# Variantes et étapes

## Si on se sent pas très à l’aise : le mot de passe aléatoire

### Étapes :
* pour se lancer, commencer par afficher juste un caractère aléatoire :

``import random``

``print(random.choice('qwertyuiop'))``


* puis afficher un mot de passe complètement aléatoire de longueur fixe de votre choix

``import random``
``import string``

``def mdp_aleatoire(taille_mdp=3):``
``    car = string.ascii_letters``
``    return ''.join(random.choice(car) for i in range(taille_mdp))``

``print("Le mdp proposé est : ", mdp_aleatoire())``


* ensuite, plutôt qu’une longueur fixe, permettre à l’utilisatrice de spécifier la longueur en paramètre sur la ligne de commande

``import random``
``import string``

``def mdp_aleatoire():``
``    car = string.ascii_letters + string.digits + string.punctuation``
``    taille = int(input("Choisissez la taille du mdp : "))``
``    return ''.join(random.choice(car) for i in range(taille))``

``print("Le mdp proposé est : ", mdp_aleatoire())``
