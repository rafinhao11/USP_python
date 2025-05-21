# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

# construir a função para verificar qual é o maior entre eles
def maior_valor(x, y):
    # verificar se 'x' é maior que 'y'
    if x > y:
        return x
    else:
        return y

# solicitar ao usuário os valores de 'x' e 'y'
x = int(input("Digite um valor numérico: "))
y = int(input("Digite um valor numérico: "))

# exibir o resultado
print(maior_valor(x, y))