from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5 . Tente adivinhar...")
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você acertou.')
else:
    print('Você perdeu! Pois pensei no número {} e não no número {}'.format(computador, jogador))

