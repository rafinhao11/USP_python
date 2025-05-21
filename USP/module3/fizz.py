# Receba um número inteiro na entrada e imprima 'Fizz' se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

# solicitar ao usuário um valor numérico
n = int(input("Digite um valor numérico: "))

# verificar se é múltiplo de 3
if n % 3 == 0:
    # exibir mensagem
    print("Fizz")
else:
    # exibir o valor se não for múltiplo
    print(n)