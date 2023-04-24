usuario = []
senha = []
for i in range(2):
    usuario.append(input("Digite o usuario: "))
    senha.append(input("Digite uma senha: "))

loginUsuario = input("Digite seu usuario: ")
loginSenha = input("Digite sua senha: ")
for x in range(2):
    if loginUsuario == usuario[x] and loginSenha == senha[x]:
        print(loginUsuario, ", Logado com Sucesso")
