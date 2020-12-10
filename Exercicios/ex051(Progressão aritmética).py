primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
ene = primeiro + (11 - 1) * razão # isto fará com que exiba os 10 primeiros termos de uma pa
for c in range(primeiro, ene, razão):
    print('{}'.format(c), end=' -> ')
print('Fim')
