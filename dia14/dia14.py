#Criar um programa que pede um número e trata erro caso o usuário digite texto

var_numero = input("Digite um número: ")
try:
    var_numero = int(var_numero)
    print("O número digitado foi:", var_numero)
except ValueError:
    print("Erro: Você não digitou um número válido.")