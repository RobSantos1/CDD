dividendo = int(input("Primeiro numero: "))
divisor = int(input("Segundo numero: "))

while (divisor == 0):
    print("Digite um numero diferente de 0!")
    divisor = int(input("Segundo numero: "))
print("O Resultado da Divisão é: ", dividendo / divisor)
