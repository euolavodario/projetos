#sortear 4 alunos para 1 deles ser o sorteado a limpar o quadro, ele vai ler o nnome deles e escerver o escolhido
import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1,a2,a3,a4]

s = random.choice(alunos)

print('Parabens, o aluno escolhido foi {}, agora vai limpar a lousa'.format(s))