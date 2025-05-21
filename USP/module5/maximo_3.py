# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos,
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# construir uma função que recebe três parâmetros
def maximo(a, b, c):
    # verificar a variável a é maior ou igual a 'b' e 'c'
    if a >= b and a >= c:
        return print(a)
    # verificar a variável b é maior ou igual a 'a' e 'c'
    elif b >= a and b >= c:
        return print(b)
    else:
        return print(c)

# solicitar ao usuário os valores das variáveis de a, b e c
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

# exibir o resultado 
print(maximo(a, b, c))