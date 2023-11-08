# Fatiamento de strings
# OBS toda string por padrão é uma lista que não saiu do armário
# Ordem de tratamento
# 0123456.....
# - 654321.....
# [i:f:p] = i - inicio, f - fim, p - parse

nome = "Rodrigo Jose dos Santos Amaral Neto Junior"
print(nome[17:23])
print(nome[-6:])
print(nome[0::2])
print(nome[1::2])

print("="*20)
lista_nome = ("F","e","l","i","p","e")
print(nome[3])
print(nome[-2])
print(lista_nome[3])
print(lista_nome[-2])