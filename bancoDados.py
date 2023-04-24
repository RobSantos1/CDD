usuario = []
senha = []
for i in range(5):
    usuario.append(input("Digite o usuario: "))
    senha.append(input("Digite uma senha: "))

for x in range(5):
    print(x, "-", usuario[x], senha[x])
