terms = int(input('How many terms do you want to show? '))
first = 0
sec = 1

print('Sequence: ',end='')
while terms > 0:
    print(first,end=' -> ')
    total = first + sec
    first = sec
    sec = total
    terms -= 1
print('END')