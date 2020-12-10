cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacent: '))
# não usando a biblioteca
hip1 = (cato**2 + cata**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip1))
# usando apenas os dos sintaxes que foram necessárias
from math import sqrt, pow
hip2 = sqrt(pow(cato, 2)+pow(cata, 2))
print('A hipotenusa vai medir {:.2f}'.format(hip2))
# usando toda biblioteca
import math
hip3 = math.hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hip3))
