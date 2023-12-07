# VAmos criar um sistema de login e senha. crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. em seguida peça as informações e valide o ligin do usuario.
dic_acesso = {'felipe': 123456, 'paulo':111111}
user_pass = {}
usuario = input("Informe seu nome de usuario: ")
senha = int(input("Informe sua senha: "))

user_pass[usuario] = senha

for chave in dic_acesso.keys():
    if dic_acesso[chave] == user_pass[usuario]:
        if chave == usuario:
            print('Seu acesso foi liberado')
            break