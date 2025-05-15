#Criar um mini programa para manipular frases digitadas pelo usuário utilizando split, upper, lower, strip e replace

var_frase = input("Digite uma frase com um traço(-) no começo e no fim: ")

#O split divide a string em uma lista de palavras
print("A frase dividida em palavras é:", var_frase.split())
#O upper transforma a frase em maiúsculas
print("A frase em maiúsculas é:", var_frase.upper())
#O lower transforma a frase em minúsculas
print("A frase em minúsculas é:", var_frase.lower())
#O strip remove os itens indicados no primeiro e último caractere da string
print("A frase sem os traços é:", var_frase.strip("-"))
#O replace substitui uma letra por outra
print("A frase com 'a' substituída por 'e' é:", var_frase.replace("a", "e"))