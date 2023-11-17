contador = 0
while contador < 20:
    idade = int(input("Informe sua idade: "))
    if idade > 13:
        print(f'O aluno {contador} tem mais de 13 anos')
    contador += 1
    