# CMI ISI – 4TCM403U

## Projet de programmation

### Leçon 1 - Programmation python - Environnements virtuels

L'écriture d'un programme même de taille modeste nécessite d'utiliser un bon nombre de librairies externes.

On construit un environnement dédie au projet qui héberge les versions des librairies utilisées dans le programme que l'on construit.

- Pour assurer la cohérence des différentes librairies utilisées dans un projet.
- Pour isoler ces librairies d'autres librairies utilisées dans un autre projet (ou même du système d'exploitation).
- Pour bien gérer les dépendances et éviter les conflits de versions entre les librairies.

#### venv / conda

[venv](https://aaronlelevier.github.io/virtualenv-cheatsheet/) est un utilitaire qui permet de créer un environnement

- Les informations propres à l'environnement sont posés dans un dossier choisi par l'utilisateur:

```
# creates a virtualenv
python -m venv /path/to/new/virtual/environment
```

On active l'environnement en faisant référence à ce dossier:

```
# activates the virtualenv
source /path/to/new/virtual/environment/bin/activate
```

--

#### Un exemple

En consultant un oracle (LLM), on trouve (attention, tout n'est pas véridique ...):

- Un exemple qui combine les librairies `pandas`, `numpy`, `matplotlib`, `seaborn` (statistical visualizations) et `scikit-learn`

Si on installe ces librairies, en faisant typiquement

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

- Si on utilise un version spécifique de `seaborn` 0.11.0, il faut alors installer `matplotlib 3.3.0`.
- Et s'il faut utliser un modèle disponible sous `scikit-learn 1.0.0`, on doit alors utiliser `numpy 1.21.0`.
- Mais alors, `seaborn 0.11.0` n'est pas compatible avec `numpy 1.21.0` car il requière une ancienne version`numpy 1.19.0`.
- EN essayant de résoudre cette situation en passant à `seaborn 0.11`, cela entrainera un passage à `numpy 1.19.0`, incompatible avec `scikit-learn 1.0.0`.

(*source DeepSeek interrogé le lundi 3 février 2025*)