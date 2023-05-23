import random
palavras = ["biscoito", "sorvete", "doce"]

letra_digitada = []
elemento = random.choice(palavras)
chance = 5

while chance > 0:

    letra = input("Digite uma letra: ")
    letra_digitada.append(letra)

    if len(letra) > 1:
        print("Digite apenas uma letra!")
        continue

    else:
        palavra_secreta = ''
        for letra_secreta in elemento:
            if letra_secreta in letra_digitada:
                palavra_secreta += letra_secreta

            else:
                palavra_secreta += "_"

        if letra not in palavra_secreta:
            chance -= 1

        if palavra_secreta == elemento:
            print("Parabéns")
            break

        else:
            print(palavra_secreta)
