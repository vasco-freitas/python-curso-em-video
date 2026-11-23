value = []

for n in range (1,6):
    while True:
        try:
            num = float(input(f'Enter a number {n}: '))
            if num in value:
                print('Repeated number. Try again')
                continue
            break
        except ValueError:
            print('Enter a number!')
            
    if len(value) == 0 or num > max(value):
        print('Added to last position of list...')
        value.append(num)
    elif num < min(value):
        print('Added to Position 1 of the list...')
        value.insert(0, num)
    else:
        for e, i in enumerate(value):
            if num > i:
                value.insert(i, num)
                print(f'inseirdo {e}')
            
print(value)
            
