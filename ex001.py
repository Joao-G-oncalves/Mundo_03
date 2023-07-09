from time import sleep
num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
      'quatorze', 'treze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
a = int(input('Digite um número de 0 a 20: '))
while True:
    if a < 0 or a > 20:
        a = int(input('Número inválido, digite um número de 0 a 20: '))
    else:
        print('-' * 40)
        print(f'Você digitou o número {num[a]}')
        print('-' * 40)
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        while continuar not in 'sn':
            continuar = str(input(f'\033[31mResposta inválida!\033[m \nDeseja continuar? [S/N] ')).strip().lower()[0]
        print('-' * 40)
        if continuar in 's':
            a = int(input('Digite um número de 0 a 20: '))
        else:
            print('Saindo ', end='')
            x = '\033[1:31m.', '\033[1:34m.', '\033[1:33m.\033[m'
            for i in range(0, len(x)):
                print(x[i], end=' ')
                sleep(1)

            print('')
            break
print('~' * 40)
