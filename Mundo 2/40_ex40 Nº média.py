while True:
    try:
        NUM = float(input('First note: '))
        if not 0 <= NUM or NUM >= 20:
            print('Error! The note must be between 0 and 20.')
            continue
        break
    except ValueError:
        print('Please, enter a valid number.')
    
while True:
    try:        
        NUMB = float(input('Second note: '))
        if not 0 <= NUMB  or NUMB >= 20:
            print('Error! The note must be between 0 and 20.')
            continue
        break
    except ValueError:
        print('Plese, enter a valid number.')

AVERAGE = (NUM + NUMB) / 2

print(f'With the notes {NUM:g} and {NUMB:g}, the average of the student is {AVERAGE:g}!') 

if 8 <= AVERAGE <= 10:
    print('Goes to Recovery!')
    
elif AVERAGE >= 10:
    print('The student has been approved!')

else:
    print('The student failed!')