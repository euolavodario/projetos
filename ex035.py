#colcacando titulo do progrma!
print('-=-'*20)
print('Analisando Triângulos')
print('-=-'*20)

r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('É POSSÍVEL criar um triangulo com os três segmentos!')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo!')
