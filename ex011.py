l = float(input('Qual é a altura da parede em metros? '))
h = float(input('Qual é a altura dessa parede em metros? '))
a = l*h
p = a/2

print('A sua parede tem uma área de {}m2'.format(a))
print('Sabendo disso você precisar de {:3f} litros de tinta!'.format(p))