# 'append' adiciona valores à lista

listaVazia = []

print(listaVazia)

listaVazia.append(1)
listaVazia.append(2)
listaVazia.append(3)
listaVazia.append('Valor')

print(listaVazia)

# 'clear' exclui todo os valores de uma lista

listaVazia.clear()
print(listaVazia)

# 'insert' insere valor especificado à uma lista na posição que você informar

listaVazia.insert(0, 0)
listaVazia.insert(3, 1.5)
listaVazia.insert(6, 'Dinheiro')

print(listaVazia)

# 'extend' extende uma lista com outra lista

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)

print(lista1)

# 'remove' remove um valor especificado de uma lista

lista1.remove(5)

print(lista1)

# 'pop' remove uma valor de uma lista especificado pela posição

lista1.pop(0)

print(lista1)

# 'sort' ordena os valores de A a Z

listaDeLetra = ['a', 'z', 'g', 'm', 'i', 'y', 'q', 's']
listaDeLetra.sort()

print(listaDeLetra)

# para ordenar os valores de Z a A

listaDeLetra.sort(reverse=True)
print(listaDeLetra)

# 'index' evidencia a posição que determinado valor se encontra na lista
print(listaDeLetra.index('y'))