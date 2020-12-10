from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('O atleta é da categoria Mirim.')
elif 9 < idade <= 14:
    print('O atleta é da categoria Infantil.')
elif 14 < idade <= 19:
    print('O atleta é da categoria Júnior.')
elif 19 < idade <= 25:
    print('O atleta é da categoria Sênior.')
else:
    print('O atleta é da categoria Master.')
