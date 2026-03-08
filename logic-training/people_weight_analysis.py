# People Weight Analysis
# This program registers people with their weights
# and shows how many were registered, along with
# the heaviest and lightest people.

people = []
while True:
    name = input('Enter name: ').strip()
    weight = float(input('Enter weight: '))
    people.append([name, weight])
    continue_option = input('Enter [Y] to register another person: ').strip().upper()
    if continue_option != 'Y':
        break
total_registered = len(people)
highest_weight = people[0][1]
lowest_weight = people[0][1]
heaviest_people = []
lightest_people = []
for person in people:
    if person[1] > highest_weight:
        highest_weight = person[1]
    if person[1] < lowest_weight:
        lowest_weight = person[1]
for person in people:
    if person[1] == highest_weight:
        heaviest_people.append(person[0])
    if person[1] == lowest_weight:
        lightest_people.append(person[0])
print(f'You registered {total_registered} people')
print(f'The highest weight was {highest_weight} kg. {heaviest_people}')
print(f'The lowest weight was {lowest_weight} kg. {lightest_people}')
