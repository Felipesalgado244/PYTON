# Faça um quiz ultilizando dicionario com as seguintes chaves: Pergunta, opções e respostas. Faça a validação da opção escolhida com a resposta e imprima.

# dic_perguntas = {
#     'pergunta': ['quanto é 2 + 2?','kkk' ],
#     'Opções': [1, 2, 3, 4],
#     'resposta': 4,
# }
# print(dic_perguntas['pergunta'][0])
# print(f'Opções {dic_perguntas["Opções"]}')

# pgt = int(input('Responda: '))

# if pgt == dic_perguntas['resposta']:
#     print('Parabéns você acertou')
# else:
#     print(f'Você errou! a resposta correta é { dic_perguntas["resposta"] }')


dic_perguntas = [
    {'pergunta': 'quanto é 2 + 2?',
    'opções': [1, 2, 3, 4],
    'resposta': 4,},

    {'pergunta': 'quanto é 2 + 1?',
    'opções': [1, 2, 3, 4],
    'resposta': 3,},

    {'pergunta': 'quanto é 2 + 3?',
    'opções': [1, 2, 3, 4, 5],
    'resposta': 5,},
]

for pergunta in dic_perguntas:
    print('pergunta:', pergunta['pergunta'] )
    print()

    for i, opcao in enumerate(pergunta['opções']):
        print(f'{i+1})', opcao)
        print()

        