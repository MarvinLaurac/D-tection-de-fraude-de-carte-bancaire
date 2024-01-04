#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[3]:


#je commance part importer le DataFrame 
df = pd.read_csv('/Users/octoberone/Desktop/DataFrame GitHub/DataFrame/Détection de fraude bancaire.csv')


# In[3]:


#affichage des 5 premiere ligne 
df.head()


# In[4]:


#voici le nombre de ligne est de cologne sans le detail 
df.shape


# In[5]:


#voi les destaille des collogne avec beaucoup plus d'information (variable, type, le nombre de valeurs null)
df.info()


# In[6]:


#par le souci du detaille, j'ai bien tutiliser cette commande pour etre sur q'il y à pas de valeur manquants
df.isnull().sum()
#par cela j'en deduit que cette DataFram est plutot agreable à utiliser dans un pemier temps 


# In[7]:


#afin d'avoir plus de detaille statistique, j'affiche les collenne numérique 

#count%:nombre de valeurs nulles
#mean%:la moyenne des valeurs
#std%:l'écart type (dispersion valeurs)
#min%:le min de la colonne 
#25%:1er quatile à moins de 25
#50%:2er quatile à moins de 25
#75%:3er quatile à moins de 25
#max:le maxi de la colonne 
print(df.describe())


# In[17]:


#premiere affichage d'istogramme afin de fisualiser la tendence avec ces sont évolution dans le temps 
#Conclusion: nous avons la majorité des transaction qui sont inférieur à 30 dollard avec un nombre importent
#de transaction inférieur à 5 dollard alan de 17500 transaction.

plt.figure(figsize=(20, 5))
    
plt.subplot(1, 2, 1)
sns.histplot(df[df["Amount"] <= 30]["Amount"], bins=100, kde=True,label='Fraude')

sns.set_style("whitegrid")
plt.title("Distribution des Montants des Transactions inférieur à 30 Dollard")
plt.xlabel("Montant")
plt.ylabel("Nombre de Transactions")
plt.legend(title="Légende")

plt.show()

