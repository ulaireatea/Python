imóvel = float(input('Qual o valor do imóvel R$ '))
sal = float(input('Informe sua renda R$ '))
tempo = int(input('Em quantos anos pretende pagar: '))
prest = imóvel / (tempo * 12)
min = sal * 30 / 100
print('Para pagar um imóvel de R${:.2f} em {} anos, \na prestação será de R$ {:.2f}'.format(imóvel, tempo, prest))
if prest <= min:
    print('Empréstimo Aprovado.')
else:
    print("Empréstimo Negado, lamentamos.")

