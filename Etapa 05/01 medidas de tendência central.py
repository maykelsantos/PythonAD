import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
#import warnings
#warnings.filterwarnings('ignore')

# banco de dados do pacote seaborn
base_dados = sbn.load_dataset('iris')

# exibir os 5 primeiros dados
print(base_dados.head())

# resumo dos dados avaliados
print('O resumo dos dados:', base_dados.shape)

# média aritmética
print('A média é:', base_dados['petal_length'].mean())

# moda
print('A moda é:', base_dados['petal_length'].mode())

# mediana
print('A mediana é:', base_dados['petal_length'].median())

# 