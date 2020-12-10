import math
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, math.tan(math.radians(a))))
# usando apenas os itens necessário da biblioteca math
from math import sin, cos, tan, radians
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {} graus tem o Seno de {:.2f}'.format(a, tan(radians(a))))
