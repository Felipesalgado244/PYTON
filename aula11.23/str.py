# Count - função contar quantas vezes um determinado caractere aparece em uma string
# upper e a lower - dois metodos que dixam a string toda em maiuscula ou em letra minuscula
# find - busca por uma expressão dentro da frase
# replace - é ultilizado para fazer alterações dentro das strings
# captalize - deixa aprimeira letra das palavras maiuscula
# split - transforma sua string em uma lista
frase = " A banana é amarela e o abacate é verde.".lower()
letra = 'a'
print(f'A letra { letra } aparece { frase.count(letra) } vezes na frase "{ frase }".')
achei = frase.find('rela')
if achei >= 0:
    print(f' A expressão foi encontrada no indice { achei }')
else:
    print(f' A expressão não foi encontrada')


nova_frase = frase.replace('banana', 'maracujá')
nova_frase = frase.replace('abacate', 'manga')
nova_frase2 = frase.replace(' ', '')
print(frase)
print(nova_frase)
print(nova_frase2)
print(frase.capitalize())
print(frase.split())







# saida = input('Digite "S" para sair: ').upper()
# print(saida)
# if  saida == 'S':
#     print(saida)