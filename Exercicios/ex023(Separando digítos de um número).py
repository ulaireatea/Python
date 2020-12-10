num = int(input('Digite um número inteiro qualquer: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Unidade {}'.format(uni))
print('Dezena {}'.format(dez))
print('Centena {}'.format(cen))
print('Milhar {}'.format(mil))

# é possível fazer do jeito abaixo mas no momento do curso não temos informação
# n = str(num)
# print('Analisando o número {}...'.format(num))
# print('Unidade {}'.format(n[3]))
# print('Dezena {}'.format(n[2]))
# print('Centena {}'.format(n[1]))
# print('Milhar {}'.format(n[0]))

