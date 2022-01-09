import emoji
import colorama
from colorama import Fore, Back, Style
from random import randint
colorama.init(autoreset=True)
print(f'{Fore.BLUE}=' * 20)
print(f'{Fore.RED}Even or Odd Game')
print(f'{Fore.BLUE}=' * 20)
cont = 0
while True:
    game = randint(0, 10)
    user = int(input(f'{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}Enter a value: '))
    parimpar = str(input(f'{Fore.LIGHTYELLOW_EX + Style.BRIGHT}Even or Odd [E/O]: ')).strip().upper()
    print(f'{Fore.BLUE}=' * 20)
    soma = game + user
    if soma % 2 == 0 and parimpar == 'E':
        cont += 1
    elif soma % 2 != 0 and parimpar == 'O':
        cont += 1
    else:
        break
print(f'{Fore.CYAN}=-' * 25)
print(f'{Back.LIGHTGREEN_EX + Fore.BLACK + Style.BRIGHT}You chose {user} and the game {game}. The total is {soma}!')
print(emoji.emojize(f'{Back.LIGHTGREEN_EX + Fore.BLACK + Style.BRIGHT}GAME OVER!You won {cont} time(s) {Back.RESET +  Fore.RED} :fire: :fire: :fire: :fire: :fire: :fire:'))
print(f'{Fore.CYAN}=-' * 25)
