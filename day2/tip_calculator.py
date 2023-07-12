# Welcome to the tip calculator.
# What was the total bill? $124.46
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill? 7
# Each person should pay: $19.93

print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
percentage_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
amount_of_people = int(input('How many people to split the bill? '))
cost_per_person = (total_bill * (percentage_tip/100) + total_bill) / amount_of_people
print(f'Each person should pay: ${round(cost_per_person, 2)}')