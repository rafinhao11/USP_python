# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro 
# e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).


# construir função n_primos()
def n_primos(n):
    # definir variável 'contador'
    contador = 0
    # definir valor 2 para a variável 'numero'
    numero = 2

    # enquanto 'numero' é menor ou igual a 'n'
    while numero <= n:
        # definir o valor 2 a variável 'divisor'
        divisor = 2
        # definir o valor True a variável 'ehPrimo'
        ehPrimo = True
        # enquanto 'divisor' é menor ou igual a 'numero' ^ 0.5
        while divisor <= numero ** 0.5:
            # verificar se é 'numero' é múltiplo de 'divisor'
            if numero % divisor == 0:
                # definir valor False se a condição for verdadeira
                ehPrimo = False
            # incrementar a variável 'divisor'
            divisor += 1
        
        # verificar se a variável 'ehPrimo' é True
        if ehPrimo:
            contador += 1

        # incrementar a variável 'numero'
        numero += 1
    # retornar o valor da variável 'contador'' 
    return contador

# solicitar ao usuário um valor numérico
n = int(input('digite valor numérico: '))
# exibir resultado da função
print(n_primos(n))