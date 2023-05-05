numeros = []
pares = ""
impares = ""
positivo = ""
negativo = ""
zeros = ""
for x in range(10):
    numeros.append(int(input("")))

for y in range(10):
    if numeros[y] % 2 == 0:
        pares += f"[{y}] - {numeros[y]} é par\n"
    if numeros[y] % 2 != 0:
        impares += f"[{y}] - {numeros[y]} é impar\n"
    if numeros[y] > 0:
        positivo += f"[{y}] - {numeros[y]} é positivo\n"
    if numeros[y] < 0:
        negativo += f"[{y}] - {numeros[y]} é negativo\n"
    else:
        zeros += f"[{y}] - {numeros[y]} é zero!\n"

print("============================================================================\n")
print(pares)
print("============================================================================\n")
print(impares)
print("============================================================================\n")
print(positivo)
print("============================================================================\n")
print(negativo)
print("============================================================================\n")
print(zeros)
print("============================================================================\n")
