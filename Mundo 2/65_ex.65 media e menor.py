exit = count = total = big = less = 0
while exit != 'N':
    num = float(input('Enter a number: '))
    if count == 0:
        less = num
        big = num
    else: 
        if big < num:
            big = num
        if less > num:
            less = num
    count += 1
    total += num
    exit = input('Want continue? [S/N] ').title().strip()
    
average = total / count
print(f'You typed in {count} numbers and the average was {average:.1f} .')   
print(f'The smallest number is {less:g} and the largest is {big:g} .')