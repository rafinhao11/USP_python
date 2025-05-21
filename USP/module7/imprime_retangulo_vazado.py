# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
# digite a largura: 10
# digite a altura: 3
##########
#        #
##########

# digite a largura: 2
# digite a altura: 2
##
##

# solicitar ao usuário os valores das variáveis 'altura' e 'largura''
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

# definir o valor 1 a variável 'i'
i = 1

# enquanto 'i' for menor ou igual a 'altura'
while i <= altura:
    # definir o valor 1 a variável 'j'
    j = 1
    # enquanto 'j' for menor ou igual a 'largura'
    while j <= largura:
        # verificar se 'i' é igual a 1 ou igual 'altura' e 'j' é igual a 1 ou igual a 'largura'
        if i == 1 or i == altura or j == 1 or j == largura:
            # exibir mensagem
            print("#", end = "")
        else:
            # exibir mensagem
            print(" ", end = "")
        # incrementar a variável 'j'
        j += 1
    # exibir mensagem
    print()
    # incrementar variável 'i'
    i += 1
