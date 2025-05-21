# Receba um número inteiro na entrada e imprima 'FizzBuzz' na saída se o número for divisível por 3 e por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

# solicitar ao usuário um valor numérico
n = int(input("Digite um valor numérico: "))

# verificar se é múltiplo de 3 e 5
if (n % 3 == 0) and (n % 5 == 0):
    # exibir mensagem
    print("Fizzbuzz")
else:
    # exibir o valor se não for múltiplo
    print(n)