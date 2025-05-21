# Receba um número inteiro na entrada e imprima 'Buzz' se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

# solicitar ao usuário um valor numérico
n = int(input("Digite um valor numérico: "))

# verificar se é múltiplo de 5
if n % 5 == 0:
    # exibir mensagem
    print("Buzz")
else:
    # exibir o valor se não for múltiplo
    print(n)