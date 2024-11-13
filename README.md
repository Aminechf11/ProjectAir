# Nettoyage des données de qualité de l'air

Ce script permet de nettoyer un jeu de données sur la qualité de l'air en supprimant les doublons, en traitant les valeurs manquantes et en filtrant les données incohérentes. Les colonnes concernées incluent les concentrations de polluants (`no2`, `o3`, `pm10`), ainsi que les informations `date` et `ninsee` (identifiant géographique).

## Étapes de nettoyage

1. **Suppression des doublons** : On élimine les lignes dupliquées dans l'ensemble de données.
2. **Traitement des valeurs manquantes** : Les lignes avec des valeurs manquantes dans les colonnes essentielles (`date`, `ninsee`, `no2`, `o3`, `pm10`) sont supprimées.
3. **Conversion des types de données** : La colonne `date` est convertie en `datetime`, et les colonnes de concentrations (`no2`, `o3`, `pm10`) sont converties en valeurs numériques. Les valeurs non valides sont transformées en `NaN`.
4. **Filtrage des valeurs incohérentes** : Les lignes avec des concentrations négatives ou invalides pour les polluants sont supprimées.
5. **Suppression des doublons spécifiques** : Si plusieurs mesures existent pour une même `date` et un même `ninsee`, la première occurrence est conservée.
6. **Réinitialisation de l'index** : L'index du DataFrame est réinitialisé après nettoyage.

## Exemple de fichier CSV

Le fichier d'entrée devrait contenir des colonnes comme suit :
| date       | ninsee | no2  | o3   | pm10 |
|------------|--------|------|------|------|
| 2022-01-01 | 12345  | 40   | 100  | 30   |

## Sauvegarde

Après nettoyage, les données sont sauvegardées dans un nouveau fichier `cleaned_air_quality.csv`.

# Prédiction de la qualité de l'air avec un arbre de décision

Ce script utilise un **arbre de décision** pour classifier la qualité de l'air en fonction des concentrations de polluants (`no2`, `o3`, `pm10`). L'objectif est de prédire si la qualité de l'air est **"Bonne"**, **"Moyenne"**, ou **"Faible"**.

## Étapes principales

1. **Création de la colonne cible** : 
   - La qualité de l'air est classée en trois catégories : 
     - **Bonne** : concentrations faibles.
     - **Moyenne** : concentrations modérées.
     - **Faible** : concentrations élevées.

2. **Modélisation avec un arbre de décision** :
   - Un modèle d'arbre de décision est entraîné pour prédire la qualité de l'air à partir des concentrations de polluants.

3. **Évaluation du modèle** :
   - La précision du modèle est calculée sur un jeu de test.


## Conclusion

Ce script nettoie les données de qualité de l'air pour éliminer les doublons et les valeurs incohérentes, et rendre les données prêtes pour l'analyse.Ainsi , nous pouvons par la suite prédire la qualité de l'air en fonction de certains paramètres tel que no2 ,o3 et pm10 .
