# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. "
# Se o número for primo, imprima 'primo'. Caso contrário, imprima 'não primo'."

# solicitar ao usuário o valor de 
n = int(input("Digite um valor numérico: "))

# iniciar a variável booleana como verdadeira
ehPrimo = True

# iniciar a variável com valor 2
divisor = 2

# verificar se n é menor que 2
if n < 2:
    ehPrimo = False
else:
    # verificar se n é menor ou igual a 2
    if n >= 2:
        # enquanto o divisor for menor ou igual a n elevado a 0.5
        while divisor <= n ** 0.5:
            if n % divisor == 0:
                ehPrimo = False
            divisor = divisor + 1

# verificar a variável é verdadeira
if ehPrimo:
    # exibir o resultado
    print("primo")
else:
    # exibir o resultado
    print("não primo")