# 4. Crie um cadastro de clientes recebendo nome, idade, data de nascimento e endreço completo(rua, numero da residencia e bairro). adicone todas as informações em um dicionario e eimprima no final.
nome_usuario = input('Informe seu nome: ')
idade_usuario = int(input('Informe sua idade: '))
data_de_nascimento_usuario = int(input('Informe sua data de nascimento: '))
bairro_usuario = input('Informe seu bairro: ')
nome_da_rua_usuario = input('Informe o nome da rua: ')
numero_da_residencia_usuario = int(input('Informe o numero de sua residencia: '))

dic = {
    'Nome': nome_usuario,
    'Idade': idade_usuario,
    'data de nascimento': data_de_nascimento_usuario,
    'bairro': bairro_usuario,
    'nome da rua': nome_da_rua_usuario,
    'numero_da_residencia': numero_da_residencia_usuario
}

print(dic)
