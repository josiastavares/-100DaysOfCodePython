#Projeto pequeno: Sistema simples de cadastro de pessoas usando classes.

# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Definindo a classe Cadastro
class Cadastro:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        print(f"{pessoa.nome} foi adicionado ao cadastro.")

    def listar_pessoas(self):
        print("Lista de pessoas cadastradas:")
        for pessoa in self.pessoas:
            print(f"- {pessoa.nome}, {pessoa.idade} anos")

# Função principal
def main():
    cadastro = Cadastro()

    while True:
        print("\n1. Adicionar pessoa")
        print("2. Listar pessoas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            pessoa = Pessoa(nome, idade)
            cadastro.adicionar_pessoa(pessoa)
        elif opcao == "2":
            cadastro.listar_pessoas()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

