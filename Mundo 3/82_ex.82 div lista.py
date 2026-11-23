value = [] ; pair = [] ; odd = []

while True:
    value.append(float(input('Enter a number: ')))
    yn = input('Want to continue?[S/N] ').strip().title()
    if yn == 'S':
        continue
    else:
        break
    
print(f'The full list is {", ".join(f'{n:g}' for n in value)}')

for n in value:
    if n % 2 == 0:
        pair.append(n)
        print(f'List pair is {pair}')
    else:
        odd.append(n)
        print(f'List odd is {odd}')
