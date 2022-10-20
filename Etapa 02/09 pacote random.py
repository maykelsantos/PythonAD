import random

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(lista1)) # sorteio um valor

palavra = 'Maykel'
print(random.choice(palavra)) # sorteia uma letra, quando a variável for string

familia = [
    'Maykel',
    'Vitória',
    'Miguel',
    'Marcos',
    'Jaqueline'
]
print(random.choice(familia)) # sorteia um valor, quando lista ou tupla

print(random.random()) # sorteia um número entre 0 e 1
print(random.randint(0, 10)) # sorteia um núemro inteiro entre os valores especificados