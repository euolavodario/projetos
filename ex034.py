#colcacando titulo do progrma!
print('-=-'*20)
print('Analisando Salários')
print('-=-'*20)

s = float(input('Qual á seu salário? R$'))

if s <= 1250.00:
    a = s + (s * 15 / 100)
else:
    a = s + (s * 10 / 100)

print('Quem ganhava R${:.2f} agora ganha R${:.2f}!'.format(s,a))