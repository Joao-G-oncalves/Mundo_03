from random import randint
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Os valores sorteados foram: ', end='')
for cont in tupla:
    print(f'{cont}', end=' ')
print(f'\nO maior valor sorteado foi o {max(tupla)}')
print(f'O menor valor sorteado foi o {min(tupla)}')
