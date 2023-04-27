tamVetor = int(input("Digite o tamanho do Vetor: "))
vetorA = []
vetorB = []
vetorSoma = []

for x in range(tamVetor):
    vetorA.append(int(input("Valores do primeiro vetor: ")))
    vetorB.append(int(input("Valores do segundo vetor: ")))
    vetorSoma.append(vetorA[x] + vetorB[x])

print(vetorA)
print(vetorB)
print(vetorSoma)
