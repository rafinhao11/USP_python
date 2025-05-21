# Jogo do NIM:
# Dois jogadores retiram alternadamente entre 1 e m peças de um total inicial n.
# Ganha quem tirar a última peça da mesa.

# Estratégia vencedora:
# A ideia é deixar sempre um número de peças que seja múltiplo de (m+1) para o oponente.
# Isso garante ao jogador que seguir a estratégia a vitória, se ele começar na hora certa.

# Objetivo:
# Escrever um programa em Python 3 onde um jogador humano joga contra o computador.
# O computador deve sempre seguir a estratégia vencedora descrita acima.

# Definições do jogo:
# n = número inicial de peças
# m = número máximo de peças que se pode retirar por jogada

# Regra para decidir quem começa:
# - Se n é múltiplo de (m+1), o jogador começa: "Você começa!"
# - Caso contrário, o computador começa: "Computador começa!"

# Estratégia do computador:
# Em sua jogada, o computador sempre tenta deixar um número de peças que seja
# múltiplo de (m+1). Se isso não for possível, ele retira o máximo permitido.

# Funções a serem implementadas:

# 1. computador_escolhe_jogada(n, m):
#    - Recebe o número atual de peças (n) e o limite de jogada (m)
#    - Retorna quantas peças o computador deve tirar (estratégia vencedora)

# 2. usuario_escolhe_jogada(n, m):
#    - Solicita a jogada do usuário
#    - Valida a entrada: deve ser entre 1 e m e menor ou igual a n
#    - Repetir a pergunta até receber um valor válido

# 3. partida():
#    - Pede os valores de n e m
#    - Decide quem começa com base na regra de múltiplo de (m+1)
#    - Alterna jogadas entre o computador e o usuário
#    - Exibe após cada jogada: peças removidas e quantas restam
#    - Exibe no final: quem ganhou ("O computador ganhou!" ou "Você ganhou!")

# Observação:
# O programa deve manter o estado do jogo (quantas peças restam)
# e o limite de peças por jogada (m) durante toda a partida.

# Atenção para input() fora de funções:
# Não usar input() diretamente no corpo do programa.
# Todas as entradas devem estar dentro de funções (por exemplo, dentro de partida()).

# Extra - Campeonatos:

# Depois de implementar uma partida, criar a função campeonato():
# - Realiza 3 partidas seguidas entre jogador e computador
# - Mostra mensagens de início e fim de cada rodada
# - Exibe o placar final como: "Placar: Você X Computador"

# Execução principal:

# O programa deve começar perguntando:
# "Bem-vindo ao jogo do NIM! Escolha:
# 1 - para jogar uma partida isolada
# 2 - para jogar um campeonato"

# A resposta determina se será chamada a função partida() ou campeonato().

# Exemplo de mensagens a serem exibidas (exigidas pelo corretor automático):
# "Você começa!"
# "Computador começa!"
# "O computador tirou uma peça."
# "Agora restam X peças no tabuleiro."
# "Você tirou X peças."
# "Fim do jogo! O computador ganhou!"
# "Fim do jogo! Você ganhou!"
# "**** Rodada X ****"
# "**** Final do campeonato! ****"
# "Placar: Você N X M Computador"


# 1. computador_escolhe_jogada(n, m):
#    - Recebe o número atual de peças (n) e o limite de jogada (m)
#    - Retorna quantas peças o computador deve tirar (estratégia vencedora)
def computador_escolhe_jogada(n, m):


# 2. usuario_escolhe_jogada(n, m):
#    - Solicita a jogada do usuário
#    - Valida a entrada: deve ser entre 1 e m e menor ou igual a n
#    - Repetir a pergunta até receber um valor válido
def usuario_escolhe_jogada(n, m):


# 3. partida():
#    - Pede os valores de n e m
#    - Decide quem começa com base na regra de múltiplo de (m+1)
#    - Alterna jogadas entre o computador e o usuário
#    - Exibe após cada jogada: peças removidas e quantas restam
#    - Exibe no final: quem ganhou ("O computador ganhou!" ou "Você ganhou!")
def partida():

# Extra - Campeonatos:

# Depois de implementar uma partida, criar a função campeonato():
# - Realiza 3 partidas seguidas entre jogador e computador
# - Mostra mensagens de início e fim de cada rodada
# - Exibe o placar final como: "Placar: Você X Computador"
def campeonato():

# Execução principal:

# O programa deve começar perguntando:
# "Bem-vindo ao jogo do NIM! Escolha:
# 1 - para jogar uma partida isolada
# 2 - para jogar um campeonato"
def main():


# chamar função
main()