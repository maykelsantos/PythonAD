import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
#import warnings
#warnings.filterwarnings('ignore')

# banco de dados do pacote seaborn
base_dados = sbn.load_dataset('iris')

# descrição de uma coluna
print(base_dados['sepal_length'].describe())

# gráfico 01
sbn.boxplot(base_dados['sepal_length'])