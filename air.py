import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Charger la table (remplace le chemin réel de ton fichier CSV ou TSV)
df = pd.read_csv("indices_QA_commune_IDF_2016.csv", sep=',')  # Remplace par le chemin réel de ton fichier

# Afficher les premières lignes pour vérifier la structure des données
print(df.head())

# Création de la colonne 'air_quality' en fonction des seuils
def classify_air_quality(row):
    # Définir les seuils pour chaque polluant
    if row['no2'] > 40 or row['o3'] > 180 or row['pm10'] > 50:  # Faible
        return 'Faible'
    elif row['no2'] > 20 or row['o3'] > 100 or row['pm10'] > 30:  # Moyenne
        return 'Moyenne'
    else:  # Bien
        return 'Bien'

# Appliquer la fonction pour créer la colonne 'air_quality'
df['air_quality'] = df.apply(classify_air_quality, axis=1)

# Encodage des variables catégorielles (target)
le = LabelEncoder()
df['air_quality'] = le.fit_transform(df['air_quality'])

#NETTOYAGE DES DONNEES
df = df.drop_duplicates()
df = df.dropna(subset=['no2', 'o3', 'pm10'])#On retire les lignes ou l'on a pas de données sur la qualité de l'air

# - Suppression des lignes avec des concentrations invalides (NaN ou inférieures à 0)
df = df[(df['no2'] >= 0) & (df['o3'] >= 0) & (df['pm10'] >= 0)]

# Si un doublon existe pour une même date et un même "ninsee", on pourrait vouloir conserver la première entrée seulement
df = df.drop_duplicates(subset=['date', 'ninsee'], keep='first')

# Sélectionner les variables explicatives (features) et la variable cible (target)
X = df[['no2', 'o3', 'pm10']]  # Variables explicatives
y = df['air_quality']  # Variable cible (air_quality)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Créer et entraîner l'arbre de décision avec le critère de Gini
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X_train, y_train)

# Prédire les résultats sur l'ensemble de test
y_pred = clf.predict(X_test)

# Afficher les résultats
print(f"Exactitude du modèle : {accuracy_score(y_test, y_pred):.4f}")
print("Rapport de classification :")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Visualisation de l'arbre de décision
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(15, 10),dpi=300)
plot_tree(clf, filled=True, feature_names=X.columns, class_names=le.classes_, rounded=True, fontsize=12)
plt.show()
