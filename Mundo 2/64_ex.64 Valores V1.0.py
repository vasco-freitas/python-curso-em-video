value = total = count = 0
while value != 999:
    value = int(input('Enter a number [999 to stop] '))
    if value == 999:
        break
    total += value
    count += 1
print(f'You have entered {count} numbers and the sum between them is {total}!')