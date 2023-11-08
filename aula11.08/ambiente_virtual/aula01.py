# A resposta dessa quuestão deve ser:
# FULANO tem altura ALT de altura, pesa PES quilos e  seu IMC é:
#valor

nome = "Felipe"
altura = 1.70
peso = 79
imc = peso / (altura * altura)

print(nome, "tem", altura, "de altura",)
print("pesa", peso, "quilos e seu IMC é:")
print(imc)

print(f'{ nome } tem {altura:.2f} de altura, pesa { peso } quilos e seu imc é: ')
print(f'{imc:.2f}')