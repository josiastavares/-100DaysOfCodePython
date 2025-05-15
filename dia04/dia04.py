#Criação de um programa que verifica se um numero é impar, par ou zero

valor = int(input("Digite um número: "))

if valor == 0:
    print("O número é zero.")
elif valor % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
