times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*20)
print(f'lista de times: {times}')
print('-='*20)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-='*20)
print(f'OS últimos 4 colocados são: {times[-4:]}')
print('-='*20)
print(f'Times em ordme alfabética: {sorted(times)}')
print('-='*20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
