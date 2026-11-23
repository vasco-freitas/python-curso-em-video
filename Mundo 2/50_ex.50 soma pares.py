"""totall = 0
result = 0
for even in range (1,7):
    while True:
        try:
            you = int(input(f"Enter the {even} value: "))
            break
        except ValueError:
            print('Option invalid. Please try again.')    
    if you % 2 == 0:
        totall += you
        result += 1
print(f'You entered {result} even numbers, and the sum was {totall}.')        
        


print()

sum = 0
total = 0

for numbers in range(0,5):
    if numbers % 2 == 0:
        total += numbers
        sum += 1
        
print(f"\nThe total sum of the {sum} even numberes is {total}!")

"""

n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
n3 = int(input("Enter a third number: "))
n4 = int(input("Enter a forth  number: "))
n5 = int(input("Enter a fifth number: "))
n6 = int(input("Enter a sixth number: "))

lista = (n1,n2, n3,n4,n5, n6)
soma = 0; n = 0

if lista[0] % 2 == 0:
    n += lista[0]
    soma += 1
    
if lista [1] % 2 == 0:
    n += lista[1]
    soma +=1
 
if lista [2] % 2 == 0:
    n += lista[2]
    soma += 1
 
if lista[3] % 2 == 0:
    n += lista[3]
    soma += 1
    
if lista[4] % 2 == 0:
    n += lista[4]
    soma += 1
    
if lista[5] % 2 == 0:
    n += lista[5]
    soma += 1    

print(f"Tem {soma} numeros pares e a soma total é {n}.")