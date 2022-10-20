import statistics

lista1 = [1, 61, 512, 14, 84, 36, 95, 645, 741]
print(sum(lista1) / len(lista1)) # evidencia a média sem utilizar o pacote
print(statistics.mean(lista1)) # evidencia a média
print(statistics.median(lista1)) # evidencia a mediana
print(statistics.mode(lista1)) # evidencia a moda