# Python en stage IT — Fiche d'exercices

**Public :** élèves de seconde, débutants en Python
**Contexte :** stage de découverte en département informatique
**Outil :** [Basthon](https://basthon.fr) (console ou notebook, aucune installation)
**Durée indicative :** une demi-journée à une journée selon le rythme

---

## Comment utiliser cette fiche

Les exercices sont **progressifs** : chacun s'appuie sur les notions du précédent. Fais-les dans l'ordre. Pour chaque exercice, tu trouveras l'objectif, l'énoncé, un exemple de ce qui est attendu, et un ou deux coups de pouce si tu bloques.

> **Conseil :** exécute ton code souvent, même incomplet, pour voir ce qui se passe. Faire une erreur et lire le message d'erreur fait partie de l'apprentissage.

---

## Exercice 1 — Fiche d'un poste informatique
**Notions :** variables, affichage (`print`)

Dans un parc informatique, chaque ordinateur a une fiche. Crée des variables pour décrire un poste, puis affiche sa fiche.

Crée les variables suivantes : un nom de poste (par exemple `"PC-COMPTA-01"`), une marque, une quantité de mémoire RAM en gigaoctets, et l'année d'achat. Affiche ensuite une fiche lisible.

**Résultat attendu (exemple) :**
```
Poste : PC-COMPTA-01
Marque : Dell
RAM : 8 Go
Année : 2021
```

**Coup de pouce :** une variable se crée avec `nom_poste = "PC-COMPTA-01"`. Pour afficher du texte, on utilise `print("...")`.

---

## Exercice 2 — Convertisseur d'unités de stockage
**Notions :** saisie utilisateur (`input`), conversion de type (`int`), calcul

Au support informatique, on jongle souvent entre les unités. Écris un programme qui demande une taille de fichier en **mégaoctets (Mo)** et qui affiche sa taille en **kilooctets (Ko)** et en **octets**.

On utilisera la règle simple : 1 Mo = 1024 Ko et 1 Ko = 1024 octets.

**Résultat attendu (exemple) :**
```
Taille en Mo ? 5
5 Mo = 5120 Ko = 5242880 octets
```

**Coup de pouce :** `input()` renvoie toujours du texte. Pour faire un calcul, il faut convertir en nombre entier avec `int(input("Taille en Mo ? "))`.

---

## Exercice 3 — Vérificateur de mot de passe
**Notions :** conditions (`if` / `else`), longueur d'une chaîne (`len`)

La sécurité, c'est le quotidien d'un service IT. Écris un programme qui demande un mot de passe et qui vérifie qu'il fait **au moins 8 caractères**. Le programme affiche si le mot de passe est accepté ou refusé.

**Résultat attendu (exemple) :**
```
Mot de passe ? abc
Refusé : trop court (minimum 8 caractères).
```
```
Mot de passe ? soleil2024
Accepté.
```

**Coup de pouce :** `len(mot_de_passe)` donne le nombre de caractères. On compare avec `if len(...) >= 8:`.

**Pour aller plus loin :** ajoute une vérification pour qu'il contienne au moins un chiffre. (Indice : la méthode `.isdigit()` teste si un caractère est un chiffre, à utiliser dans une boucle.)

---

## Exercice 4 — Compte à rebours de redémarrage
**Notions :** boucle `for`, fonction `range`

Quand on doit redémarrer un serveur, on prévient les utilisateurs avec un compte à rebours. Écris un programme qui affiche un compte à rebours de 10 jusqu'à 1, puis le message `Redémarrage !`.

**Résultat attendu :**
```
10
9
8
...
1
Redémarrage !
```

**Coup de pouce :** `range(10, 0, -1)` génère les nombres de 10 à 1 en descendant. On parcourt avec `for i in range(10, 0, -1):`.

---

## Exercice 5 — Inventaire du parc informatique
**Notions :** listes, parcours de liste, `len`

Le département gère plusieurs ordinateurs. On stocke leurs noms dans une liste. Écris un programme qui affiche le nombre total de postes, puis la liste numérotée de chaque poste.

Pars de cette liste :
```python
parc = ["PC-COMPTA-01", "PC-RH-02", "PC-DIR-03", "PORTABLE-04"]
```

**Résultat attendu :**
```
Le parc contient 4 postes :
1 - PC-COMPTA-01
2 - PC-RH-02
3 - PC-DIR-03
4 - PORTABLE-04
```

**Coup de pouce :** `len(parc)` donne le nombre d'éléments. Pour numéroter, `for i in range(len(parc)):` permet d'accéder à la fois à la position `i` et à l'élément `parc[i]`.

---

## Exercice 6 — Générateur d'adresses e-mail
**Notions :** chaînes de caractères, méthodes `.lower()`, concaténation

À l'arrivée d'un nouveau salarié, le service IT crée son adresse e-mail au format `prenom.nom@entreprise.fr`, tout en minuscules. Écris un programme qui demande un prénom et un nom, puis génère l'adresse.

**Résultat attendu (exemple) :**
```
Prénom ? Marie
Nom ? DUPONT
Adresse : marie.dupont@entreprise.fr
```

**Coup de pouce :** pour mettre du texte en minuscules, on utilise `prenom.lower()`. Pour assembler des morceaux de texte, on les additionne : `prenom + "." + nom + "@entreprise.fr"`.

---

## Exercice 7 — Une fonction réutilisable
**Notions :** fonctions (`def`), paramètres, valeur de retour

Les programmeurs évitent de réécrire le même code. Transforme le générateur d'e-mail de l'exercice 6 en une **fonction** `creer_email(prenom, nom)` qui renvoie l'adresse. Teste-la ensuite avec deux ou trois personnes différentes.

**Résultat attendu (exemple) :**
```
marie.dupont@entreprise.fr
ali.benali@entreprise.fr
```

**Coup de pouce :** une fonction se définit ainsi :
```python
def creer_email(prenom, nom):
    adresse = prenom.lower() + "." + nom.lower() + "@entreprise.fr"
    return adresse
```
On l'appelle ensuite avec `print(creer_email("Marie", "Dupont"))`.

---

## Mini-projet final — Petit outil de support
**Notions :** tout ce qui précède (boucle `while`, conditions, fonctions)

On combine tout dans un petit menu de support, comme un mini-outil interne. Le programme affiche un menu et répète tant que l'utilisateur ne choisit pas « Quitter » :

```
=== Outil de support IT ===
1 - Convertir des Mo en octets
2 - Créer une adresse e-mail
3 - Quitter
Votre choix ?
```

Selon le choix, le programme exécute l'action correspondante (en réutilisant le code des exercices précédents), puis réaffiche le menu. Le choix `3` arrête le programme.

**Coup de pouce :** on répète avec `while True:` et on sort de la boucle avec `break` quand l'utilisateur choisit `3`. Réutilise la fonction `creer_email` de l'exercice 7 plutôt que de réécrire le code.

---

## Pistes d'extension (si tu vas vite)

- **Exercice 5 :** ajouter un poste à l'inventaire avec `parc.append("NOUVEAU-PC")`, ou compter combien de noms contiennent le mot « PORTABLE ».
- **Exercice 3 :** vérifier aussi la présence d'une majuscule (`.isupper()`).
- **Mini-projet :** ajouter une option « 4 - Compter les postes du parc » qui réutilise l'inventaire de l'exercice 5.
- **Graphiques :** dans le notebook Basthon, tracer un petit diagramme avec `matplotlib` (par exemple le nombre de postes par service).
