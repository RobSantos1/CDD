tentativa = 0
while tentativa != 3:
    senha = input("Digite sua Senha:")
    if senha == "abc":
        print("Senha Correta!")
        break
    else:
        tentativa += 1
        if tentativa == 3:
            print("Senha Bloqueada")
