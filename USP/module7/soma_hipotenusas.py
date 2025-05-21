# Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. 
# Em outras palavras, h, é uma hipotenusa se existem números inteiros i e j tais que: h^2 = i^2 + jˆ2

# Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 
# e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

# Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. 
# Uma boa solução para este exercício é fazer um laço de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. 
# Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

# Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

# criar uma função para verificar o valor da hipotenusa

# construir função eh_hipotenusa()
def eh_hipotenusa(h):
    # definir valor 1 a variável 'i'
    i = 1
    # enquanto 'i' for menor que 'h'
    while i < h:
        # definir valor 1 a variável 'j'
        j = i
        # enquanto 'j' for menor que 'h'
        while j < h:
            # verificar se a fórmula da hipotenusa é verdadeira
            if i ** 2 + j ** 2 == h ** 2:
                # retornar valor True
                return True
            # incrementar a variável 'j'
            j += 1
        # incrementar a variável 'i'
        i += 1
    # retornar valor False
    return False

def soma_hipotenusas(n):
    # definir o valor 0 para a variável 'soma'
    soma = 0
    # definir valor 1 para a variável 'h'
    h = 1
    # enquanto 'h' é menor ou igual a 'n'
    while h <= n:
        # definir variável que hipotenusa que verifica se a 'h' é hipotenusa
        hipotenusa = eh_hipotenusa(h)
        # verificar se a variável 'hipotenusa' é verdadeira
        if hipotenusa:
            # incrementa a variável 'soma' com valor 'h'
            soma += h
        # incrementa a variável 'h'
        h += 1
    # retornar a variável 'soma'
    return soma

# solicitar ao usuário a valor da variável 'n'
n = int(input('digite um valor numérico: '))
# exibir resultado da função soma_hipotenusas(n)
print(soma_hipotenusas(n))