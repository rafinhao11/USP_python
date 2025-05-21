# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

# construir a função para identificar as vogais do alfabeto
def vogal(letra):
    # verificar se a variável está de acordo com as condições
    if letra == 'A' or letra == "a":
        return True
    elif letra == 'E' or letra == "e":
        return True
    elif letra == 'I' or letra == "i":
        return True
    elif letra == 'O' or letra == 'o':
        return True
    elif letra == 'U' or letra == 'u':
        return True
    else:
        return False

# solicitar ao usuário a entrada de um caractere
letra = input("Digite um caractere: ")

# exibir o resultado
print(vogal(letra))