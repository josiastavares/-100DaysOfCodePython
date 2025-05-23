#Criar uma classe Pessoa com atributos nome e idade e método falar.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

pessoa1 = Pessoa("Eduardo", 20)
pessoa1.falar()