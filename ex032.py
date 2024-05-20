from datetime import date
from time import sleep

ano = int(input('Me diga um ano(Coloque 0 para pegar o ANO ATUAL!): '))

if ano == 0:
    ano = date.today().year

print('-=-'*30)
print('Analisando o ano {}'.format(ano))
print('-=-'*30)
sleep(1)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!😁'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!🧐'.format(ano))