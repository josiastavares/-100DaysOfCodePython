#Revisão: fazer um programa que simula uma lista de tarefas (CRUD básico)

var_decisao = 0

while var_decisao != 5:

    var_decisao = input("Digite sua opção: \n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Editar tarefa\n4 - Remover tarefa\n5 - Sair\n")
    try:
        var_decisao = int(var_decisao)
        if var_decisao == 1:
            var_tarefa = input("Digite a tarefa: ")
            arq1 = open("dia17/lista_tarefas2.txt", "a")
            arq1.write(var_tarefa + "\n")
            arq1.close()
            print("Tarefa adicionada com sucesso!")

        elif var_decisao == 2:
            arq1 = open("dia17/lista_tarefas2.txt", "r")
            print(arq1.read())
            arq1.close()

        elif var_decisao == 3:
            arq1 = open("dia17/lista_tarefas2.txt", "r")
            lista_tarefas = arq1.readlines()
            arq1.close()

            for i, tarefa in enumerate(lista_tarefas):
                print(f"{i + 1} - {tarefa.strip()}")

            var_numero_tarefa = int(input("Digite o número da tarefa que deseja editar: ")) - 1
            var_nova_tarefa = input("Digite a nova tarefa: ")
            lista_tarefas[var_numero_tarefa] = var_nova_tarefa + "\n"

            arq1 = open("dia17/lista_tarefas2.txt", "w")
            arq1.writelines(lista_tarefas)
            arq1.close()
            print("Tarefa editada com sucesso!")

        elif var_decisao == 4:
            arq1 = open("dia17/lista_tarefas2.txt", "r")
            lista_tarefas = arq1.readlines()
            arq1.close()

            for i, tarefa in enumerate(lista_tarefas):
                print(f"{i + 1} - {tarefa.strip()}")

            var_numero_tarefa = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            del lista_tarefas[var_numero_tarefa]

            arq1 = open("dia17/lista_tarefas2.txt", "w")
            arq1.writelines(lista_tarefas)
            arq1.close()
            print("Tarefa removida com sucesso!")

        elif var_decisao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Erro: Você não digitou um número válido.")
        continue