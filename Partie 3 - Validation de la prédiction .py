#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import roc_auc_score, roc_curve


# In[5]:


#je commence par importer le DataFrame
df = pd.read_csv('/Users/octoberone/Desktop/DataFrame GitHub/DataFrame/Détection de fraude bancaire.csv')


# In[6]:


#affichage des 5 premières lignes
df.head()


# In[7]:


#voici le nombre de lignes et de colonnes sans le détail
df.shape


# In[8]:


#voici les détails des colonnes avec beaucoup plus d'informations (variables, types, le nombre de valeurs nulles)
df.info()


# In[9]:


#par souci du détail, j'ai utilisé cette commande pour être sûr qu'il n'y a pas de valeurs manquantes
df.isnull().sum()
#par conséquent, j'en déduis que ce DataFrame est plutôt agréable à utiliser dans un premier temps


# In[10]:


#Afin d'avoir plus de détails statistiques, j'affiche les colonnes numériques

#count%:nombre de valeurs nulles
#mean%:la moyenne des valeurs
#std%:l'écart type (dispersion valeurs)
#min%:le min de la colonne 
#25%:1er quatile à moins de 25
#50%:2er quatile à moins de 25
#75%:3er quatile à moins de 25
#max:le maxi de la colonne 

print(df.describe())


# In[11]:


#premier affichage d'histogramme afin de visualiser la tendance et son évolution dans le temps
#conclusion : La majorité des transactions sont inférieures à 30 dollars, 
#avec un nombre important de transactions inférieures à 5 dollars, allant jusqu'à 17 500 transactions

plt.figure(figsize=(20, 5))
    
plt.subplot(1, 2, 1)
sns.histplot(df[df["Amount"] <= 30]["Amount"], bins=100, kde=True, color= "y", label='Fraude')

sns.set_style("whitegrid")
plt.title("Distribution des Montants des Transactions inférieur à 30 Dollard")
plt.xlabel("Montant")
plt.ylabel("Nombre de Transactions")
plt.legend(title="Légende")

plt.show()


# In[12]:


#dans cette étape, je vérifie la présence des deux classes
#de plus je les affiche, j'en déduis que la classe 1 est celle qui a des transactions frauduleuses
class_ = df['Class'].value_counts()

if len(class_) == 2:
    print("il y à deux classe")
    for class_index in class_.index:
        print(f"Class {class_index}:", class_[class_index])
else:
    print("il y à pas deux classe")


# In[13]:


#Par cela, j'affiche dans un histogramme les classes, dans celui-ci malheureusement la faible présence de transactions frauduleuses
#ne ne permet pas de les apercevoir visuellement
plt.figure(figsize=(8, 5))
sns.countplot(x="Class",color= "red",label="Class", data=df)

sns.set_style("whitegrid")
plt.title("Class des transactions")
plt.xlabel("Classe")
plt.ylabel("Transactions")
plt.legend(title="Transactions des client")

plt.show()


# In[14]:


#premièrement, je vais séparer les colonnes dans la variable X sauf 'Class' dans Y
#pour isoler les caractéristiques de l'entraînement
X = df.drop("Class", axis=1)
y = df["Class"]


# In[15]:


#maintenant je vais fractionner le jeu de données
#pour tester la performance de la prédiction
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[16]:


#Ensuite une normalisation
#pour améliorer les résultats
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[17]:


#et enfin un entraînement du modèle
#pour finaliser notre prédiction 
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


# In[18]:


#après avoir fait cela, il suffit juste de prédire les transactions frauduleuses sur la prédiction établie
y_pred = model.predict(X_test)


# In[19]:


#Voici les affichages de ce travail:
#Un accuracy score: pour mesurer la proportion totale (prédiction correcte / nombre total de prédictions)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')


# In[20]:


#Un classification report: pour mesurer la prédiction avec plus de détail (précision, rappel, score F1, support)
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)


# In[21]:


#une confusion matrix: pour avoir un visuel sur la prédiction correcte et les erreurs dont :
#56862: sont identifiées correctement comme non frauduleuses (BON)
#2: sont identifiées comme non frauduleuses mais sont frauduleuses (FAUX)
#23:sont identifiées comme frauduleuses mais sont non frauduleuses (FAUX)
#75: sont identifiées correctement comme frauduleuses (BON)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)


# In[22]:


plt.figure(figsize=(5, 5))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues", cbar=True)
plt.xlabel("Avec la prédiction")
plt.ylabel("Vrais valeurs")
plt.title("Confusion Matrix")
plt.show()


# In[26]:


#dans ce partie de code, je vais utiliser le model entrainer présedament 
#pour générer la probabiliter prédite du model 
#puis le score auc, pour évaluer le model (positif, négatif)
y_probs = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_probs)


# In[34]:


#et enfin l'affichage des deux courbe pour savoir le bon et le moin bon de la prédiction 
#dans ce graphique nous pouvons aprercevoir une bonne perfoamance de prédiction 
fpr, tpr, _ = roc_curve(y_test, y_probs)

plt.figure(figsize=(20, 5))
plt.plot(fpr, tpr, color= "y", label="ROC")
plt.plot([0, 1], [0, 1],color= "r", linestyle='--')
plt.xlabel("Faux positif")
plt.ylabel("Vrai Positif")
plt.title("Courbe ROC")
plt.legend(title="Légende")
plt.show()

