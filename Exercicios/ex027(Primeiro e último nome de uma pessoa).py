n = str(input('Digite seu nome completo: ')).strip()
print('Muito Prazer em te conhecer {}!'.format(n))
nome = n.split()
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu último sobrenome é {}'.format(nome[len(nome)-1]))
