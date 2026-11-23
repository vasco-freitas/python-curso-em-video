print('---=== EX:36 House loan ===---')

HOME_VALUE = float(input('Price of the house you intend to buy: '))
SALARY = float(input('Enter your salary: '))
TIME = int(input('How many years of performance? '))
print()

TIME_MONTHS = HOME_VALUE / (TIME * 12)
SALARY_PERCENTAGE  = SALARY * 0.30

MAXIMUM_TERM = 40
MINIMUM_TERM = 5

print(f'To pay off a house of {HOME_VALUE:.2f}€ in {TIME} years, the installment will be {TIME_MONTHS:.2f}€. But your limit is {SALARY_PERCENTAGE:.2f}€.\n')

if TIME > MAXIMUM_TERM or TIME < MINIMUM_TERM:
    print(f'Can not pay in {TIME} years.')
    print('The maximum period to pay the installment is 40 years and the minimum period is 5 years.\n')
elif TIME_MONTHS <= SALARY_PERCENTAGE:
    print('Loan Accepted!')
else:
    print('Loan declined!')
    
print('See you next time!')
