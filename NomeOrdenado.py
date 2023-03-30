numero1 = float(input("Primeiro numero: "))
numero2 = float(input("Segundo numero: "))

if numero1 != numero2:
    if numero1 < numero2:
        print(numero1, "/", numero2)
    else:
        print(numero2, "/", numero1)
else:
    print("Numeros iguais!")

