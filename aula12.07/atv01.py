# vamos criar um sistema de login e senha. crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. em seguida peça as informações e valide o login do usuario

dic_acessos = {
    'felipe': 123456,
    'paulo': 654321
}

usuario_senha = {}
usuario = input('Informe seu USUÁRIO: ')
senha = int(input('Informe sua SENHA: '))
usuario_senha[usuario] = senha

for chave in dic_acessos.keys():
    if chave == usuario: 
        print("Usuario ok")
        if dic_acessos[chave] == senha:
            print('Acesso liberado')
            break
        else:
            print(f'Senha incorreta para o usuario { usuario } ')
            break
else:
    print(f'Usuario { usuario } incorreto')