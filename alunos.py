qtdeAlunos = int(input("Quantos Alunos tem na sala ? "))
alunos = []

for x in range(qtdeAlunos):
    nomeAlunos = input("Nome do Aluno: ")
    alunos.append(nomeAlunos)

for i in range(qtdeAlunos):
    print(i, "-", end=" ")
    print(alunos[i])

