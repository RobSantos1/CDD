numero = int(input("Qual numero voce quer repetir: "))

for x in range(1, numero+1):
    print(x)
    for y in range(1, x):
        print(x)
