# Reescreva o programa segundos para imprimir também a quantidade de dias, ou seja,
# faça um programa em Python que, dada a quantidade de segundos, quebre esse valor em dias, horas, minutos e segundos.
# A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
# Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro
# Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:
# Entrada: Por favor, entre com o número de segundos que deseja converter: 178615
# Saída: 2 dias, 1 horas, 36 minutos e 55 segundos."

# solicitar ao usuário o valor de segundos
segundos = int(input("Digite um valor numérico: "))

# dividir o valor sem resto
dia = segundos // 86400

# capturar o resto da divisão
segundos_resto = segundos % 86400

# dividir o valor sem resto
horas = segundos_resto // 3600

# capturar o resto da divisão
segundos_resto = segundos_resto % 3600

# dividir o valor sem resto
minutos = segundos_resto // 60

# capturar o resto da divisão
segundos = segundos_resto % 60

# exibir os resultados
print(f'{dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos')