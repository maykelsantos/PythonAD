import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
#import warnings
#warnings.filterwarnings('ignore')

# banco de dados do pacote seaborn
base_dados = sbn.load_dataset('iris')

# amplitude total
base_dados['sepal_length'].max() - base_dados['sepal_length'].min()