import random

tabuleiro =[[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]]

# Escolher como jogar (JOGADOR X JOGADOR) (JOGADOR X MÁQUINA)
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

# Escolher o simbolo que deseja jogar ("X" OU "O")
def escolha_simbolo():
    print('''
(1) pra X
(2) pra O
''')
    escolha_simbolo = int(input("Escolha: "))
    return escolha_simbolo

# Verificar Vitoria em (linhas, colunas e diagonais)
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

# Atualizar a portuação dos jogador de acordo com cada rodada
def atualizar_pontuacao(pontuacao, jogador):
    pontuacao[jogador] += 1

# Verificar caso de empate (Velha)
def verificaVelha(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False # Ainda tem espaços vazios 
    return True #Fim de jogo (empate)

# Mostrar a portuação dos jogadores de acordo com cada rodada
def imprimir_pontuacao(pontuacao):
    print(f"Pontuação - Jogador X: {pontuacao['X']} | Jogador O: {pontuacao['O']}")

# Mostra o tabuleiro com as Coordenadas
def imprimirTabuleiro(tabuleiro):
    print("    1   2   3")
    print("1:", tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
    print("   " + "-" * 11)
    print("2:", tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
    print("   " + "-" * 11)
    print("3:", tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])

# Receber a linha em que o jogador seja posicionar o simbulo 
def leiaCoordenadasLinha():
    linha = int(input("Qual linha deseja jogar? "))
    return linha

# Receber a Coluna em que o jogador seja posicionar o simbulo 
def leiaCoordenadasColuna():
    coluna = int(input("Qual coluna deseja jogar? "))
    return coluna

# Receber as coordenadas e colocalas o simbolo no tabuleiro caso estaja vazia 
def jogar(linha, coluna, jogador):
    global tabuleiro
    if tabuleiro[linha - 1][coluna - 1] == " ":
        tabuleiro[linha - 1][coluna - 1] = jogador

# Escolher difilculdade caso o jogador escolher o modo de jogo (JOGADOR X MAQUINA)
def escolhaDificuldade():
    print('''
===============EM QUAL DIFICULDADE DESEJA JOGAR?===============
(1) Facil
(2) Dificil
===============================================
''')
    escolha_dificuldade = int(input("Escolha: "))
    return escolha_dificuldade

# 
def modoDificil():
    print("Em desenvolvimeto...")

# Ler coordenada da maquina atraves do random (Aleatoriamente)  
def jogadaMaquinaFacil():
  while True:
    linha = random.randint(0, 2)
    coluna = random.randint(0, 2)
    if tabuleiro[linha][coluna] == " ":
      return linha, coluna

def modoJogador():
    global tabuleiro
    # Mostrar Placar
    pontuacao = {'X': 0, 'O': 0}
    # Escolha simbolo
    jogador_x = "X" if escolha_simbolo() == 1 else "O"
    jogador_o = "O" if jogador_x == "X" else "X"

    # Modo escolido
    print("JOGADOR X JOGADOR")

    # Laço utilizado para limitar rodadas
    while pontuacao['X'] < 3 and pontuacao['O'] < 3:  
      # Número máximo de jogadas
      for _ in range(9): 

        imprimirTabuleiro(tabuleiro)

        print(f"Jogador {jogador_x} é sua vez:")

        # Jogadas do jogador "X"
        while True:
          linha = leiaCoordenadasLinha()
          coluna = leiaCoordenadasColuna()

          # Limite Coordenadas
          if 1 <= linha <= 3 and 1 <= coluna <= 3:
            # Verifica se a posição esta oculpada
            if tabuleiro[linha - 1][coluna - 1] == " ":
              # Adiciona no tabuleiro 
              jogar(linha, coluna, jogador_x)
              break
            else:
              print("Posição já ocupada. Tente novamente.")
          else:
            print("Coordenadas inválidas. Tente novamente.")

        if verificar_vitoria(tabuleiro, jogador_x):
          print(f"Jogador {jogador_x} venceu!")
          atualizar_pontuacao(pontuacao, jogador_x)
          tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
          break

        if verificaVelha(tabuleiro):
            print("Jogo empatou!")
            tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
            break

        imprimirTabuleiro(tabuleiro)
        print(f"Jogador {jogador_o} é sua vez:")

        # Jogadas do jogador "X"
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
          tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
          break

        if verificaVelha(tabuleiro):
            print("Jogo empatou!")
            break
            tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        
      print(f"Partida encerrada! Pontuação atual:")
      imprimir_pontuacao(pontuacao)
    # Pegar o jogador com a pontuação mais alta e atribui esse jogador à variável 
    vencedor = max(pontuacao, key=pontuacao.get)
    print(f"Melhor de 3 encerrado! O jogador {vencedor} venceu!")
    imprimir_pontuacao(pontuacao)

def modoFacil():
  jogador = "X" 
  while True:
        imprimirTabuleiro(tabuleiro)
        print(f"Jogador {jogador} é sua vez:")
        if jogador == "X":
            while True:
                linha = leiaCoordenadasLinha()
                coluna = leiaCoordenadasColuna()
                if 1 <= linha <= 3 and 1 <= coluna <= 3:
                    if tabuleiro[linha - 1][coluna - 1] == " ":
                        jogar(linha, coluna, jogador)
                        break
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
        imprimirTabuleiro(tabuleiro)
        if verificar_vitoria(tabuleiro, jogador):
            print(f"Jogador {jogador} venceu!")
            break
        elif verificaVelha(tabuleiro):
            print("Empate!")
            break
        jogador = "X" if jogador == "O" else "O"        

def exibir():
     escolha_dificuldade = 0
     escolha_menu = 0
     while escolha_menu != 3:
        escolha_menu = imprimeMenuPrincipal()
        match escolha_menu:
          case 1:
            modoJogador()
          case 2: 
              escolha_dificuldade = escolhaDificuldade()
              if escolha_dificuldade == 1:
                  modoFacil()
              elif escolha_dificuldade == 2:
                  modoDificil()
              else:
                  print("Escolha Inválida. Tente novamente")
          case 3: 
              print("Programa finalizado. Volte sempre!")
          case _:
            print("Escolha Inválida. Tente novamente")

# PRINCIPAL 
exibir()

 