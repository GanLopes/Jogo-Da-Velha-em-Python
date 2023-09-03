import random

 

tabuleiro = [

    [" ", " ", " "],

    [" ", " ", " "],

    [" ", " ", " "]

]

 

def inicializarTabuleiro():

  tab = [

    [" ", " ", " "],

    [" ", " ", " "],

    [" ", " ", " "]

]

  return tab

 

def imprimeMenuPrincipal():

    print('''

===============COMO DESEJA JOGAR?===============

(1) JOGADOR X JOGADOR

(2) JOGADOR X MÁQUINA

(3) Sair

===============================================

''')

    escolha = int(input("Escolha: "))

    return escolha

 

# Escolher o simbolo que deseja jogar

 

def escolha_simbolo():

    print('''

(1) pra X

(2) pra O

''')

    escolha_simbolo = int(input("Escolha: "))

    return escolha_simbolo

# Verificar linhas, colunas e diagonais

 

def verificar_vitoria(tabuleiro, jogador):

 

    for i in range(3):

        # Verificar se todas as posições na linha atual são iguais ao jogador

        if all(pos == jogador for pos in tabuleiro[i]):

            return True  # Jogador ganhou em uma linha

 

        # Verificar se todas as posições na coluna atual são iguais ao jogador

        if all(pos == jogador for pos in [tabuleiro[0][i], tabuleiro[1][i], tabuleiro[2][i]]):

            return True  # Jogador ganhou em uma coluna

 

    # Verificar diagonais

    if all(tabuleiro[i][i] == jogador for i in range(3)):

        return True  # Jogador ganhou na diagonal principal

 

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):

        return True  # Jogador ganhou na diagonal secundária

    return False  # Nenhum padrão de vitória foi encontrado

 

def atualizar_pontuacao(pontuacao, jogador):

    pontuacao[jogador] += 1

 

# Verificar caso de empate

def verificaVelha(tabuleiro):

    for linha in tabuleiro:

        if ' ' in linha:

            return False  # Ainda há espaços vazios, o jogo não encerrou em velha

    return True

 

def imprimir_pontuacao(pontuacao):

    print(f"Pontuação - Jogador X: {pontuacao['X']} | Jogador O: {pontuacao['O']}")

 

def imprimirTabuleiro(tabuleiro):

    print("    1   2   3")

    print("1:", tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])

    print("   " + "-" * 11)

    print("2:", tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])

    print("   " + "-" * 11)

    print("3:", tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])

 

def leiaCoordenadasLinha():

    linha = int(input("Qual linha deseja jogar? "))

    return linha

 

def leiaCoordenadasColuna():

    coluna = int(input("Qual coluna deseja jogar? "))

    return coluna

 

def jogar(linha, coluna, jogador):

    global tabuleiro

    if tabuleiro[linha - 1][coluna - 1] == " ":

        tabuleiro[linha - 1][coluna - 1] = jogador

    else:

        print("Posição já ocupada. Tente novamente.")

 

def escolhaDificuldade():

    print('''

===============EM QUAL DIFICULDADE DESEJA JOGAR?===============

(1) Facil

(2) Dificil

===============================================

''')

    escolha_dificuldade = int(input("Escolha: "))

    return escolha_dificuldade

 

def modoDificil():

    print("Em desenvolvimeto...")

 

# Ler coordenada da maquina atraves do random

def jogadaMaquinaFacil():

  while True:

    linha = random.randint(0, 2)

    coluna = random.randint(0, 2)

    if tabuleiro[linha][coluna] == " ":

      return linha, coluna

 

