nome = str(input('Digite o seu nome completo: ')).strip()
sep = nome.split()
#--------------------------------------------------------------
print('Muito Prazer em te conhecer {}!'.format(nome))
print('Seu primeiro nome é {}' .format(sep[0]))
print('Seu ultimo nome é {}'.format(sep[len(sep)-1]))
print('Seu nome tem {} letras!'.format(len(sep)))
