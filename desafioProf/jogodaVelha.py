matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def interface():
    for x in range(3):
        for y in range(3):
            if matriz[x][y] == 0:
                print("_", end=" ")
            elif matriz[x][y] == 1:
                print("X", end=" ")
            elif matriz[x][y] == -1:
                print("O", end=" ")
        print()


jogador1 = input("Qual seu nome? ")
print(f"Bem vindo {jogador1}! Seu marcador é o X")
jogador2 = input("Qual seu nome? ")
print(f"Bem vindo {jogador2}! Seu marcador é o O")
jogada = 1

while jogada <= 9:

    if jogada % 2 == 1:
        selectlinha = int(input(f"{jogador1}, qual linha você deseja jogar ? "))
        selectcoluna = int(input("Qual a coluna você deseja jogar? "))
        for linhaX in range(3):
            if selectlinha - 1 == linhaX:
                for colunaX in range(3):
                    if selectcoluna - 1 == colunaX:
                        if matriz[linhaX][colunaX] == 0:
                            matriz[linhaX].pop()
                            matriz[linhaX].insert(colunaX, 1)
                            jogada += 1
                        else:
                            print("Tente dnv!")
        interface()

    if jogada % 2 == 0:
        selectlinha = int(input(f"{jogador2}, qual linha você deseja jogar ? "))
        selectcoluna = int(input("Qual a coluna você deseja jogar? "))

        for linhaO in range(3):
            if selectlinha - 1 == linhaO:
                for colunaO in range(3):
                    if selectcoluna - 1 == colunaO:
                        if matriz[linhaO][colunaO] == 0:
                            matriz[linhaO].pop(colunaO)
                            matriz[linhaO].insert(colunaO, -1)
                            jogada += 1
                        else:
                            print("Tente dnv!")
        interface()
