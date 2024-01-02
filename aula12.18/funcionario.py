# crie a abstração para uma super classe funcionario com duas subclasses. imprima todos os dados

class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
class Professor(Funcionario):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def __str__(self):
        return f'Salario: {self.salario} Disciplina: {self.disciplina}.'
    
paulo = Professor('Paulo', 20, 1300.00, 'Backend/Frontend')

print(paulo)