# Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros a, b e c e da equação ax^2 + bx + c, respectivamente, e imprimir o resultado na saída da seguinte maneira:
# 1. Quando não houver raízes reais imprima: esta equação não possui raízes reais
# 2. Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade, imprima: a raiz desta equação é X ou a raiz dupla desta equação é X
# 3. Onde X é o valor da raiz dupla, quando houver duas raízes reais imprima: as raízes da equação são X e Y, onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente.
# Exemplos: as raízes da equação são 1.0 e 2.0, as raízes da equação são -2.0 e 0.0

# importar biblioteca para cálculos matemáticos
import math

# solicitar ao usuário os valores das variáveis a, b e c
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

# calcular o valor de delta
delta = (b ** 2) - 4 * a * c

# verificar se delta é menor que zero
if delta < 0:
    print("esta equação não possui raízes reais")
# verificar se delta é igual a zero
elif  delta == 0:
    x = (- b) + math.sqrt(delta) / (2 * a)
# senão, calcular os valores de X1 e X2
else:
    x1 = (- b) + math.sqrt(delta) / (2 * a)
    x2 = (- b) - math.sqrt(delta) / (2 * a)
    # verificar qual é o maior valor e colocar em ordem crescente
    if x1 < x2:
        # exibir o resultado
        print(f'as raízes da equação são {x1} e {x2}')
    else:
        # reordernar os valores 
        x1, x2 = x2, x1
        # exibir o resultado
        print(f'as raízes da equação são {x1} e {x2}')