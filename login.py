usuario_1 = "admin"
usuario_1_senha= "1234"

usuario = input("Digite o seu nome de usuário: ")
senha = input("Digite a sua senha: ")

if usuario == usuario_1 and senha == usuario_1_senha:
    print("Acesso permitido")
else:
    print("Acesso negado")
    print("Usuário ou senha incorretos")