# Professional Profile Analyzer
# This program collects personal and professional information from the user
# and classifies career stage, professional level, income class,
# estimated growth potential, and current market status.

name = input('Enter your name: ').strip()
age = int(input('Enter your age: '))
salary = float(input('Enter your salary: '))
years_experience = float(input('Enter how many years of experience you have: '))
field = input('Enter your field of work: ').strip()
print('=' * 20)
print('PROFESSIONAL PROFILE')
print('=' * 20)
print()
print(f'Name: {name}')
print(f'Field of work: {field}')
print(f'Age: {age}')
print(f'Experience: {years_experience}')
print()
if age < 18:
    career_stage = 'Too young for job market'
elif age <= 25:
    career_stage = 'Career starter'
elif age <= 40:
    career_stage = 'Growth phase'
elif age <= 60:
    career_stage = 'Experienced professional'
else:
    career_stage = 'Veteran'
if years_experience <= 1:
    professional_level = 'Junior professional'
elif years_experience <= 5:
    professional_level = 'Mid-level professional'
elif years_experience <= 10:
    professional_level = 'Senior professional'
else:
    professional_level = 'Specialist'
if salary <= 2000:
    income_class = 'Low income'
elif salary <= 6000:
    income_class = 'Middle income'
elif salary <= 15000:
    income_class = 'High income'
else:
    income_class = 'Elite professional'
growth_potential = salary * (1 + years_experience / 10)
market_status = 'Undefined market status'
if professional_level == 'Junior professional' and income_class == 'Low income':
    market_status = 'Weak in the job market'
elif (professional_level == 'Junior professional' or professional_level == 'Mid-level professional') and income_class == 'Middle income':
    market_status = 'Professional in development phase'
elif professional_level == 'Senior professional' or income_class == 'High income':
    market_status = 'Competitive professional'
elif professional_level == 'Specialist' or income_class == 'Elite professional' or growth_potential >= 7000:
    market_status = 'Outstanding professional'
print(f'Career Stage: {career_stage}')
print(f'Professional Level: {professional_level}')
print(f'Income Class: {income_class}')
print()
print(f'Estimated Growth Potential: ${growth_potential:.2f}')
print()
print(f'Market Status: {market_status}')
print('=' * 20)
