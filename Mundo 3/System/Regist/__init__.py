def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def regist_person(name = 'Unknown'):
    with open('cursoemvideo.txt', 'a') as arquivo:
        
        while True:
            enter = input('Name: ').title().strip()
            
            if not enter:
                enter = name
                break
            
            if not all(c.isalpha() or c.isspace() for c in enter):
                print('Prohibited characters have been detected!')
                continue
            break
        
        while True:
            try:
                age = int(input('Age: '))
                if age < 0 or age > 120:
                    print('Please, enter a valid age!')
                    continue
                break
            except ValueError:
                print('Please, enter a valid age!')
        arquivo.write(f'{enter:<20}  {age:>3} years old\n')
        print(f'{enter} was added!')
    
    
def read_arq():
    try:
        with open('cursoemvideo.txt', 'r') as arquivo:
            data = arquivo.read().strip()
        if not data:
            print('No registration!')
        else:
            print(data)
    except FileNotFoundError:
        print('File not found!')
    

