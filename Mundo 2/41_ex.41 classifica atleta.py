#personalizando
from datetime import datetime

#estrutura
current_year = datetime.now().year
cem = current_year - 100

#perguntando
while True:
    try:
        BIRTH = int(input("In what year were you born? "))
        if not cem <= BIRTH <= current_year:
            print(f"Invalid year! Please enter a year between {cem} and {current_year}.")
            continue
        break
    except ValueError:
        print("Invalid input. Please, enter a valid number for the year.")
 
#informacoes do usuário        
age = current_year - BIRTH
print(f'\nThe athlete is {age} years old.')

#respondendo 
if age <= 9:
    print("Mirim")
elif age <= 14:
    print("Infantil")    
elif age <= 19:
    print('Junior')
elif age <= 25:
    print("Senior")    
else:
    print("Master")