speed = float(input('Qual á a velocidade atual do carro? '))
if speed > 100:
    print('Multado! Você excedeu o limite permitido da via que é 100km')
    multa = (speed - 100) * 7
    print('Você deve pagar uma multa no valor de R$ {}'.format(multa))
print('Tenha um bom dia, dirija com segurança')
