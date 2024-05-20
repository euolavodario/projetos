s = float(input('Qual é o seu salário atual? '))
a = s+(s*15/100)

print('Parabens você recebeu um aumento de 15%, agora seu salário de R${:.2f} é de R${:.2f}!'.format(s,a))