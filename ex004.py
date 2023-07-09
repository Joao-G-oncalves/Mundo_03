tupla = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), \
        int(input('Digite outro número: '))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Foram digitados os seguintes números pares: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')
