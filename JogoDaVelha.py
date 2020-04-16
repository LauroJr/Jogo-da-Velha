import os

print(12*'-=')
print("CADASTRE OS JOGADORES: ")
print(12*'-=')

jogador1 = str(input("Player 1: "))
jogador2 = str(input("Player 2: "))
print()
player1 = str(input(f"{jogador1}, escolha entre [O] ou [X] p/ jogar: "))
print()
if player1 == 'O':
    player2 = 'X'
    print(f'{jogador1}, você joga: {player1}\n{jogador2}, você joga:\
 {player2}')
    print()
    iniciar = input("Tecle enter para iniciar o jogo")
else:
    player2 = 'O'
    print(f'{jogador1}, você joga: {player1}\n{jogador2}, você joga:\
 {player2}')
    print()
    iniciar = input("Tecle enter para iniciar o jogo: ")

os.system("cls")
rodada = 3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
t = 1
bol = True
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = t
        t += 1
cont = 0

while cont < 9 and bol is True:
    venc = False
    if rodada % 2 == 1:
        play = player1
        vencedor = jogador1
    else:
        play = player2
        vencedor = jogador2
    print(15*'-=')
    print("ESCOLHA UM NÚMERO P/ JOGAR: ")
    print(15*'-=')
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[ {matriz[l][c]} ]', end=' ')
        print()
    print()
    jogo = int(input())

    if jogo == 1:
        if lista[0] == 1:
            os.system("cls")
            matriz[0][0] = play
            lista[0] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 2:
        if lista[1] == 2:
            os.system("cls")
            matriz[0][1] = play
            lista[1] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 3:
        if lista[2] == 3:
            os.system("cls")
            matriz[0][2] = play
            lista[2] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 4:
        if lista[3] == 4:
            os.system("cls")
            matriz[1][0] = play
            lista[3] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 5:
        if lista[4] == 5:
            os.system("cls")
            matriz[1][1] = play
            lista[4] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 6:
        if lista[5] == 6:
            os.system("cls")
            matriz[1][2] = play
            lista[5] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 7:
        if lista[6] == 7:
            os.system("cls")
            matriz[2][0] = play
            lista[6] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 8:
        if lista[7] == 8:
            os.system("cls")
            matriz[2][1] = play
            lista[7] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    elif jogo == 9:
        if lista[8] == 9:
            os.system("cls")
            matriz[2][2] = play
            lista[8] = 'f'
        else:
            os.system("cls")
            print("Este campo já possui um valor. Tente outro")
            jogo = 50

    if jogo != 50:
        rodada += 1

    if matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[0][2] == matriz[1][1] and matriz[0][2] == matriz[2][0]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[0][1] == matriz[1][1] and matriz[0][1] == matriz[2][1]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    elif matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2]:
        print(f"Parabéns {vencedor}, você acaba de vencer esta rodada!!!")
        bol = False
        venc = True
    else:
        cont += 1
      # if cont == 8:
      #    bol = False    para usar esta condição, troque o conectivo and por or

if venc is False:
    print("Rodada sem vencedor...")
