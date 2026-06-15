# Planning pédagogique — 10 jours

Ce planning est conçu pour deux élèves de seconde. Il peut être adapté selon leur niveau, leur autonomie et le temps disponible.

## Objectif global

À la fin du stage, les élèves doivent être capables de présenter un petit assistant Python orienté finance qui :

1. lit des données fictives d'entreprise ;
2. vérifie la complétude d'un dossier ;
3. calcule quelques indicateurs simples ;
4. génère un résumé lisible ;
5. prépare un prompt exploitable par un assistant IA.

## Semaine 1 — Python et données

### Jour 1 — Découverte

Objectifs :

- comprendre le rôle d'un développeur dans une équipe finance ;
- installer Python, VS Code et Git ;
- écrire les premiers scripts Python ;
- comprendre `print`, variables et types simples.

Livrable : un script `bonjour_finance.py`.

### Jour 2 — Conditions et fonctions

Objectifs :

- utiliser `if`, `else` ;
- créer des fonctions simples ;
- vérifier qu'une donnée est présente ou valide.

Livrable : une fonction qui vérifie si une entreprise a un nom, un pays et un chiffre d'affaires.

### Jour 3 — Listes et dictionnaires

Objectifs :

- manipuler des listes ;
- manipuler des dictionnaires ;
- représenter une entreprise en Python.

Livrable : une fiche entreprise affichée proprement.

### Jour 4 — JSON

Objectifs :

- lire un fichier JSON ;
- comprendre la différence entre données et code ;
- charger un dossier client fictif.

Livrable : un programme qui lit `ressources/donnees/entreprises/alpha-industrie/company.json`.

### Jour 5 — Mini application

Objectifs :

- regrouper le code dans des fonctions ;
- structurer un mini projet ;
- produire un résumé de dossier.

Livrable : première version de l'application fil rouge.

## Semaine 2 — GitHub, qualité et IA

### Jour 6 — GitHub

Objectifs :

- comprendre dépôt, commit, branche, issue et pull request ;
- créer une branche ;
- ouvrir une pull request ;
- recevoir une revue de code simple.

Livrable : une pull request contenant une petite amélioration.

### Jour 7 — IA générative

Objectifs :

- comprendre ce qu'est un LLM ;
- comprendre prompt, contexte, hallucination et confidentialité ;
- écrire un prompt clair.

Livrable : un prompt qui résume une entreprise fictive.

### Jour 8 — Assistant IA

Objectifs :

- construire un prompt à partir de données structurées ;
- distinguer données, règles et consignes ;
- utiliser l'IA comme assistant, pas comme décideur.

Livrable : une fonction `build_prompt(company, financials)`.

### Jour 9 — Qualité et tests

Objectifs :

- écrire quelques tests avec `pytest` ;
- comprendre pourquoi les tests protègent le code ;
- lancer la CI GitHub Actions.

Livrable : tests verts sur GitHub Actions.

### Jour 10 — Démo finale

Objectifs :

- préparer une démonstration courte ;
- expliquer ce qui a été appris ;
- présenter les limites et améliorations possibles.

Livrable : démonstration de 10 minutes par binôme ou élève.
