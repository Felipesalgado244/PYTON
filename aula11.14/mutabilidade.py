# Alguns cuidados com dados mutaveis
# Mutaveis - são dados que podem ter seu valor alterado na memoria do seu dipositivo
# Imutaveis - são dados que só podem ser ser copiados da memoria do dispositivo

lista  = ['Felipão', 'Felipe']
lista[1] = 'Felipin'
print(lista)
nome = 'Felipe'
# nome = 'Felipão'
# nome[5] = 'a'
novo_nome = nome
nome = 'Felipão'
print(nome)
print(novo_nome)

lista_a = ['Felipão', 'Lindo']
lista_b = lista_a.copy()
lista_c = lista_b
lista_b[1] = 'José'
print(lista_a)
print(lista_b)
print(lista_c)