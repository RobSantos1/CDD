qtde_maca = int(input("Quantas maçãs voce deseja comprar? "))

preco_promo = qtde_maca * 1.00
preco = qtde_maca * 1.30

if qtde_maca < 12:
    print(f"Total a pagar R${preco:.2f}")
    if 12 * 1 < preco:
        falta = 12 - qtde_maca
        desconto = preco - 12
        print(f"Faltam mais {falta} maçãs para você ter um desconto de R${desconto:.2f} no seu pedido")

else:
    print(f"Total a pagar R${preco_promo:.2f}")