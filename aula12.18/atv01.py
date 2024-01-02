# Dunder metodo => __metodo__
# mostrar classe: __class__.__name__

class Pessoa:
    nome = 'Felipe'

class Empregado(Pessoa):
    cargo = 'porteiro'
    salario = 1000

class Estudante(Pessoa):
    matricula = 121314

class EstudanteGraduacao:
    curso = 'ADM'

class EstudantePos:
    orientador = 'Chico'
    nivel = 1

Pessoa = Pessoa()
pessoa2 = EstudantePos()

print(f'Olá orientador {pessoa2.orientador}')
print(f'Olá {Pessoa.nome} sua matricula é {Estudante.matricula}')