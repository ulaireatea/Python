resp = 'S'
soma = quant = med = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
med = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, med))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
