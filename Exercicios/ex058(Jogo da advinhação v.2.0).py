from random import randint
computador = randint(0, 10)
print('Sou seu computador, acabei de processar um número entre 0 e 10.')
print('Será que consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('...é maior, tente novamente')
        else:
            print('...é menor, tente novamente')
print('Você acertou na {}ºtentativa.'.format(palpites))
