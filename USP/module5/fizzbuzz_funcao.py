# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# construir a função
def fizzbuzz(n):
    # verificar se é múltiplo de 3 e 5
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    # verificar se é múltiplo de 3
    elif n % 3 == 0:
        return "Fizz"
    # verificar se é múltiplo de 5
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

# Entrada do usuário
n = int(input("Digite um número inteiro: "))
print(fizzbuzz(n))