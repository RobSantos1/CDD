numAlunos = int(input("Quantos alunos existem na sala ? "))
cont = 0
soma = 0
while cont < numAlunos:  #contador é menor que o numero de alunos
    notas = float(input("Digite a nota dos alunos:"))
    soma += notas
    cont += 1
media = soma / numAlunos
print("A média da turma é:", media)
