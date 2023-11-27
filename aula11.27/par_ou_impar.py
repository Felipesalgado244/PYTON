jogador01 = input("Escolha par ou impar: ").lower()
if jogador01 == 'par':
    jogador02 = 'impar'
else:
    jogador02 = 'par'

numero_jogador1 = int(input("Escolha seu numero: "))
numero_jogador2 = int(input("Escolha seu numero: "))

resultado = numero_jogador1 + numero_jogador2
if resultado % 2 == 0:
    if jogador01 == 'par':
        print("jogador 1. You win!!!")
    else:
        print("jogador 2. You win!!!")
else: 
    if jogador01 == 'impar':
        print("jogador 1. You win!!!")
    else:
        print("jogador 2. You win!!!")