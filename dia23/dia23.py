#Criar exemplos simples de map, filter e reduce usando listas de números

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exemplo de map: multiplicar cada número da lista por 2

def multiplicar_por_dois(numero):
    return numero * 2

numeros_multiplicados = list(map(multiplicar_por_dois, lista_numeros))

print("Lista multiplicada por 2:", numeros_multiplicados)

# Exemplo de filter: filtrar números pares da lista

def eh_par(numero):
    return numero % 2 == 0

numeros_pares = list(filter(eh_par, lista_numeros))

print("Lista de números pares:", numeros_pares)

# Exemplo de reduce: somar todos os números da lista

from functools import reduce
def somar(x, y):
    return x + y
soma_total = reduce(somar, lista_numeros)
print("Soma total da lista:", soma_total)