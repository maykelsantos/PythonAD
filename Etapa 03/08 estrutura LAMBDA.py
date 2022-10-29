# Exemplo 1 ---------

funcaoLambda1 = lambda valor: valor + 10
print(funcaoLambda1(1))

# Exemplo 2 ----------

funcaoLambda2 = lambda valor1, valor2: valor1 / valor2
print(funcaoLambda2(1, 5))

# Exemplo 3 ----------

funcaoLambda3 = lambda valor3: 'Verdadeiro' if valor3 % 2 == 0 else 'Falso'
import random
numero = random.randint(0, 100)
print(funcaoLambda3(numero),', o número é', numero)