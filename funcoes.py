def somar(numb1, numb2):
    print(numb1 + numb2)


def subtrair(numb1, numb2):
    print(numb1 - numb2)


def multiplicacao(numb1, numb2):
    print(numb1 * numb2)


def divisao(numb1, numb2):
    print(numb1 / numb2)


def elemento(numero):
    if numero > 0:
        return 'P'
    elif numero == 0:
        return 'Z'
    else:
        return 'N'


lista_Produto = []
lista_Valor = []


def lista_ADD(produto, valor):
    lista_Produto.append(produto)
    lista_Valor.append(valor)


def somas(*numeros):
    total = 0
    for x in numeros:
        total += x
    return total


def tamTexto(texto):
    cont = 0
    for x in texto:
        if x != ' ':
            cont += 1
    print(cont)
    print(len(texto.replace(" ", "")))
    print(texto[::-1])


def novalista(numerosrepetidos):
    vetorB = []
    for x in numerosrepetidos:
        if x not in vetorB:
            vetorB.append(x)
    print(vetorB)


def newlist(numerosrepetidos):
    print(list(set(numerosrepetidos)))


def primo(number):
    contador = 0
    for x in range(2, number, +1):
        if number % x == 0:
            contador += 1
    if contador == 0:
        print("Primo")
    else:
        print("Não é primo")
