#ler um angulo e mostrar na tela o valor do seno, cosseno e tangente.
import math

a = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(a))
coss = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O o seno do ângulo {}° é igual a: {:.3f}'.format(a,sen))
print('O cosseno de {}° é igaul a {:.3f}'.format(a,coss))
print('A tangente de {} é igual a {:.3f}'.format(a,tan))

