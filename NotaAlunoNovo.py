repetir = 'S'
while repetir == 'S':
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    print("Média do aluno é:", media)

    repetir = input("Deseja realizar novo calculo S/N: ").upper()
