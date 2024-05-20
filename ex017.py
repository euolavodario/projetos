import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
'''hip = (co**2+ca**2)**(1/2)'''
hip = math.hypot(co,ca)

print('A hipotenusa é igual a {:.2f}'.format(hip))

