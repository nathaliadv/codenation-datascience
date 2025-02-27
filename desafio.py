# -*- coding: utf-8 -*-
"""DESAFIO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dPOg1qIgJPmE_yqmRZp5C1Tk8mV1N0n1
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

df_train = pd.read_csv('/content/drive/My Drive/CODENATION/train.csv', sep="," , encoding="UTF8" )
df_test = pd.read_csv('/content/drive/My Drive/CODENATION/test.csv', sep="," , encoding="UTF8" )

df_train.corr()

atributos = [
    'NU_NOTA_CN',
    'NU_NOTA_CH',
    'NU_NOTA_LC',
    'NU_NOTA_REDACAO']

atributos_corr = [
    'NU_NOTA_MT',
    'NU_NOTA_CN',
    'NU_NOTA_CH',
    'NU_NOTA_LC',
    'NU_NOTA_REDACAO']

df_train[atributos].isnull().sum()

df_test[atributos].isnull().sum()

#Testando o número de ausentes ou eliminados no primeiro dia (CN e CH) e segundo dia (LC, MT e REDACAO) para dataset treino e teste
#Diferente de 1 (!=) porque 1 corresponde a presente. 0 e 2 correspondem, respectivamente, a falta e eliminação.

presenca_1 = df_train['TP_PRESENCA_CN']
res_1 = sum(map(lambda i: i != 1, presenca_1))
print(res_1)

presenca_2= df_train['TP_PRESENCA_LC']
res_2 = sum(map(lambda i: i != 1, presenca_2))
print(res_2)


presenca_3 = df_test['TP_PRESENCA_CN']
res_3 = sum(map(lambda i: i != 1, presenca_3))
print(res_3)

presenca_4= df_test['TP_PRESENCA_LC']
res_4 = sum(map(lambda i: i != 1, presenca_4))
print(res_4)

#O número de ausentes e eliminados é igual a quantidade de "isnull" no passo anterior. Logo, os nulos corresponde a provas 
#não feitas (zeraram).

corr = df_train[atributos_corr].corr()
ax = plt.subplots(figsize=(11, 8))
sns.heatmap(corr,  annot=True)

x0 = df_train['NU_NOTA_CN'].fillna(0)
x1 = df_test['NU_NOTA_CN'].fillna(0)
sns.distplot(x0)
sns.distplot(x1)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x2 = df_train['NU_NOTA_CH'].fillna(0)
x3 = df_test['NU_NOTA_CH'].fillna(0)
sns.distplot(x2)
sns.distplot(x3)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x4 = df_train['NU_NOTA_LC'].fillna(0)
x5 = df_test['NU_NOTA_LC'].fillna(0)
sns.distplot(x4)
sns.distplot(x5)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x6 = df_train['NU_NOTA_REDACAO'].fillna(0)
x7 = df_test['NU_NOTA_REDACAO'].fillna(0)
sns.distplot(x6)
sns.distplot(x7)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

#Acima foram plotados alguns gráficos para ver a distribuição dos dados.
#Há uma grande parte de notas zeradas pois os valores null foram preenchidos com 0.
#Serão removidas as notas zero do dataset de treino

# Seleciona somente as seguintes linhas com valores diferentes de 0 e não nulos do dataset de treino
df_train = df_train.loc[
      (df_train['NU_NOTA_CN'].notnull()) & (df_train['NU_NOTA_CN'] != 0) & (df_train['NU_NOTA_CH'].notnull()) & (df_train['NU_NOTA_CH'] != 0) 
      & (df_train['NU_NOTA_LC'].notnull()) & (df_train['NU_NOTA_LC'] != 0)
      & (df_train['NU_NOTA_REDACAO'].notnull()) & (df_train['NU_NOTA_REDACAO'] != 0)    
]

# Seleciona somente as seguintes linhas com valores diferentes de 0 e não nulos do dataset de teste
df_test = df_test.loc[
      (df_test['NU_NOTA_CN'].notnull()) & (df_test['NU_NOTA_CN'] != 0) & (df_test['NU_NOTA_CH'].notnull()) & (df_test['NU_NOTA_CH'] != 0) 
      & (df_test['NU_NOTA_LC'].notnull()) & (df_test['NU_NOTA_LC'] != 0) & (df_test['NU_NOTA_REDACAO'].notnull()) & (df_test['NU_NOTA_REDACAO'] != 0)    
]

df_train[atributos].isnull().sum()

df_test[atributos].isnull().sum()

x0 = df_train['NU_NOTA_CN'].fillna(0)
x1 = df_test['NU_NOTA_CN'].fillna(0)
sns.distplot(x0)
sns.distplot(x1)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x2 = df_train['NU_NOTA_CH'].fillna(0)
x3 = df_test['NU_NOTA_CH'].fillna(0)
sns.distplot(x2)
sns.distplot(x3)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x4 = df_train['NU_NOTA_LC'].fillna(0)
x5 = df_test['NU_NOTA_LC'].fillna(0)
sns.distplot(x4)
sns.distplot(x5)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

x6 = df_train['NU_NOTA_REDACAO'].fillna(0)
x7 = df_test['NU_NOTA_REDACAO'].fillna(0)
sns.distplot(x6)
sns.distplot(x7)
plt.legend(labels=['TRAIN','TEST'], ncol=2, loc='upper left');

#Gerando os gráficos novamente percebe-se agora temos dados muito 
#mais homogêneos entre teste e treino do que quando iniciamos a nossa análise.

X_train = df_train[atributos]
y_train = df_train['NU_NOTA_MT']
X_test = df_test[atributos]

#Normalização dos dados usando o StandardScaler()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()  
X_train = scaler.fit_transform(X_train)  
X_test = scaler.transform(X_test)

# Usando o modelo RandomForestRegressor para fazer a regressão

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor( 
           criterion='mae', 
           max_depth=8,
           max_leaf_nodes=None,
           min_impurity_split=None,
           min_samples_leaf=1,
           min_samples_split=2,
           min_weight_fraction_leaf=0.0,
           n_estimators= 500,
           n_jobs=-1,
           random_state=0,
           verbose=0,
           warm_start=False
)

regressor.fit(X_train, y_train)

y_pred_test = regressor.predict(X_test)

y_pred_train = regressor.predict(X_train)

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_train, y_pred_train))
print('MSE:', metrics.mean_squared_error(y_train, y_pred_train))  
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, y_pred_train)))

resposta = pd.DataFrame({'NU_INSCRICAO': df_test['NU_INSCRICAO'], 'NU_NOTA_MT': y_pred_test})
resposta

resposta.to_csv('/content/drive/My Drive/CODENATION/answer.csv',index=False)

