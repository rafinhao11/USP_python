# Receba um número inteiro na entrada e imprima 'par' quando o número for par ou 'ímpar' quando o número for ímpar.

# solicitar ao usuário um valor numérico
n = int(input("Digite o valor numérico: "))

# verificar se o valor é múltiplo de 2
if n % 2 == 0:
    # exibir mensagem
    print("par")
else:
    # exibir mensagem
    print("ímpar")
    