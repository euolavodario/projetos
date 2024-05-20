d = int(input('A quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
total = (d*60)+(km*0.15)

print('O total a pagar pelo aluguel do carro é de: R${:.2f}'.format(total))