string = 'Olá Mundo!'
cpf = 'CPF: 4359701454'
meuNome = 'maykel'

print(string)
print(len(string)) # contagem dos cacteres ou dos valores
print(type(string)) # evidencia o tipo do valor dentro da variável
print(string+' <- concatenar') # concatenação
print(string.replace('Mundo', 'Jesus')) # substitui o valor especificado, mas não alterado a variável em si
print(cpf.replace('CPF: ', '')) # segundo exemplo de substituição
print(string.startswith('Olá')) # verifica se o início da variável tem os caracteres especificados
print(string.endswith('!')) # verifica se o fim da variável tem os caracteres especificados
print(cpf.count('4')) # realiza a contagem dos caracteres especificados dentro da variável
print(meuNome.capitalize()) # transforma o primeiro caractér da string em maiúscula
print(meuNome.upper()) # transforma todas as caracteres das string em maiúscula