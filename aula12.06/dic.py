# Crud - created, Readed, Updated e Deleted
dic = { 'nome': 'Felipe'} # Created
dic2 = dict( idade = 19) # Created
dic['nome'] # Readed
reading = dic2.get('idade') # Readed

dic.update(sobrenome='morais') # Updated
dic.update({'idade': 19}) # Updated
tupla = ('peso', 72.12), # Updated
lista = ['data', '13/04/1996'],['numeros',[1, 2, 3, 4, 5, 6, 7, 8, 9]] # Updated
dic.update(lista)
dic.update(tupla)
print(dic)
print(dic2)

dic.clear() # Deleted
print(f'Dados do dicionario: {dic}')