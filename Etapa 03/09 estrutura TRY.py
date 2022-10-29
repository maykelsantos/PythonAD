# Exemplo 1 ---------

try:
    0 / 0 # exemplo de erro, pois não é possível essa operação matemática
except:
    print('[***ERRO***]')
finally:
    print('Continuando [...]')
    
# Exemplo 2 ---------

try:
    variavel # exemplo de erro, essa variável não existe
except:
    print('[***ERROR***]')
finally:
    print('Continuando [...]')