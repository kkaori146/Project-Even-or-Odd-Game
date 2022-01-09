from random import randint
print('=' * 20)
print('Even or Odd Game')
print('=' * 20)
cont = 0
while True:
    game = randint(0, 10)
    user = int(input('Enter a value: '))
    parimpar = str(input('Even or Odd [E/O]: ')).strip().upper()
    soma = game + user
    if soma % 2 == 0 and parimpar == 'E':
        cont += 1
    elif soma % 2 != 0 and parimpar == 'O':
        cont += 1
    else:
        break
print('=-' * 25)
print(f'You chose {user} and the game {game}. The total is {soma}!')
print(f'\nGAME OVER!You won {cont} time(s)')
print('=-' * 25)
