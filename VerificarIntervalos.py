countIntervalo = 0
countFora = 0
for i in range(10):
    Number = int(input("Digite qualquer numero: "))
    if Number >= 10 and Number <= 20:
        countIntervalo += 1
    else:
        countFora += 1

print("Valores entre 10 e 20:", countIntervalo)
print("Valores fora do Intervalo:", countFora)