def modoJogador():

 

    num_partidas = 3

 

    pontuacao = {'X': 0, 'O': 0}

 

    while pontuacao['X'] < 2 and pontuacao['O'] < 2:  

      print("JOGADOR X JOGADOR")

      imprimir_pontuacao(pontuacao)

 

      jogador_x = "X" if escolha_simbolo() == 1 else "O"

 

      jogador_o = "O" if jogador_x == "X" else "X"

 

      for _ in range(9):  # Número máximo de jogadas

 

        imprimirTabuleiro(tabuleiro)

 

        print(f"Jogador {jogador_x} é sua vez:")

 

        while True:

          linha = leiaCoordenadasLinha()

          coluna = leiaCoordenadasColuna()

 

          if 1 <= linha <= 3 and 1 <= coluna <= 3:

 

            if tabuleiro[linha - 1][coluna - 1] == " ":

              jogar(linha, coluna, jogador_x)

              break

            else:

              print("Posição já ocupada. Tente novamente.")

          else:

            print("Coordenadas inválidas. Tente novamente.")

        if verificar_vitoria(tabuleiro, jogador_x):

          print(f"Jogador {jogador_x} venceu!")

          atualizar_pontuacao(pontuacao, jogador_x)

          break

 

        imprimirTabuleiro(tabuleiro)

        print(f"Jogador {jogador_o} é sua vez:")

 

        while True:

          linha = leiaCoordenadasLinha()

          coluna = leiaCoordenadasColuna()

          if 1 <= linha <= 3 and 1 <= coluna <= 3:

            if tabuleiro[linha - 1][coluna - 1] == " ":

              jogar(linha, coluna, jogador_o)

              break

            else:

                print("Posição já ocupada. Tente novamente.")

          else:

            print("Coordenadas inválidas. Tente novamente.")

 

        if verificar_vitoria(tabuleiro, jogador_o):

          print(f"Jogador {jogador_o} venceu!")

          atualizar_pontuacao(pontuacao, jogador_o)

          break

      print(f"Partida encerrada! Pontuação atual:")

      imprimir_pontuacao(pontuacao)

    vencedor = max(pontuacao, key=pontuacao.get)

    print(f"Melhor de 3 encerrado! O jogador {vencedor} venceu!")

    imprimir_pontuacao(pontuacao)

def exibir():
    escolha_menu = 0

    while escolha_menu != 3:
        escolha_menu = imprimeMenuPrincipal()

        if escolha_menu == 1:
            modoJogador()

        elif escolha_menu == 2:
            escolha_dificuldade = escolhaDificuldade()

            if escolha_dificuldade == 1:
                pontuacao = modoFacil()
                imprimir_pontuacao(pontuacao)
            elif escolha_dificuldade == 2:
                modoDificil()
            else:
                print("Escolha Inválida. Tente novamente")

        elif escolha_menu == 3:
            print("Programa finalizado. Volte sempre!")
            break

        else:
            print("Escolha Inválida. Tente novamente")

def modoFacil():
    jogador = "X" if escolha_simbolo() == 1 else "O"
    pontuacao = {'X': 0, 'O': 0}  # Inicializar a pontuação antes das partidas

    while True:
        imprimirTabuleiro(tabuleiro)
        print(f"Jogador {jogador} é sua vez:")

        if jogador == "X":
            linha = leiaCoordenadasLinha()
            coluna = leiaCoordenadasColuna()

            if 1 <= linha <= 3 and 1 <= coluna <= 3:
                if tabuleiro[linha - 1][coluna - 1] == " ":
                    jogar(linha, coluna, jogador)
                else:
                    print("Posição já ocupada. Tente novamente.")
            else:
                print("Coordenadas inválidas. Tente novamente.")
        else:
            linha, coluna = jogadaMaquinaFacil()
            if tabuleiro[linha][coluna] == " ":
                jogar(linha, coluna, jogador)
            else:
                continue

        if verificar_vitoria(tabuleiro, jogador):
            imprimirTabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            atualizar_pontuacao(pontuacao, jogador)
            break
        elif verificaVelha(tabuleiro):
            imprimirTabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador = "X" if jogador == "O" else "O"

    return pontuacao

def modoJogadorXMaquina():
    pontuacao = {'Jogador': 0, 'Máquina': 0}
    
    while pontuacao['Jogador'] < 2 and pontuacao['Máquina'] < 2:
        print("JOGADOR X MÁQUINA")
        imprimir_pontuacao(pontuacao)

        jogador = escolha_simbolo()
        maquina = 'X' if jogador == 2 else 'O'

        for _ in range(9):
            imprimirTabuleiro(tabuleiro)

            if jogador == 1:
                linha = leiaCoordenadasLinha()
                coluna = leiaCoordenadasColuna()
            else:
                linha, coluna = jogadaMaquinaFacil()

            if 1 <= linha <= 3 and 1 <= coluna <= 3:
                if tabuleiro[linha - 1][coluna - 1] == " ":
                    jogar(linha, coluna, 'X' if jogador == 1 else 'O')
                else:
                    print("Posição já ocupada. Tente novamente.")
            else:
                print("Coordenadas inválidas. Tente novamente.")

            if verificar_vitoria(tabuleiro, 'X' if jogador == 1 else 'O'):
                imprimirTabuleiro(tabuleiro)
                vencedor = 'Jogador' if jogador == 1 else 'Máquina'
                print(f"{vencedor} venceu!")
                pontuacao[vencedor] += 1
                break
            elif verificaVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador = 1 if jogador == 2 else 2

        imprimir_pontuacao(pontuacao)

    vencedor = max(pontuacao, key=pontuacao.get)
    print(f"Melhor de 3 encerrado! O {vencedor} venceu!")

exibir()