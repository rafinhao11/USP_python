# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:
# Entrada: Digite um número inteiro: 78615
# Saída: O dígito das dezenas é 1
# Dica: O operador // faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor.
# O operador % devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

# solicitar ao usuário um valor numérico
valor = int(input("Digite o valor numérico: "))

# 
dezenas = ((valor // 10) % 10)

# exibir o resultado
print(f'O dígito das dezenas é {dezenas}')