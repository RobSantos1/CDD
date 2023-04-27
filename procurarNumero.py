vetorA = []
contador = 0
for x in range(10):
    vetorA.append(int(input("Qual numero voce quer guardar ? ")))

num = int(input("Qual valor voce quer encontrar? "))

for y in range (10):
    if vetorA[y] == num:
        contador += 1

print("Quantas vezes o numero", num, "foi encontrado: ", contador)
