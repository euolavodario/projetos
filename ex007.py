# Duas notas de um aluno, média
aluno = input('Nome do Aluno: ')
n1 = float(input('Nota pv1: '))
n2 = float(input('Nota pv2: '))

m = (n1+n2)/2

print('Média do aluno {} é {:.1f}'.format(aluno, m))