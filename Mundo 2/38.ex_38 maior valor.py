NUM = float(input('First number: '))
S_NUM = float(input('Second number: '))

if NUM == S_NUM:
    print(f'The two values {NUM:g} and {S_NUM:g} are equals!')
elif NUM > S_NUM:
    print(f'The first value {NUM:g} is higher!')
else:
    print(f'The second value {S_NUM:g} is higher! ')