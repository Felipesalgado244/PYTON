# Operadores IN e NOT IN
nome = "Felipe"
print('Fe'in nome)

print('='*20)

seu_nome = input('informe seu nome: ')
buscar = input('Informe o valor a  ser encontrado: ')

if ( buscar in seu_nome ): 
    print(f'{ buscar } está contido em { seu_nome }')
else:
    print(f'{ buscar } NÃO está contido em { seu_nome }')
    

nao_nome = "Felipinho"
print("au" not in nao_nome)