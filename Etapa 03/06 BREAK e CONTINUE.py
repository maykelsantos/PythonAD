# Exemplo 01 ----------
frutas = ['Mamão', 'Laranja', 'Pêra', 'Limão', 'Maracujá', 'Acerola']
for fruta in frutas:
    print(fruta)
    if fruta == 'Pêra':
        print('A fruta acima fez meu código parar.')
        break
    
# Exemplo 02 ----------
for loop in range (0, 11):
    if loop == 5:
        print('Cheguei até o 5')
        continue
    print(loop)