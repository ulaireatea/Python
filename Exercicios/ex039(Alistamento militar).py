from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente, infelizmente.')
elif idade < 18:
    print('Ainda faltam {} para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
else:
    print('Você já deveria ter se alistado a {} anos.'.format(idade - 18))
    print('Você se alistou em {}.'.format(atual - (idade - 18)))
