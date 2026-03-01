"""
Tuple Ranking System

Features:
- Register players (name, points)
- Calculate highest score
- Calculate second highest score
- Calculate lowest score
- Calculate average score
"""
players=()
menu1='Y'
bottomplayername=''
averagepoints=0
secondpoints=0
while menu1=='Y':
    playername=str(input('Enter player name: ')).strip()
    points=int(input('Enter points: '))
    newplayer=(playername, points)
    players+=((playername, points),)
    averagepoints+=points
    menu1=str(input('Do you want to register another player? (Y/N): ')).strip().upper()
bottomplayerpoints = players[0][1]
topplayerpoints=players[0][1]
for name, points in players:
    if points>topplayerpoints:
        topplayerpoints=points
for name, points in players:
    if points==topplayerpoints:
        print(name, points)
for name, points in players:
    if points<topplayerpoints and points>secondpoints:
        secondpoints=points
for name, points in players:
    if points==secondpoints:
        print(name, points)
for name, points in players:
        if points<bottomplayerpoints:
            bottomplayerpoints=points
for name, points in players:
    if points==bottomplayerpoints:
        print(name, points)
print(f'Average points: {averagepoints/len(players)}')
