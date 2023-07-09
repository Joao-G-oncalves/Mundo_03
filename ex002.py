tabela = 'Corinthians', 'Santos', 'Avaí', 'América-MG', 'Bragantino', 'São Paulo', 'Atlético-MG', 'Botafogo', \
         'Internacional', 'Coritiba', 'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo', 'Fluminense', 'Goiás', \
         'Ceará', 'Juventude', 'Atlético-GO', 'Fortaleza'
print('-=-' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=-' * 30)
print(f'Os 5 primeiros são : {tabela[0:5]}')
print('-=-' * 30)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=-' * 30)
print(f'O {tabela[7]} está na {tabela.index("Botafogo")+1}ª posição.')
print('-=-' * 30)
