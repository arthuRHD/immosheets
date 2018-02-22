# README

## Idées

- OK - Utiliser un dataframe Pandas pour faire quelques stats.
- TODO - Passer un paramètre en entrée pour passer une autre requête à exécuter. Ca permettrait de tester aussi un report sur les loyers. Mais attention, le problème avec les locations c'est que ce n'est peut-être pas les mêmes champs... Ou mieux lire dans un fichier de conf (voir ce qu'a fait le mec sur GitHub).
- TODO - Gérer le multi-pages sur les résultats. Pour le moment je ne lis que la 1ère. Il est indiqué dans le résultat le nombre max de pages, ca peut m'aider à faire la boucle. Je peux faire un truc ou j'analyse la page et je mets pageMax dans un param, avec un while. Au début pageMax vaut 1 et ensuite il prend la valeur de pageMax.
- TODO - Ajouter des logs, retours console pour l'utilisateur, au moins les OK.