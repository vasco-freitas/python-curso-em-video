from datetime import datetime 
CURRENT_YEAR = datetime.now().year

while True:
    try:
        BIRTH = int(input('Year of birth: '))
        if BIRTH > CURRENT_YEAR:
            print('Error! Birth year cannot be in the future.')
            continue
        break
    except ValueError:
        print('Please, enter a valid year.')

gender = ['Male', 'Female']

while True:       
    GENDER = input('Is your gender male or female? ').strip().title()       
    
    if GENDER not in gender:
        print('Please, enter your gender.')
    else:
        break  

AGE = CURRENT_YEAR - BIRTH
ARMY_YEAR = BIRTH + 18

print(f'\nThose born in {BIRTH} are {AGE} years old in {CURRENT_YEAR}')

if GENDER == "Female":
    print('Girls do not need to enlist!')
    exit()

if CURRENT_YEAR == ARMY_YEAR:
    print(f'You must enlist immediately!')

elif CURRENT_YEAR < ARMY_YEAR:
    MISSING = ARMY_YEAR - CURRENT_YEAR
    print(f'\nThere are still {MISSING} years to go before enlistment!')
    print(f'Your enlistment in {ARMY_YEAR}.')
        
else:
    MISSING = CURRENT_YEAR - ARMY_YEAR
    print(f'\nYou should have been enlisted {MISSING} years ago!')
    print(f'Your enlistment year was {ARMY_YEAR}.')
