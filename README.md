# Stage seconde — Python, IA et finance

Bienvenue dans ce dépôt pédagogique destiné à accompagner deux élèves de seconde pendant un stage de deux semaines dans une équipe informatique du domaine de la finance.

L'objectif n'est pas de former des experts en Python ou en intelligence artificielle en dix jours. L'objectif est de leur faire découvrir concrètement le métier de développeur, la manipulation de données, l'usage raisonné de l'IA et les pratiques collaboratives avec GitHub.

## Scénario du stage

Les stagiaires rejoignent une équipe qui développe un outil interne pour aider des analystes financiers à préparer l'étude d'une demande de financement d'entreprise.

Ils vont construire progressivement un mini assistant capable de :

- lire des données fictives sur des entreprises ;
- vérifier si un dossier de financement est complet ;
- calculer quelques indicateurs simples ;
- produire un résumé lisible ;
- préparer un prompt pour un assistant IA ;
- présenter leur projet en fin de stage.

Toutes les données du dépôt sont fictives.

## Organisation du dépôt

```text
.
├── docs/                 Documentation pour le tuteur et les stagiaires
├── parcours/             Missions quotidiennes sur 10 jours
├── projet/               Application fil rouge en Python
├── ressources/           Données fictives et supports
├── tests/                Tests automatiques avec pytest
├── .github/workflows/    Intégration continue GitHub Actions
└── README.md
```

## Progression pédagogique

| Jour | Thème | Objectif |
|---|---|---|
| 1 | Découverte | Installer l'environnement et écrire les premiers scripts Python |
| 2 | Données simples | Manipuler variables, conditions et fonctions |
| 3 | Dossiers clients | Lire et comprendre des dictionnaires Python |
| 4 | JSON | Charger des données depuis des fichiers |
| 5 | Mini application | Structurer un programme Python simple |
| 6 | GitHub | Utiliser issues, branches, commits et pull requests |
| 7 | IA générative | Comprendre les prompts et les limites des LLM |
| 8 | Assistant IA | Préparer des prompts à partir de données client |
| 9 | Qualité | Ajouter tests, documentation et amélioration du code |
| 10 | Démo finale | Présenter le projet et les apprentissages |

## Démarrage rapide

### 1. Cloner le dépôt

```bash
git clone https://github.com/amah/stage-seconde-python-ia-finance.git
cd stage-seconde-python-ia-finance
```

### 2. Créer un environnement Python

```bash
python -m venv .venv
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
```

Sous Windows :

```powershell
.venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer les tests

```bash
pytest
```

### 5. Lancer l'application

```bash
python projet/src/main.py
```

## Principes importants

- On apprend par petits pas.
- On vérifie le code avec des tests simples.
- On utilise l'IA comme assistant, pas comme décideur.
- On ne manipule aucune donnée réelle de client ou d'entreprise.
- On documente ce que l'on fait.

## Rôle du tuteur

Le tuteur joue le rôle de tech lead :

- il explique les objectifs ;
- il crée ou commente les issues ;
- il relit les pull requests ;
- il aide les stagiaires à formuler leurs raisonnements ;
- il rappelle les règles de confidentialité, de qualité et de responsabilité.

Voir `docs/guide-du-tuteur.md` pour le détail.
