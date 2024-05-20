from time import sleep

d = float(input('Qual é a distancia da viagem em Km? '))
p = d*50 if d <= 200 else d*0.45
print('Você está preste a comprar uma viagem de {d}Km!')
sleep(1)
print('E o preço que você terá que pagar pela passagem será de R${:.2f}'.format(p))
#if d <= 200:
   # p = d*0.5
   # print('O preço da passagem será de R${}!'.format(p))
#else:
    #p = d*0.45
    #print('O preço da passagem será de R${}!'.format(p))
