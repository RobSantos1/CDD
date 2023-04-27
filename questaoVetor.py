vetorA = []
vetorPar = []

somaVetor = 0
maiorMedia = 0

for x in range(10):
    vetorA.append(int(input("Numero para guardar no vetor: ")))

menorNum = vetorA[0]
maiorNum = vetorA[0]

for y in range(10):

    if vetorA[y] % 2 == 0:
       vetorPar.append(vetorA[y])
    if vetorA[y] < menorNum:
        menorNum = vetorA[y]
    if vetorA[y] > maiorNum:
        maiorNum = vetorA[y]
    somaVetor += vetorA[y]
    media = somaVetor / 10

for z in range(10):
    if vetorA[z] > media:
        maiorMedia += 1

print("\nNumeros pares:", vetorPar,
      "\nMaior numero:", maiorNum,
      "\nMenor numero:", menorNum,
      "\nQuantos numero maiores que a media:", maiorMedia)
