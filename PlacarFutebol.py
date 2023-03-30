
time1 = input("Time da Casa: ")
time2 = input("Time Visitante: ")
qtdeGolCasa = input("Quantos gols o time da casa fez? ")
qtdeGolVisitante = input("Quantos gols o time visitante fez? ")

if qtdeGolCasa != qtdeGolVisitante:
    if qtdeGolCasa > qtdeGolVisitante:
        print("Time Vencedor:", time1)
    else:
        print("Time Vencedor", time2)
else:
    print("EMPATE!")
