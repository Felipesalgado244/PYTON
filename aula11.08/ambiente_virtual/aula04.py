# outra forma de INTERPOLAR

nome = "Felipe"
salario = 4500.99

print(nome, "Ganha um salario de R$", salario)
print(f'O salario de {nome} é R$ { salario }')
# Forma FORMAT de imprimir
# s - string
# d  i - int
# f - float
# x  X - hexadecimais
print('O salario de %s é R$ %.f' % (nome, salario))
print('Quem ganha um salario de R$ %.2f é o %s' % (salario, nome))
