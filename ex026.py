frase = input('Escreva uma frase: ').upper().strip()

print('A letra "A" aprarece {} vezes na frase!'.format(frase.count('A')))
print('A letra "A" aparace pela primeira vez na pocisão {}'.format(frase.find('A')+1))
print('A letra "A" aparace pela primeira vez na pocisão {}'.format(frase.rfind('A')+1))