l1 = float(input('Digite um valor para o lado 1: '))
l2 = float(input('Digite um valor para o lado 2: '))
l3 = float(input('Digite um valor para o lado 3: '))
iso = l1 == l2 or l1 == l3 or l2 == l3

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores informados podem formar um triângulo.')
    if l1 == l2 == l3:
        print('E o tipo de triângulo formado é Equilátero.')
    elif l1 != l2 != l3 != l1:
        print('E o tipo de triângulo formado é Escaleno.')
    else:
        print('E o tipo de triângulo formado é Isósceles')
else:
    print('Os valores informados não podem formar um triângulo.')
