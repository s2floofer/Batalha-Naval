#https://youtu.be/MroxRS0II2o?si=e1Mt99MTDdah8EgN
import random

#tabuleiro em forma de matriz do jogo
tabuleiroJogadorMatriz = [["🌊"for i in range(10)] for i in range(5)]
tabuleiroComputadorMatriz = [["🌊" for i in range(10)] for i in range(5)]
jogadasFeitasComp = []

#função de imprimir as boas vindas ao jogo e pedindo nome do jogador para poder interagir mais adiante
def imprimeBoasVindas():
    print("\033[1;37m\nSEJA BEM VINDO(A) À BATALHA NAVAL\n\033[0m")
    print("         |    |    |")
    print("         )_)  )_)  )_)")
    print("         )___))___))___)\\")
    print("        )____)____)_____)\\\\")
    print("     _____|____|____|____\\\\\\__")
    print("-------\\                /---------")
    print("      ^^^^^ ^^^^^^^^^^^^^^^^^^^^^")
    print("         ^^^^      ^^^^     ^^^    ^^")
    print("             ^^^^      ^^^")
    nomeJogador = input("\nQual é seu nome? ").upper()
    return nomeJogador

#mostrando o tabuleiro do computador com sua coluna e linhas numeradas para melhor entendimento
def tabuleiroComputador(embarcacoesComp):
    print("\033[1;37m\nTABULEIRO DO COMPUTADOR\n\033[0m")
    #numero das colunas
    print(" ", end=" ")
    for col in range(10):
        print(f"{col} ", end=" ")
    print()
    for i, linha in enumerate(tabuleiroComputadorMatriz):
        #numero da linha
        print(f"{i } ", end="")
        for elemento in linha:
            if elemento == "🚢":
                print("🌊", end = " ")
            else:
                print(elemento, end=" ")
        print()
    print(f"\nEMBARCAÇÕES RESTANTES: {embarcacoesComp}\n")

#função de separar os tabuleiros para ficar mais organizado na jogatina
def separarTabuleiros():
    print("-------------------------------------------")

#função do tabuleiro do jogador interagindo com o nome
def tabuleiroJogador(embarcacoesJogador, nomeJogador, mostrarNavios=False):
    print(f"\033[1;37m\nTABULEIRO DE {nomeJogador}\n\033[0m")
    #numero das colunas
    print(" ", end=" ")
    for col in range(10):
        print(f"{col} ", end=" ")
    print()
    for i, linha in enumerate(tabuleiroJogadorMatriz):
        #numero da linha
        print(f"{i } ", end="")
        for elemento in linha:
            if elemento == "🚢" and not mostrarNavios:
                print("🌊", end=" ")
            else:
                print(elemento, end=" ")
        print()
    print(f"\nEMBARCAÇÕES RESTANTES: {embarcacoesJogador}\n")

#aqui é necessário pedir as coordenadas de posicionamento do jogador 
def coordenadasJogador(nomeJogador, tabuleiroJogadorMatriz):
    embarcacoesColocadas=0 
    totalEmbarcacoes = 7   
    while embarcacoesColocadas < totalEmbarcacoes:
        tabuleiroJogador(totalEmbarcacoes - embarcacoesColocadas, nomeJogador, mostrarNavios=True)
        faltam = totalEmbarcacoes - embarcacoesColocadas
        print(f"\nVocê ainda precisa posicionar {faltam} embarcação(ões).\n")
        linha = int(input(f"{nomeJogador.capitalize()}, digite a linha da sua {embarcacoesColocadas + 1}ª embarcação (de 0 a 4): "))
        coluna = int(input(f"{nomeJogador.capitalize()}, digite a coluna da sua {embarcacoesColocadas + 1}ª embarcação (de 0 a 9): "))
        print()

        if 0 <= linha <= 4 and 0 <= coluna <= 9:
            if tabuleiroJogadorMatriz[linha][coluna] == "🌊":
                tabuleiroJogadorMatriz[linha][coluna] = "🚢"
                embarcacoesColocadas += 1
            else: 
                print("Já possui uma embarcação nessa posição!\n")
        else:
            print("Atenção, essas coordenadas são inválidas!\n")

#coordenadas de posicionamento do computador randomizado 
def coordenadasComputador():
    embarcacoesColocadas=0    
    for tentativa in range(1000):
        if embarcacoesColocadas == 7:
            break 
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)

        if tabuleiroComputadorMatriz[linha][coluna] == "🌊":
            tabuleiroComputadorMatriz[linha][coluna] = "🚢"
            embarcacoesColocadas += 1

