p = float(input('Informe o peso em Kg: '))
a = float(input('Informa a altura em metros: '))
imc = p / (a**2)
print('O índice de massa corporal desta pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
