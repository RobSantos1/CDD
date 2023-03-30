nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno Aprovado!")
elif media >= 4:
    print("Aluno na Recuperação")
else:
    print("Aluno Reprovado!")