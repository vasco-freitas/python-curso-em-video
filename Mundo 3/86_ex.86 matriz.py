matrix = [[],[],[]]
index = 0 ; num = 0

for n in range(0,9):
    matrix[index].append(int(input(f'Enter a value to [{index},{num}]: ')))
    num += 1
    if num == 3: 
        index += 1
        num = 0
        
print('==--=='*10)

for n in matrix:
    for e in n:
        print(f'[{e:^5}]', end = '')
    print()

#print(f'''{matrix[0]}
#{matrix[1]}      
#{matrix[2]}''')