# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética.

# solicitar ao usuário os valores das notas 1, 2, 3 e 4
nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# calcular a média aritmética das notas
media = (nota1 + nota2 + nota3 +  nota4) / 4

# exibir o resultado
print(f'A média aritmética é {media :.1f}')