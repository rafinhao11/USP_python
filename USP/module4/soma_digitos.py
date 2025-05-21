# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
# Dica: Para separar os dígitos, lembre-se: o operador '//' faz uma divisão inteira jogando fora o resto
# ou seja, aquilo que é menor que o divisor; O operador '%' devolve apenas o resto da divisão inteira jogando fora o resultado,
# ou seja, tudo que é maior ou igual ao divisor.

# solicitar ao usuário um valor numérico
n = int(input("Digite o valor numérico: "))

# iniciar a variável com o valor 0
soma = 0

# iniciar a variável com o valor 0
divisor = 0

# enquanto n é menor que zero
while n > 0:
    divisor = n % 10
    soma = soma + divisor
    n = n // 10

# exibir o resultado
print(soma)