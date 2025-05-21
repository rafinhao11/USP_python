# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro
# e devolve o maior número primo menor ou igual ao número passado à função

# construir função que verifica se o valor de entrada é primo
def ehPrimo(n):
    # iniciar a variável booleana como verdadeira
    ehPrimo = True

    # iniciar a variável divisor com o valor 2
    divisor = 2

    # verificar se n é menor que 2
    if n < 2:
        ehPrimo = False
    else:
        # enquanto divisor é menor ou igual a n elevado a 0.5
        while divisor <= (n ** 0.5):
            # verificar se n é múltiplo de divisor
            if n % divisor == 0:
                ehPrimo = False
            divisor = divisor + 1
        return ehPrimo

# construir uma função que retorna o menor número primo ao valor passado
def maior_primo(n):
    # enquanto a função é não é verdadeira
    while not ehPrimo(n):
        n = n - 1
    return n

# solicitar ao usuário um valor numérico
n = int(input("Digite um valor numérico: "))

# exibir o resultado 
print(maior_primo(n))