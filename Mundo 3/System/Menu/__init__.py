from Regist import *

def line():
    return '--'*20


def header(sms):
    return f"""{line()}
{sms}
{line()}"""


def read_option(num):
    while True:
        try: 
            n = int(input(num))
            if n > 3 or n < 1:
                print("Choose options 1, 2 or 3!")
            else:
                return n
        except ValueError:
            print("Choose options 1, 2 or 3!")


def main_menu(*lista):
    while True:
        print(f"{header('MAIN MENU'.center(40))}")
        
        for n in lista:
            print(n)
                      
        print(line())
        option = read_option(('Your option: '))
        if option == 1:
            print(header('Registered People'))
            read_arq()
        elif option == 2: 
            print(header('New Registration'))
            regist_person()
        else:
            print(header('Leaving the system... See you soon.'))
            break