# Estruturas condicionais
vriavel = 20
if vriavel < 20:
    print("menor que 20")
elif vriavel == 20:
    print('igual')
elif vriavel > 20 and vriavel < 50:
    print("Está no intervalo entre 21 e 49")
else:
    print("Qualquer outra coisa")

# Estuturas de repetição
#FOR e WHILE
for i in range(1, 10, 2):
    print(f'print o numero { i }')

contador = 5
while contador > 0:
    print(f'Esse é o int do número { contador }')
    contador -= 1

# join - unir strings
lista = ['Felipe', 'morais', 'II']
nome = ' '.join(lista)
print(nome)