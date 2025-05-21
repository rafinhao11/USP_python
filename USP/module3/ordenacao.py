# Receba 3 números inteiros na entrada e imprima 'crescente' se eles forem dados em ordem crescente.
# Caso contrário, imprima 'não está em ordem crescente'

# solicitar ao usuário a entrada de três valores numéricos
num_one = int(input("Digite um valor numérico: "))
num_two = int(input("Digite um valor numérico: "))
num_three = int(input("Digite um valor numérico: "))

# verificar se menores um que o outro
if (num_one < num_two) and (num_one < num_three):
    # verificar se é menor que outro
    if(num_two < num_three):
        # exibir mensagem
        print("crescente")
    else:
        # exibir mensagem
        print("não está em ordem crescente")
else:
    # exibir mensagem
    print("não está em ordem crescente")