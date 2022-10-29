import time

for qualquerCoisa in range(10): # lembrar que a contagem inicia do valor zero '0'
    print(qualquerCoisa)
    
for qualquerCoisa in range(1, 11): # delimitando início e fim
    print(qualquerCoisa)
    
for qualquerCoisa in range(0, 100, 5): # delimitando o espaço de contagem. Nesse caso '5'
    print(qualquerCoisa)

paises = ['Brasil', 'Argentina', 'Uruguai', 'Alemanha', 'Cuba', 'Moçambique', 'França']

for percurso in paises:
    print(percurso)
    time.sleep(1) # aguarda um segundo para executar o próximo código

for percurso in paises:
    if percurso == 'Brasil':
        print(percurso, ', este é o país pentacampeão do mundo!')
        time.sleep(1) # aguarda um segundo para executar o próximo código
    elif percurso == 'Alemanha':
        print(percurso, ', este país ganhou do Brasil de 7 x 1. Placar histórico!')
        time.sleep(1) # aguarda um segundo para executar o próximo código
    else:
        print(percurso)
        time.sleep(1) # aguarda um segundo para executar o próximo código