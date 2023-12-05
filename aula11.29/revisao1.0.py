variavel = 1

print(variavel)

variavel = "A casa do Kaynan é azul igual ao céu"
#           012345678910
# -11-10-9-8-7-6-5-4-3-2-1
print(variavel)
#regra do fatiamento [inicio, fim, step]
print(variavel[-17:-12])
print(variavel[-3:])

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#         0    1    2    3    4    5    6
#        -7   -6   -5   -4   -3   -2   -1

print()

#ultilizando fatiamento e repetição imprima uma lista de "a" até "e" removendo uma letra de cada vez.
lista = ['a', 'b', 'c', 'd', 'e']

for i in range(5):
    rm = lista[:5-i]
    print(rm)

#fazer 10 questões em umcodigo e dizer se está certo ou errado
# q1 = "f"
# q2 = "v"
# q3 = "f"
# q4 = "v"
# q5 = "f"
# q6 = "v"
# q7 = "f"
# q8 = "v"
# q9 = "f"
# q10 = "v"

# questoes = q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
# questao = questoes

# for i in  range(1, 11):
#     i = input("V ou F: ")
#     if questoes == questao:
#         print("vc acertou")
#     else:
#         questoes != questao
#         print('vc errou')




q1 = 2
q2 = 2
q3 = 3
q4 = 4
q5 = 5
q6 = 6
q7 = 7
q8 = 8
q9 = 9
q10 = 10
questoes = q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
questao = questoes
for i in questoes:
    questao = int(input('Digite o valor: '))
    if i == questao:
        print('Você acertou!')
    else:
        i != questao
        print('Você errou.')
