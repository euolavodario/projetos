# preço com desconto
p = float(input('Qual é o preço do produto para a liquidação 5OFF? R$'))
np = p-(p*5/100)

print('O produto que era {} em liquidação fica: {:2f}!'.format(p, np))