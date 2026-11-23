value = []
count = 0
while True:
    count += 1 
    num = float(input(f'Enter a number {count}: '))
    if num not in value:
        print('Number added...')
        value.append(num)
    else:
        print('Number not added. It is repeated...')
    yn = input('Want to continue?[S/N] ').strip().title()
    if yn == 'S':
        continue
    else:
        break

sort = sorted(value)
print(f'You entered the values {', '.join(f'{n:g}' for n in sort)}')