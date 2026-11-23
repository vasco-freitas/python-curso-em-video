from datetime import datetime #importao modulo data e  hora atual 
year = int(input('Which year do you want to check? Enter 0 for the current year: '))

if year == 0: #se a variavel year for igual a 0
    year = datetime.now().year #variavel year recebe o ano atual
    
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): #se a variavel year for divisivel por 400 ou se a variavel year for divisivel por 4 e nao for divisivel por 100
    print(f'The year {year} is a leep year.') 
    
else:
    print(f'The year {year} is not a leap year.')
    