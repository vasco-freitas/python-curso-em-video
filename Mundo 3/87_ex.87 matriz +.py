real = [[],[],[]]
for l in range (0,3):
    for n in range(0,3):
        real[l].append(int(input(f'Enter a value [{l},{n}]: ')))
        
for n in real:
    for e in n:
        print(f'[{e:^5}] ', end = '')
    print()

print(f'The sum of the even numbers is {sum(e for linha in real for e in linha if e % 2 == 0)}!')
print(f'The sum of the values in the third column is {sum(real[2])}!')
print(f'The higheast value in the second line is {max(real[1])}')