from random import randint
print(f"""{'---'*12}
{'Joga no Euromilhões':^36}
{'---'*12}""")

num = int(input('How many games do you want? '))
print(f'-=-=- Drawing {num} games -=-=-')

for n in range(1,num + 1):
    atual = []
    
    while len(atual) < 5:
        num = randint(1,50) 
        if num not in atual:
            atual.append(num)
            
    print(f'Game {n}: {sorted(atual)}')
    atual.clear()
    
    while len(atual) < 2:
        num = randint(1,12)
        if num not in atual:
            atual.append(num)  
               
    print(f'Stars: {sorted(atual)}\n')