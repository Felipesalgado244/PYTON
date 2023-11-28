# faça uma funçao que retorne o reverso de um numero inteiro informado. por exemplo: 127 -> 721
def numero_reverso(numero):
    reverso = 0
    while numero > 0:
# Pegar o ultimo valor do numero
        ultimo_valor = numero % 10

        #Add ultimo valor
        reverso = (reverso * 10) + ultimo_valor

        # tira ultimo valor
        numero = numero // 10
    # retorna o reverso
    return reverso

numero = int(input("Informe um numero: "))
resultado = numero_reverso(numero)
print(f'o número informado foi { numero } e o reverso dele é: { resultado }')


