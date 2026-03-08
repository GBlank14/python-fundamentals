# Loan Approval System
# This program checks whether a house loan can be approved
# based on salary, house price, payment period, and monthly installment.

name = input('Enter your name: ').strip()
salary = float(input('Enter your salary: '))
house_price = float(input('House price: '))
years = int(input('Enter in how many years you want to pay: '))
monthly_payment = house_price / (years * 12)
print(f'{name}, your monthly payment will be ${monthly_payment:.2f}')
if salary < 2000 or years > 30:
    print('Loan rejected')
elif monthly_payment > salary * 0.30:
    print('Loan rejected')
else:
    print('Loan approved!')
