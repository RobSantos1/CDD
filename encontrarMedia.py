tam = 5
notas = []
total = 0
contador = 0
for i in range(tam):
    notaAluno = float(input("Qual a nota do Aluno? "))
    notas.append(notaAluno)
    total += notas[i]

media = total / tam

for x in range(tam):
    if notas[x] >= media:
        contador += 1

print("Média dos alunos: ", media)
print("Notas que passaram por média: ", contador)