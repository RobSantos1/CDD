num = 0
while num != 6:
    number1 = float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o segundo número: "))

    num = input("Escolha uma das opções:\n1. Para Soma"
                "\n2.Para Subtração\n3.Multiplicação"
                "\n4.Divisão\n5.Digitar novo numero\n6.Sair\n")

    if num == '1':

        print(number1 + number2)
    elif num == '2':
        print(number1 - number2)

    elif num == '3':
        print(number1 * number2)

    elif num == '4':
        print(number1 / number2)

    elif num == '5':
        continue

    elif num == '6':
        break
    else:
        continue
