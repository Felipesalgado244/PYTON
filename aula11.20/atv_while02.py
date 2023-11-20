#faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha igual ao nome do usuario, mostrando uma mensagem de erro e pedindo as informaçoes novamente

# while True:
#     nome = input("informe seu nome: ")
#     senha = input("informe uma senha: ")
#     if senha == nome:
#         print("erro")
#     else:
#         break



#correção do prof
tentativas = 1
while tentativas <= 3:
    usuario = input("Informe seu usuário: ")
    senha = input("Informe sua senha: ")
    if senha == usuario:
        print(f'ERROR: essa foi sua tentativa numero {tentativas}')
        if tentativas == 3:
            print('Suas tentativas acabaram. Tente amanhã')
            break
    else:
        print(f'Acesso liberado')
        break
    tentativas += 1