class Estudante:
    nome = 'Felipe'
    matricula = 353637

class EstudanteGraduacao(Estudante):
    curso = 'ADS'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'

aluno = EstudanteGraduacao()

print(f'Olá, {aluno.nome} seu curso de graduação é o de {aluno.curso} e a sua matricula de acesso é {aluno.matricula}')

aluno2 = EstudantePos()
print(f'Olá, {aluno2.nome} seu nivel é {aluno2.nivel}° e a seu tutor será o {aluno2.orientador}')

print(aluno.curso)