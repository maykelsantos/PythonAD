# Exemplo 1 ----------

class pessoa:
    # Método construtor da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def boasVindas(self):
        print('Olá, ', self.nome, '. Seja bem vindo!')
        
    def naoAutorizado(self):
        print('Olá, ', self.nome, '. Infelizmente, seu acesso não está autorizado!')
        
    def maiorIdade(self):
        if self.idade >= 18:
            import time
            time.sleep(1)
            print('Verificando os dados [...]')
            time.sleep(1)
            print('Usuário é MAIOR de idade.')
            time.sleep(1)
            self.boasVindas()
        else:
            import time
            time.sleep(1)
            print('Verificando os dados [...]')
            time.sleep(1)
            print('Usuário é MENOR de idade.')
            time.sleep(1)
            self.naoAutorizado()
            
app = pessoa('Maykel', 28) # necessário atribuir a classe à uma variável
app.maiorIdade()