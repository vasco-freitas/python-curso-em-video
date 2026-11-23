term = float(input('First term: ')) 
reason = float(input('Reason of the PA: '))
count = 0 
more_term = 10
count_term = 0

while more_term != 0: 
    total = term + reason * count
    count += 1
    more_term -= 1
    print(f'{total:g}',end=' -> ')
    count_term += 1
    if more_term == 0:
        print('STOP',end='')
        terms = float(input('\nWant to show how many more terms? '))
        more_term += terms
    
print(f'\nHad {count_term} terms in this program!')
print('\nEND')