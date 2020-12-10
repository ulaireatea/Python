num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
sel = int(input('Sua opção: '))
if sel == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif sel == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif sel == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente uma opção de 1 à 3.')
