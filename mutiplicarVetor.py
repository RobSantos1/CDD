
vetorA = []
vetorM = []
for i in range(0, 10):
    vetorA.append(int(input("numeros do Vetor A: ")))

valorX = int(input("Numero para multiplicar:"))

for y in range(0, 10):
    vetorM.append(valorX * vetorA[y])

    print(vetorM[y], end=' ')
