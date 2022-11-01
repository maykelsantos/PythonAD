import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)

# vetor com números aleatórios entre 1 e 1.500, com 10 amostras 
y = np.random.randint(low = 1, high = 1500, size = 10)
y

# gráfico de linha simples
plt.plot(y)

# inserção da primeira linha no plot
plt.plot(y, color = '#43E60E', marker = 'o', ms = 5, mec = 'yellow',\
    markerfacecolor = 'blue', ls = '-.')
        # color = define a cor da linha
        # marker = define o estilo do marcador
        # ms = define o tamanho do marcador
        # mec = define a cor da linha do marcador
        # markerfacecolor = define a cor da face do marcador
        # ls = define o estilo da linha

# inserção da segunda linha do plot (multiplicando 'y' por 2)
plt.plot(y * 2, marker = '+', color = 'green', ms = 5)
        # marker = define o estilo do marcador
        # color = define a cor da linha
        # ms = define o tamanho do marcador

# rótulos
plt.xlabel('Eixo X', color = 'red', size = 12)
plt.ylabel('Eixo Y')
plt.title('Título', loc = 'left') # loc = localização do título

# gridlines
plt.grid(axis = 'y', color = 'gray', linestyle = '--', linewidth = 1,\
    alpha = 0.8)
        # axis = define em qual eixo deve exibir o gridline
        # alpha = define a opacidade da linha
plt.show()

# diversos plot na mesma visualização
np.random.seed(6)
x = np.arange(1, 11)
y1 = np.random.randint(1, 400, 10)
y2 = np.random.randint(150, 500, 10)
y3 = np.random.randint(200, 600, 10)

plt.figure(figsize = (15, 5)) # define o tamanho da figura
plt.suptitle('Figura', fontsize = 15) # define o título e o tamanho da fonte da figura

plt.subplot(1, 3, 1) # respectivamente, 1 linha, 3 coluna, plot na coluna 1
plt.plot(x, y1, color = 'green')
plt.title('Subplot 1', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 2)
plt.plot(x, y2, color = 'blue')
plt.title('Subplot 2', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 3)
plt.plot(x, y3, color = 'red')
plt.title('Subplot 3', pad = 10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.tight_layout(pad = 4) # define o espaçamento entre os plots
plt.show()

# diversos plot na mesma visualização exemplo 2
fig, ax = plt.subplots(1, 3, figsize = (15, 5))
fig.suptitle('Figure')
ax[0].plot(x, y1, color = 'gray') # linha 0, coluna 0
ax[1].plot(x, y2, color = 'yellow') # linha 0, coluna 1
ax[2].plot(x, y3, color = 'orange') # linha 0, coluna 2

for i in range(3):
    ax[1].set(title = f'Subplot {i+1}', xlabel = 'Eixo X', ylabel = 'Eixo Y')
    