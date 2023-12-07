# Faça um codigo que pede a marca e o modelo do carro do cliente isere ele em uma lista e depois transforma em dicionario. imprima os dois resultados
lista_de_carros = []
marca = input('informe a Marca do seu carro: ')
modelo = input('informe o modelo do seu carro: ')

lista_de_carros.append(marca)
lista_de_carros.append(modelo)

dic_carros = {}
dic_carros.update([lista_de_carros])

print(lista_de_carros)
print(dic_carros)
