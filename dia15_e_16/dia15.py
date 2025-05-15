#dia 15
#Criar um programa que escreve uma lista de tarefas em um arquivo .txt, utilizando os métodos open e write.

arq1 = open("dia15_e_16/lista_tarefas.txt", "w")
arq1.write("Colocar roupas para lavar\n")
arq1.write("Fazer Almoço\n")
arq1.write("Lavar a louça\n")
arq1.write("Estudar Python\n")
arq1.write("Fazer exercícios\n")
arq1.close()

#dia 16
#Criar um programa que lê o arquivo .txt criado no dia 15 e imprime seu conteúdo na tela.

arq1 = open("dia15_e_16/lista_tarefas.txt", "r")
print(arq1.read())
arq1.close()