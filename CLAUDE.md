# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Contexte du projet

Dépôt **pédagogique** (en français) pour un stage de seconde de deux semaines en équipe informatique finance. Le public est constitué de débutants complets : tout code, commentaire, message de commit et documentation doit rester **en français, simple et expliqué**. Le but est l'apprentissage progressif, pas la sophistication. Privilégier la clarté sur l'élégance ou la performance. Toutes les données sont fictives.

## Commandes

```bash
# Environnement (depuis la racine)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Tests (pytest est configuré pour être lancé depuis la racine)
pytest                                          # toute la suite
pytest tests/test_finance_assistant.py          # un fichier
pytest tests/test_finance_assistant.py::test_company_is_complete   # un seul test

# Lancer l'application fil rouge
python projet/src/main.py
```

La CI (`.github/workflows/python-ci.yml`) tourne sur Python 3.11 et exécute `pytest` à chaque push/PR sur `main`. Pas de linter configuré.

## Architecture

Le code applicatif tient en deux fichiers sous `projet/src/` :

- **`finance_assistant.py`** — toute la logique métier sous forme de fonctions pures sans état : `load_json`, `is_company_complete`, `missing_loan_documents`, `summarize_company`, `build_ai_prompt`. C'est ici qu'on ajoute des fonctionnalités.
- **`main.py`** — point d'entrée qui charge les JSON et affiche résumé + prompt.

**Détail important sur les imports :** le projet n'est pas un package installable et `projet/src/` n'est pas sur le `sys.path` par défaut.
- `main.py` fonctionne car Python ajoute son propre dossier au path → il importe `finance_assistant` directement.
- `tests/test_finance_assistant.py` ajoute manuellement `projet/src` au `sys.path` en tête de fichier (d'où le `# noqa: E402` sur l'import). Tout nouveau fichier de test doit reproduire ce préambule.

**Flux de données :** les JSON fictifs vivent sous `ressources/donnees/entreprises/<entreprise>/` avec deux fichiers par entreprise — `company.json` et `loan-request.json`. Les chemins sont résolus relativement à la racine via `Path(__file__).resolve().parents[...]`. La convention des documents requis repose sur des clés booléennes `has_<document>` dans `loan-request.json` (voir `missing_loan_documents`).

**Garde-fou produit :** `build_ai_prompt` injecte explicitement « Ne prends pas de décision de crédit » dans le prompt. L'IA résume, elle ne décide pas — c'est un principe du stage testé par `test_build_ai_prompt_does_not_decide_credit`. Le conserver.

## Structure des dossiers (au-delà du code)

- `parcours/jour-NN/` — missions quotidiennes des stagiaires (10 jours, voir tableau de progression du README).
- `docs/` — `guide-du-tuteur.md` (rôle de tech lead du tuteur) et `planning.md`.
- `débuter/` — exercices Python d'introduction.
