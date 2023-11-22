# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. primo é aquele que é divisivel somente por ele mesmo e por 1.


numero = int(input('Por favor informar um número inteiro: '))
intervalo = range(1, numero+1)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'Foi divisivel por { i }')
        contador += 1

if contador == 2 or contador ==1:
    print(f'O número { numero } é primo')