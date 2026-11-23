'''num = int(input("Enter a number: "))
count = num
f = 1

print(f'Calculating {num} != ',end=" ")
while num > 0:
    print(f'{num}',end=" ")
    print("×" if num > 1 else "=",end=" ")
    f *= num
    num -= 1
print(f,end=" ") '''

num = int(input('Enter a number to calculated factorial: '))
count = 1

print(f'Calculating {num} != ',end=' ')
for factorial in range (num,0,-1):
    print(factorial, end=" ")
    print("x" if factorial > 1 else '=',end=' ')
    count *= factorial
print(count, end= ' ')
    