'''real = [[],[]]

for n in range (1,7):
    num = int(input(f'Enter a number {n}: '))
    if num % 2 == 0:
        real[0].append(num)
    else:
        real[1].append(num)
        
real[0].sort()
real[1].sort()

print(f'Even numbers {real[0]} and odd numbers {real[1]}!')'''

real = [[],[]]

for n in range (1,5):
    numb = int(input('Enter a number: '))
    
    if numb % 2 == 0:
        real[0].append(numb)
    else:
        real[1].append(numb)

real[0].sort()
real[1].sort()

print(real[0])
print(real[1])