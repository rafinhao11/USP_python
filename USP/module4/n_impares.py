# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

# solicitar ao usuário um valor numérico
n = int(input("Digite um valor numérico: "))

# iniciar a variável count com o valor 1
count = 1

# iniciar a variável num_total com o valor 1
num_total = 1

# enquanto cont for menor ou igual a n
while count <= n:
    # verificar se num_total não é múltiplo de 2
    if num_total % 2 == 1:
        # exibir o resultado
        print(num_total)
        count = count + 1
    num_total = num_total + 1