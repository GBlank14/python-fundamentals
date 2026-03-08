# ATM Simulator
# This program calculates the number of banknotes
# needed for a withdrawal amount.

amount = int(input('Withdraw amount: $'))
notes_50 = amount // 50
rest = amount % 50
notes_20 = rest // 20
rest = rest % 20
notes_10 = rest // 10
rest = rest % 10
notes_1 = rest // 1
print(f'Total of {notes_50} notes of $50')
print(f'Total of {notes_20} notes of $20')
print(f'Total of {notes_10} notes of $10')
print(f'Total of {notes_1} notes of $1')
