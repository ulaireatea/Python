dist = float(input('Qual a distância da viagem? '))
print('Você está preste a iniciar uma viagem de {} km.'.format(dist))
if dist <= 200:
    custo = dist * 0.50
else:
    custo = dist * 0.45
print('O custo de sua viagem será R$ {:.2f} '.format(custo))
