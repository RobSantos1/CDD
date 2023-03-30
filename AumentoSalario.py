
nome = input("Qual seu nome ?" )
idade = input("Quantos anos você tem ?" )
salario = float(input("Quanto você já recebe?" ))
aumento = float(input("Quanto você pretende receber de aumento (Porcentagem)" ))

novoSalario = salario + (salario * aumento/100)

print("\nNome:", nome, "\nIdade:", idade, "\nSalario:", salario, "\nSalario após aumento:", novoSalario)
