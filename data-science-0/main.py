#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.info()


# In[4]:


black_friday.head()


# In[5]:


black_friday['Age'].unique()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[6]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[7]:


def q2():
    return len(black_friday.loc[black_friday['Age'] == '26-35'].loc[black_friday['Gender'] == 'F'])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[8]:


def q3():
    return len(set(black_friday['User_ID']))


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[9]:


def q4():
    return len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[16]:


def q5():
    without_nan = len(black_friday) - len(black_friday.dropna())
    total = without_nan / len(black_friday)
    return total


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[28]:


def q6():
    return int(black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[12]:


def q7():
    return black_friday['Product_Category_3'].value_counts().idxmax()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[32]:


def q8():
    max_val = black_friday['Purchase'].max()
    min_val = black_friday['Purchase'].min()
    normalize = (black_friday['Purchase'] - min_val) / (max_val - min_val)
    mean = normalize.mean()
    return float(mean)


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[14]:


def q9():
    mean_val = black_friday['Purchase'].mean() 
    std_val = black_friday['Purchase'].std()
    padronize = ((black_friday['Purchase'] - mean_val)/std_val)
    count = padronize.loc[padronize >= -1 ].loc[padronize <= 1]
    return len(count)


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[19]:


def q10():
    aux = black_friday.loc[black_friday['Product_Category_2'].isnull()]
    return all(aux['Product_Category_3'].isnull())

