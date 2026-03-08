# Lottery Game Generator
# This program generates random lottery games,
# each containing 6 unique numbers between 1 and 60.

from random import sample
from time import sleep
number_of_games = int(input('Number of games to generate: '))
games = []
for _ in range(number_of_games):
    game = sorted(sample(range(1, 61), 6))
    games.append(game)
print()
print(f'Generating {number_of_games} games...')
sleep(1)
for index, game in enumerate(games, start=1):
    print(f'Game {index}: {game}')
    sleep(1)
print('GOOD LUCK!')
