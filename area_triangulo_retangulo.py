
while True:
    menu = int(input(""" Calculo da area das formas geometricas
    Qual forma você escolhe?
    1 - Triangulo
    2 - Retangulo
    3 - Encerrar
=> """))
    if menu == 1:
        base = float(input("\nQual o valor da base do triangulo? "))
        altura = float(input("Qual o valor da altura do triangulo? "))

        area_triangulo = (base * altura) / 2
        print(f"\nA area do triangulo é: {area_triangulo}\n")

    elif menu == 2:
        base = float(input("\nQual o valor da base do retangulo? "))
        altura = float(input("Qual o valor da altura do retangulo? "))

        area_retangulo = base * altura
        print(f"\nA area do retangulo é: {area_retangulo}\n")

    elif menu == 3:
        break

    else:
        print("Opção Invalida!")
