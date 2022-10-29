import random

#---------

parar = 0

while parar <= 10:
    print(parar)
    parar = parar + 1
    
#----------

loop = 0
while loop <= 10:
    print(loop)
    if loop == 5:
        for x in range(10):
            print(x)
    loop = loop + 1
    
#----------
# Jogo de Exemplo

while True:
    jogador1 = random.randint(0, 10)
    jogador2 = random.randint(0, 10)
    print('Jogador 1 tirou o valor ', jogador1)
    print('Jogador 2 tirou o valor ', jogador2)
    if jogador1 > jogador2:
        print('Jogador 1 ganhou o jogo!')
        break
    print('\n')