largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura*altura
print('Sua parede tem a dimensão de {}m X {}m e sua área é de {:.3f}m².'.format(largura, altura, área))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(área/2))
