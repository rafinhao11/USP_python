# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
# O programa deve imprimir, usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
# digite a largura: 10
# digite a altura: 3
##########
##########
##########

# solicitar ao usuários os valores das variáveis 'altura' e 'largura'
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

# definir valor 1 para a variável 'i'
i = 1

# enquanto 'i' é menor ou igual a altura:
while i <= altura:
    # definir valor 1 para a variável 'j'
    j = 1
    # enquanto 'j' é menor ou igual a largura
    while j <= largura:
        # exibir mensagem
        print("#", end = "")
        # incrementar a variável 'j'
        j += 1
    # exibir mensagem
    print()
    # incrementar a variável 'i'
    i += 1

