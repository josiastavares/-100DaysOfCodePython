#Projeto pequeno: Calculadora simples (operações +, -, *, /).

opcao = 0

while opcao != 5:
    print("Escolha uma opção: \n 1. Adição \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n 5. Sair")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado: {resultado}")

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado: {resultado}")

    elif opcao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"Resultado: {resultado}")

    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif opcao == 5:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente.")