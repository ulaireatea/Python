from math import trunc
num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
# ou ainda e possível importar toda biblioteca
import math
num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))
# ou ainda usando uma função intena (neste exercício é possível)
num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))
