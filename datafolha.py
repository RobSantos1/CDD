eleitores = int(input("Quantidade de Eleitores: "))
votos_nulos = int(input("Quantidade de votos nulos: "))
votos_brancos = int(input("Quantidade de votos brancos: "))
votos_validos = int(input("Quantidade de votos validos: "))

percentual_nulos = (votos_nulos / eleitores) * 100
percentual_brancos = (votos_brancos / eleitores) * 100
percentual_validos = (votos_validos / eleitores) * 100

print(f"{percentual_validos}% de votos válidos")
print(f"{percentual_brancos}% de votos brancos")
print(f"{percentual_nulos}% de votos nulos")
