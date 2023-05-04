cont = 0
numeros = 0
vetorImpar = []

while True:
    if numeros % 2 == 1:
        vetorImpar.append(numeros)
        cont += 1
    if cont == 10:
        break
    numeros += 1

print(vetorImpar)
