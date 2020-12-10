n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1, n2, nota))
# if nota >= 6:
#    print('O aluno está Aprovado.')
# elif nota < 4:
#    print('O aluno está de Reprovado.')
# else:
#    print('O aluno está de Recuperação.')
if nota >=4 and nota <6:
    print('O aluno está de Recuperação.')
elif nota < 4:
    print('O aluno está de Reprovado.')
else:
    print('O aluno está Aprovado.')