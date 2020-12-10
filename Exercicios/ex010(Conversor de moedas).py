real = float(input('Quanto você tem na carteira R$ '))
cotação = float(input('Quanto esta a cotação do dólar hoje R$ '))
print('Hoje com R$ {:.2f} reais, você pode comprar US$ {:.2f} dólares'.format(real, (real/cotação)))
