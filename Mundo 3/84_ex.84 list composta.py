value = [] ; real = []
count = 0

while True:
    while True:
        name = input('Name: ').strip()
        if not name.isalpha():
            print('Cannot contain numbers!')
            continue
        break
    value.append(name)
    count += 1
    value.append(float(input('Weight: ')))
    real.append(value[:])
    value.clear()
    sn = input('Want to continue?[S/N] ').strip().title()
    if sn == 'S':
        continue
    else:
        break
    
min = min(p[1] for p in real)
min_n = [p[0] for p in real if p[1] == min]

max = max(p[1] for p in real)
max_n = [p[0] for p in real if p[1] == max]

print(f'{count} people registered!')
print(f'The greatest weight is {min:.2f}Kg. Weight of {', '.join(min_n)}')
print(f'the lowest weight was {max:.2f}Kg. Weight of {'. '.join(max_n)}')
