num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):  # python conta sempre um a menos por isso o +1
    if num % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[mO número {} foi divísível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso este número é PRIMO')
else:
    print('E por isso NÃO é Primo')
