from time import sleep

v = float(input('A quantos em Km/h o carro estava? '))
m = (v-80)*7

if v > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade que é de 80 Km/h!')
    print('PROCESSANDO...')
    sleep(2)
    print('Você terá que pagar R${:.2f} de multa!'.format(m))
else:
    print('Tudo certo! Tenha um bom dia cidadão!')