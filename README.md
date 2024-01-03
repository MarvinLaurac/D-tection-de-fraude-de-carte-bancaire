# D-etection-de-fraude-de-carte-bancaire

![Détection](https://github.com/MarvinLaurac/D-tection-de-fraude-de-carte-bancaire/assets/152433361/04bec3e6-ae4d-4e4a-902c-b1342e376712)

# INTRODUCTION
Dans le monde financier, la fraude bancaire doit répondre à de nombreux problèmes. Elle touche autant les banques que les clients qui y déposent leur argent. Cela est dû aux arnaques de transaction qui peuvent être complexes à identifier. Par conséquent, il est important de repérer ces fraudes.

Ce projet a pour but de créer un modèle qui peut aider à la détection de ces transactions suspectes, avec des données d’analyse et d'apprentissage automatique.

![1 1](https://github.com/MarvinLaurac/D-tection-de-fraude-de-carte-bancaire/assets/152433361/abc83961-2d8d-4c0d-99d7-2dedbb7ade74)

# LOGICIEL PRIVILÉGIÉ
  - Python

J'ai utiliser  Python avec ces bibliothèques comme Pandas pour l'analyse de données, Scikit-Learn pour le machine learning, et Matplotlib pour la visualisation.

# CONTEXTE DU SUJET
Ce projet représente les transactions par carte de crédit réalisées en septembre 2013 par des détenteurs européens. Parmi les 284 807 transactions enregistrées sur deux jours, 492 sont identifiées comme frauduleuses, ce qui indique un déséquilibre puisque les fraudes ne représentent que 0,172 % du total. Les données sont principalement constituées de variables numériques issues d'une transformation par Analyse en Composantes Principales (ACP), à l'exception de 'Time' et 'Amount'. Les variables V1 à V28 sont le résultat de cette ACP, tandis que 'Time' indique les secondes écoulées depuis la première transaction de l'ensemble de données et 'Amount' reflète le montant de chaque transaction. Cet ensemble de données présente un défi en raison de son déséquilibre et des limitations liées à la confidentialité, qui empêchent l'accès aux caractéristiques originales et à des informations plus détaillées. La variable cible, 'Class', est binaire, où 1 indique une transaction frauduleuse et 0 une transaction légitime.

# Recommandations de l’auteur du DataFrame
De plus, l'efficacité de la détection de la fraude ne peut être évaluée par la précision seule, étant donné le déséquilibre des classes. Il est donc recommandé d'utiliser l'aire sous la courbe de précision-rappel (AUPRC) comme métrique principale. Cette approche offre une évaluation plus fiable de la performance du modèle, en particulier dans les cas de classification déséquilibrée, comme c'est le cas avec cet ensemble de données.

