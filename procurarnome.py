qtdeAlunos = int(input("Quantos Alunos tem na sala ? "))
alunos = []

for x in range(qtdeAlunos):
    nomeAlunos = input("Nome do Aluno: ")
    alunos.append(nomeAlunos)

srcNome = input("Qual nome do aluno você procura?")

for i in range(qtdeAlunos):
    if srcNome == alunos[i]:
        print(i, "-", alunos[i])
