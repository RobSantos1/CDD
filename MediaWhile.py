repeat = 0
soma = 0
while repeat < 10:
    num = int(input("Digite um numero:"))
    soma += num
    repeat += 1

media = soma / repeat
print("Media dos numeros: ", media)

