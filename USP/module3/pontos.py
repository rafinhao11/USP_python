# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
# às coordenadas x e y de um ponto em um plano cartesiano.
# Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima 'longe' na saída.
# Caso o contrário, quando a distância for menor que 10, imprima 'perto'.
# Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte: d(x,y)= RAIZ((X1 - X2)^2 - (Y1 - Y2) ^2)

# importar biblioteca de cálculos matemáticos
import math

# solicitar ao usuário os valores de X1, Y1, X2 e Y2
x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

# calcular as coordenadas dos pontos cartesianos
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# verificar se a distância é maior ou igual a 10
if distance >= 10:
    # exibir mensagem
    print("perto")
else:
    # exibir mensagem
    print("longe")