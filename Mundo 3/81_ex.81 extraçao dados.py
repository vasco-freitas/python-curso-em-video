values = []
count = 0
while True:
    count += 1
    values.append(float(input(f'Enter a number {count}: ')))
    while True:
        yn = input('Want to continue?[S/N] ').strip().title()
        if yn not in ['S','N']:
            print('Responds with S or N.')
            continue
        break
    if yn == 'S':
        continue
    else:
        break
    
sort = sorted(values, reverse=True)

print(f'''You have entered {len(values)} elements!
Value in descending order are {', '.join(f'{n:g}' for n in sort)}''')

if 5 in values:
    print(f'The value 5 is part of the list! In index{[index + 1 for index, n in enumerate(values) if n == 5]}')
else:
    print('The value 5 not is part of the list!')