#função do ataque do computador, randomizando 
def ataqueComputador(embarcacoesJogador):
    while True:
        ataqueCompLinha = random.randint(0, 4)
        ataqueCompColuna = random.randint(0, 9)
        if (ataqueCompLinha, ataqueCompColuna) not in jogadasFeitasComp:
            jogadasFeitasComp.append((ataqueCompLinha, ataqueCompColuna))
            if  4 >= ataqueCompLinha >= 0 and 9 >= ataqueCompColuna >= 0:
                if tabuleiroJogadorMatriz[ataqueCompLinha][ataqueCompColuna] ==  "🌊":
                    tabuleiroJogadorMatriz[ataqueCompLinha][ataqueCompColuna] = "❌"
                    print(f"\033[31m\nO computador jogou as coordenadas linha: {ataqueCompLinha} e coluna: {ataqueCompColuna} e atingiu apenas água!\033[0m")
                elif tabuleiroJogadorMatriz[ataqueCompLinha][ataqueCompColuna] == "🚢":
                    tabuleiroJogadorMatriz[ataqueCompLinha][ataqueCompColuna] = "💥"
                    embarcacoesJogador -= 1
                    print(f"\033[32m\nO computador jogou as coordenadas linha: {ataqueCompLinha} e coluna: {ataqueCompColuna} e atingiu uma embarcação sua!\033[0m")
                return embarcacoesJogador

#função de ataque do jogador, informando tudo que necessário, acertou água, navio, ou se ja jogou na posição
def ataqueJogador(nomeJogador, embarcacoesComputador):
    ataqueJogadorLinha = int(input(f"{nomeJogador.capitalize()}, digite a linha da embarcação que deseja atacar (de 0 a 4): "))
    ataqueJogadorColuna = int(input(f"{nomeJogador.capitalize()},digite a coluna da embarcação que deseja atacar(de 0 a 9): "))
    mensagem = ""
    if  4 >= ataqueJogadorLinha >= 0 and 9 >= ataqueJogadorColuna >= 0:
        if tabuleiroComputadorMatriz[ataqueJogadorLinha][ataqueJogadorColuna] == "🌊":
            tabuleiroComputadorMatriz[ataqueJogadorLinha][ataqueJogadorColuna] = "❌"
            mensagem = "\033[31m\nVish, você acertou apenas água!\n\033[0m"
        elif tabuleiroComputadorMatriz[ataqueJogadorLinha][ataqueJogadorColuna] == "🚢":
            tabuleiroComputadorMatriz[ataqueJogadorLinha][ataqueJogadorColuna] = "💥"
            embarcacoesComputador -= 1
            mensagem = "\033[32m\nParabéns, você atingiu a embarcação inimiga!\n\033[0m"
        else:
            mensagem = "\033[33m\nVocê já jogou nessas coordenadas!\n\033[0m"
    else:
        mensagem = "\nAtenção, essas coordenadas são inválidas!\n"
    return embarcacoesComputador, mensagem

#função principal da batalha do jogo, fazendo estrutura de repetição com as funções do ataque d o jogador e computador
def batalha(nomeJogador, embarcacoesJogador, embarcacoesComp):
    while embarcacoesJogador > 0 and embarcacoesComp > 0:
        tabuleiroComputador(embarcacoesComp)
        separarTabuleiros()
        tabuleiroJogador(embarcacoesJogador, nomeJogador)
        embarcacoesComp, mensagem = ataqueJogador(nomeJogador, embarcacoesComp)
        print(mensagem)

        if embarcacoesComp == 0:
            tabuleiroComputador(embarcacoesComp)
            separarTabuleiros()
            tabuleiroJogador(embarcacoesJogador, nomeJogador)
            print(f"\033[1;32mParabéns {nomeJogador.capitalize()}! Você venceu! \nObrigada por jogar nosso jogo! \nDesenvolvido por Fernanda Pinho, Isabela Louise e Julia Molina\033[0m")
            break

        embarcacoesJogador = ataqueComputador(embarcacoesJogador)
        
        if embarcacoesJogador == 0:
            tabuleiroComputador(embarcacoesComp)
            separarTabuleiros()
            tabuleiroJogador(embarcacoesJogador, nomeJogador)
            print(f"\033[1;31m\nPoxa! O computador venceu \nObrigada por jogar nosso jogo! \nDesenvolvido por Fernanda Pinho, Isabela Louise e Julia Molina\n\033[1;31m")
            break

#contador das embarcações
embarcacoesComp=7
embarcacoesJogador=7

#chamando as funções para o jogo rodar
nomeJogador = imprimeBoasVindas()
tabuleiroComputador(embarcacoesComp)
separarTabuleiros()
coordenadasJogador(nomeJogador, tabuleiroJogadorMatriz)
coordenadasComputador()
batalha(nomeJogador, embarcacoesJogador, embarcacoesComp)
