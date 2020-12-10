from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jog = int(input('Qual sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jog]))
print('-='*11)
if comp == 0: #comp jogou pedra
    if jog == 0:
        print('Empate')
    elif jog == 1:
        print('Você Venceu')
    elif jog == 2:
        print('Você Perdeu')
    else:
        print('Jogada inválida')
elif comp == 1: #comp jogou papel
    if jog == 0:
        print('Você Perdeu')
    elif jog == 1:
        print('Empate')
    elif jog == 2:
        print('Você Venceu')
    else:
        print('Jogada inválida')
elif comp == 2: #comp jogou tesoura
    if jog == 0:
        print('Você Venceu')
    elif jog == 1:
        print('Você Perdeu')
    elif jog == 2:
        print('Empate')
    else:
        print('Jogada inválida')

