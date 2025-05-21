# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
# Dica: lembre-se que o fatorial de 0 vale 1!

# solicitar ao usuário um valor numérico
n = int(input("Digite o valor numérico: "))

# iniciar a variável fat com o valor 1
fat = 1

# iniciar a variável i com o valor 1
i = 1

# enquanto i for menor ou igual a n
while i <= n:
    fat = fat * i
    i = i + 1

# exibir o resultado
print(fat)