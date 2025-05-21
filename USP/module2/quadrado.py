# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado.
#calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: perímetro: x - área: y

# entrada do valor de
lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))

# cálculo do perímetro
perimetro = 4 * lado

# cálculo da área
area = lado ** 2

# exibir os resultados dos cálculos
print(f'perímetro: {perimetro} - área: {area}')