# Analyse de log : activités et horaires


## Contexte
Dans votre entreprise un serveur permet de centraliser les infos des plannings de différentes séances de formation.

Vous devez parser un fichier correspondant au planning d'une formation et réaliser quelques statistiques de base.

Ici on veut un script assez léger qui tourne dans un environnement très basique (type image Docker minimale).

C'est à dire qu'on préfère éviter importer des bibliothèques qu'il faudrait installer en plus de Python.


## Spécifications de votre script : 
- Doit s'appeler "parse_log.py"
- Utilisation : `$ python parse_log.py <fichier.log>`
- Doit prendre en entrée un fichier au format de "planning.log"
- Doit produire un rapport au format demandé "expected_output.txt"
    - Chaque ligne en sortie doit faire exactement 43 caractères
    - Par ordre alphabétique
    - Pourcentage du temps de chaque activité (arrondi au point de pourcentage inférieur)
    - Il doit y avoir 6 caractères à droite du "s" de "minutes"
- Repérez les alignements nécessaires dans le fichier fourni et reproduisez les
- Produire les tests unitaires associés à vos fonctions
- Le script doit écrire son résultat dans la sortie standard


## Contraintes
- Testez votre programme dans un venv ou container : si vous avez besoin d'un "pip install" pour le faire tourner vous échouerez automatiquement.
- Vous pouvez utiliser tout builtin Python (fonctions et librairies)


## Conseils
- Commencez par écrire vos tests unitaires en créant des scénarios simples (une seule ligne dans le log)
- Ensuite vérifiez (idéalement en ligne de commande) si quand vous lancez votre programme sur le fichier joint vous obtenez un fichier identique à l'output demandé
- [Les f-strings sont vos amies](https://realpython.com/python-f-strings/)
- Si vous trouvez déjà ça facile [vous familiariser avec la lib python "re"](https://docs.python.org/3/library/re.html) (un peu d'investissement initial, mais outil vraiment puissant)