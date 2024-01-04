#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


#je commence par importer le DataFrame
df = pd.read_csv('/Users/octoberone/Desktop/DataFrame GitHub/DataFrame/Détection de fraude bancaire.csv')


# In[3]:


#affichage des 5 premières lignes
df.head()


# In[4]:


#voici le nombre de lignes et de colonnes sans le détail
df.shape


# In[5]:


#voici les détails des colonnes avec beaucoup plus d'informations (variables, types, le nombre de valeurs nulles)
df.info()


# In[6]:


#par souci du détail, j'ai utilisé cette commande pour être sûr qu'il n'y a pas de valeurs manquantes
df.isnull().sum()
#par conséquent, j'en déduis que ce DataFrame est plutôt agréable à utiliser dans un premier temps


# In[7]:


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


# In[17]:


#premier affichage d'histogramme afin de visualiser la tendance et son évolution dans le temps
#conclusion : La majorité des transactions sont inférieures à 30 dollars, 
#avec un nombre important de transactions inférieures à 5 dollars, allant jusqu'à 17 500 transactions

plt.figure(figsize=(20, 5))
    
plt.subplot(1, 2, 1)
sns.histplot(df[df["Amount"] <= 30]["Amount"], bins=100, kde=True,label='Fraude')

sns.set_style("whitegrid")
plt.title("Distribution des Montants des Transactions inférieur à 30 Dollard")
plt.xlabel("Montant")
plt.ylabel("Nombre de Transactions")
plt.legend(title="Légende")

plt.show()

