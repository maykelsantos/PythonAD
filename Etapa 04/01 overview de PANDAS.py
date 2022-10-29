import pandas as pd
import numpy as np

dados = pd.read_csv('planilha.csv')
dados

# informação do tipo
type(dados)

# exibição das 5 primeiras linhas do arquivo
dados.head()

# exibição das 5 últimas linhas do arquivo
dados.tail()

# quantidade de linhas e colunas, respectivamente
dados.shape

# exibição das colunas em formato de 'array'
dados.columns

# quantidade de linhas duplicadas
dados.duplicated().sum() # 'duplicated()' resulta em 'True' se houver linhas duplicadas

# informações gerais do dataframe
dados.info()

# verificação da existência de NaN (exibe a quantidade de NaN de cada coluna)
dados.isna().sum()

# sumário estatístico do dataframe
dados.describe()

# sumário estatístico do dataframe, inclusive para variáveis categóricas
dados.describe(include = 'all')

# quantidade de valores únicos em cada coluna
dados.nunique()

# exibição dos valores únicos
dados['race/ethnicity'].unique()

# frequência dos valores especificados
dados['race/ethnicity'].value_counts()

# ordenação 01 do dataframe 
dados.sort_values('math score')

# ordenação 02 do dataframe
dados.sort_values(['math score', 'reading score', 'writing score'], ascending = False)\
    .reset_index(droop = True) # a '\' serve para quebrar a linha de código sem quebrar o código
    
# adicionando uma coluna de média por linhas
dados['media'] = dados.mean(axis = 1)

# consulta 01
dados.query('(gender == "male") & (`test preparation course` == "none") & (`math score` >= 70)')

# consulta 02
dados[(dados.gender == 'male') & (dados['test preparation course'] == 'none') & (dados['math score'] >= 70)]

# agrupamento - com estatísticas descritivas
dados.groupby(by = 'gender').agg([np.mean, np.median]).T
