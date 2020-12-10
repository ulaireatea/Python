from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa.''')
    opção = int(input('>>> Qual sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A produto de {} x {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Digite novos valores.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa.')
