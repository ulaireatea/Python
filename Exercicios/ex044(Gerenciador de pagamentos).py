print('{:=^40}'.format(' Lojas Guanabara '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('O valor para pagamento é R$ {:.2f}'.format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('O valor para pagamento é R$ {:.2f}'.format(total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Compra parcelada em 2X sem juros parcela no valor de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    tparc = int(input('Quantas parcelas? '))
    parcela = total / tparc
    print('Compra parcelada em {}x com juros, parcela no valor de R$ {:.2f}'.format(tparc, parcela))
else:
    print('Escolha uma opção válida')
