# Even or Odd Game
# The player chooses a number and whether the result will be even or odd.
# The computer chooses a random number and the program checks who wins.
from random import choice
numbers = list(range(1, 11))
wins = 0
while True:
    computer_number = choice(numbers)
    player_number = int(input('Enter a number from 1 to 10: '))
    choice_even_odd = input('Even or Odd? [E/O]: ').strip().upper()
    total = player_number + computer_number
    if total % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    print(f'You played {player_number} and PC {computer_number}. Total = {total} ({result})')
    if (result == 'Even' and choice_even_odd == 'E') or (result == 'Odd' and choice_even_odd == 'O'):
        wins += 1
        print('You won! Let’s play again...')
    else:
        print(f'GAME OVER! You won {wins} times')
        break
