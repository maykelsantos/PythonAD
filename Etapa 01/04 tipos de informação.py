# Tipo de Informação

# Na programação, o tipo de dados é um conjunto importante. Variáveis podem armazenar dados de diversos tipos
# e diversos tipos podem fazer coisas diferentes.
# O python tem os seguintes tipos de dados integrados por padrão:

string = str('Olá mundo!')
inteiro = int(28)
flutuante = float(2.8)
compleX = complex(1j)
lista = list(['maça', 'uva'])
tupla = tuple(('A', 'B'))
rangE = range(8)
dicionario = dict(nome = 'Maykel', age = 28)
seT = set(('A', 'B', 'C'))
frozenseT = frozenset(('A', 'B', 'C'))
Boleano = bool(5)
byteS = bytes(5)
byteArray = bytearray(5)
memoryView = memoryview(bytes(5))

from datetime import datetime
data = datetime.today().date()