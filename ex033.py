#definindo funções
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite um último número: '))

#verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#printando o maior e o menor
print('O MAIOR número digitado foi o {}!'.format(maior))
print('O MENOR número digitado foi o {}!'.format(menor))

