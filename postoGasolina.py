pGasolina = 5.80
pEtanol = 4.90
preco = 0

combustivel = input("Qual o tipo de combustivel foi adicionada ao automovel?\n G - Gasolina \n E - Etanol \n").upper()
litros = float(input("Quantos litros foi adicionado ao automovel? "))

if combustivel == 'G':
    preco = pGasolina * litros
    print("Valor a ser pago", preco)
elif combustivel == 'E':
    preco = pEtanol * litros
    print("Valor a ser pago", preco)
else:
    print("Erro")
