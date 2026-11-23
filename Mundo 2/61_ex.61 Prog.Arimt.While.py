term = float(input('Enter the term: '))
reason = float(input('Enter the reason: '))
count = 0
while count != 10:
    total = term + reason * count
    print(f'{total:g}',end=' -> ')
    count += 1
    
print('End')