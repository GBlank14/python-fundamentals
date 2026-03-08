# Rock Paper Scissors Game
# The player chooses rock, paper, or scissors.
# The computer makes a random choice and the program shows the result.

from random import choice
from time import sleep

player_choice = int(input("""[0] ROCK
[1] PAPER
[2] SCISSORS
Choose which you want to play: """))
computer_choices = [0, 1, 2]
computer_choice = choice(computer_choices)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if player_choice == 0 and computer_choice == 1:
    print("""----------------
You play Rock
Computer plays Paper
----------------
You lose!""")
elif player_choice == 0 and computer_choice == 2:
    print("""----------------
You play Rock
Computer plays Scissors
----------------
You win!""")
elif player_choice == 0 and computer_choice == 0:
    print("""----------------
You play Rock
Computer plays Rock
----------------
Draw!""")
elif player_choice == 1 and computer_choice == 1:
    print("""----------------
You play Paper
Computer plays Paper
----------------
Draw!""")
elif player_choice == 1 and computer_choice == 0:
    print("""----------------
You play Paper
Computer plays Rock
----------------
You win!""")
elif player_choice == 1 and computer_choice == 2:
    print("""----------------
You play Paper
Computer plays Scissors
----------------
You lose!""")
elif player_choice == 2 and computer_choice == 1:
    print("""----------------
You play Scissors
Computer plays Paper
----------------
You win!""")
elif player_choice == 2 and computer_choice == 2:
    print("""----------------
You play Scissors
Computer plays Scissors
----------------
Draw!""")
else:
    print("""----------------
You play Scissors
Computer plays Rock
----------------
You lose!""")
