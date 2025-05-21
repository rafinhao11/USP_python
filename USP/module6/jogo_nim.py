def computador_escolhe_jogada(n, m):
    retirada = 1
    while retirada <= m:
        if (n - retirada) % (m + 1) == 0:
            return retirada
        retirada += 1
    return min(m, n)

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_computador = True

    if n % (m + 1) == 0:
        print("\nVoce começa!\n")
        vez_computador = False
    else:
        print("\nComputador começa!\n")

    while n > 0:
        if vez_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"O computador tirou {jogada} peça{'s' if jogada > 1 else ''}.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"Você tirou {jogada} peça{'s' if jogada > 1 else ''}.")

        if n > 0:
            print(f"Agora restam {n} peça{'s' if n > 1 else ''} no tabuleiro.\n")
        else:
            print("Fim do jogo!", end=" ")
            if vez_computador:
                print("O computador ganhou!\n")
                return 1  # computador ganhou
            else:
                print("Você ganhou!\n")
                return 0  # jogador ganhou

        vez_computador = not vez_computador  # alterna turno

def campeonato():
    rodada = 1
    pontos_computador = 0
    pontos_usuario = 0

    while rodada <= 3:
        print(f"**** Rodada {rodada} ****\n")
        vencedor = partida()
        if vencedor == 1:
            pontos_computador += 1
        else:
            pontos_usuario += 1
        rodada += 1

    print("**** Final do campeonato! ****\n")
    print(f"Placar: Você {pontos_usuario} X {pontos_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = 0
    while escolha != 1 and escolha != 2:
        escolha = int(input())

    if escolha == 1:
        print("\nVoce escolheu uma partida!\n")
        partida()
    else:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()

main()