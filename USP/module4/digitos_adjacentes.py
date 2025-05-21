# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima 'sim'; se não existir, imprima 'não'.

# solicitar ao usuário um valor numérico
n = input("Digite um valor numérico: ")

# iniciar a variável i com valor 0
i = 0

# iniciar a variável com valor booleano
ehIgual = False

# enquanto i for menor que o tamanho da string - 1
while i < len(n) - 1:
    # verificar se o índice da string é igual ao próximo valor do índice
    if n[i] == n[i + 1]:
        ehIgual = True
    i = i + 1

# verificar se a variável booleana ainda é verdadeira
if ehIgual:
    # exibir mensagem
    print("sim")
else:
    # exibir mensagem
    print("não")