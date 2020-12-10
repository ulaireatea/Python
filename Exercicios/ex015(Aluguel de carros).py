d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
v = (d*60)+(0.15*k)
print('O total a pagar é de R$ {:.2f}'.format(v))
