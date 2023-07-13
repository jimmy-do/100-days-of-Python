# Simple BMI Calculator
# BMI = (weight) / (height^2)

weight = int(input('How much do you weight in kg? '))
height = float(input('How tall are you in m?'))

bmi = round(weight / (height ** 2))

# print(bmi)

if bmi < 18.5:
    print('Your bmi is ' + bmi + ', you are underweight.')
elif bmi < 25:
    print('You are normal weight.')
elif bmi < 30:
    print('You are overweight.')
elif bmi < 35:
    print('You are obese.')
else:
    print('You are clinically obese.')
