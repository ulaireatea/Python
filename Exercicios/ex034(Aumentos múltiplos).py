sal = float(input('Qual o salário do funcionário? R$ '))
if sal <= 1250:
    novo = sal * 1.15
else:
    novo = sal * 1.10
print('Quem recebia R$ {:.2f} passa a receber R$ {:.2f}'.format(sal, novo))
