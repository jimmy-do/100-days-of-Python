# Simple BMI Calculator
# BMI = (weight) / (height^2)

weight = float(input('How much do you weight in kg? '))
height = float(input('How tall are you in m?'))

bmi = round(weight / (height ** 2))

# print(bmi)

if bmi < 18.5:
    print(f'Your bmi is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your bmi is {bmi}, you are normal weight.')
elif bmi < 30:
    print(f'Your bmi is {bmi}, you are overweight.')
elif bmi < 35:
    print(f'Your bmi is {bmi}, you are obese.')
else:
    print(f'Your bmi is {bmi}, you are clinically obese.')
