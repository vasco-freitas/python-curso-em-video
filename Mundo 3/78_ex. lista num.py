value = []
for n in range (1,6):
    while True:
        try:
            value.append(float(input(f'Value in position {n}: ')))
            break
        except ValueError:
            print('Enter a number, please.')
      
min = min(value)
max = max(value)
position = [i + 1 for i, n in enumerate(value) if n == min]
position_max = [i + 1 for i, n in enumerate(value) if n == max]

print(f'You have entered the values {", ".join(f'{n:g}' for n in value )}') 
print(f'The lowest number entered was {min:g} in positions {position}')
print(f'The maximum number is {max:g} in positions {position_max}')




