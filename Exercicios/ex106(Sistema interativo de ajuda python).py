from time import sleep
c = ('\033[m',          # 0
     '\033[0;30;41m'    # 1
     '\033[0;30;42m'    # 2
     '\033[0;30;43m'    # 3
     '\033[0;30;44m'    # 4
     '\033[0;30;45m'    # 5
     '\033[7;30m'       # 6
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema de ajuda pyhelp', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'Fim':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
