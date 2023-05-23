import random
import time

while True:
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha_pc = random.choice(opcoes)

    escolha_user = int(input("""Qual a sua escolha? 
1 - Pedra
2 - Papel
3 - Tesoura
=>"""))

    if escolha_user == 1:
        if escolha_pc == 'Pedra':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Empate!")
        elif escolha_pc == 'Papel':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Máquina Win!")
        else:
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Você ganhou!")

    elif escolha_user == 2:
        if escolha_pc == 'Pedra':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Você ganhou!")
        elif escolha_pc == 'Papel':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Empate!")
        else:
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Máquina Win!")

    elif escolha_user == 3:
        if escolha_pc == 'Pedra':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Máquina Win!")
        elif escolha_pc == 'Papel':
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Você ganhou!")
        else:
            print("JO")
            time.sleep(1)
            print("KEN")
            time.sleep(1)
            print("PÔ!\n")
            time.sleep(1)
            print("Empate!")

    else:
        print("Digite novamente sua jogada")
        continue

    sair = input("Deseja jogar novamente? [s]/[n]")

    if sair == 'n':
        break
