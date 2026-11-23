real = [] 

while True:
    name = input('Name: ').strip().title()
    n1 = float(input('Note 1: '))
    n2 = float(input('Note 2: '))
    average = (n1 + n2) / 2
    
    real.append([name,n1,n2,average])
    
    while True:
        sn = input('Want to continue?[S/N] ').strip().title()
        if sn not in ['S','N']:
            print('Invalid!')
            continue
        break
    if sn in ['N']:
        break

print(f'''{'===---=='*8}
{'Nª':<3} {'Name':<12} {'Average':<3}
{'-----'*7}''')


for n, aluno in enumerate(real,start=1):
    print(f'{n:<3} {aluno[0]:<12} {aluno[3]:<3}')
    
while True:
    view = int(input('Show grades of which student?[999 to exit] '))
    if view == 999:
        break
    elif 1 <= view <= len(real):
        student = real[view - 1]
        print(f"{student[0]} notes are {student[1]} and {student[2]}!")
    else:
        print(f"Student {view} does not exist!")    
        
    
print('End of session')



    