class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.cpf = None

    def __str__(self):
        return f'Nome: {self.nome}, idade: {self.idade}, CPF: {self.__cpf}'
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoas):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

    def __str__(self):
        return f'Salario: {self.salario}, Disciplina: {self.disciplina}.'
    
class Aluno(Pessoas):
    ...


class Homem(Pessoas):
    ...

class Mulher(Pessoas):
    ...

elvis = Homem('Elvis', 28)
paula = Mulher('Paula', 19)
paulo = Professor('Paulo Junior', 29, 1400.00, 'Backend')


elvis.set_cpf(1234567890)
paula.set_cpf(9876543210)
paulo.set_cpf(1234567890)

print(elvis)
print(paula)
print(paulo)