from time import sleep

try:
	a = float(input("The first number: "))
	b = float(input("The second number: "))
	c = float(input("The third number: "))
	d = float(input("The fourth number: "))
	
except ValueError:
	print("\n[erro] Oops! You can only whrite numbers and periods.")
	exit()

y = sorted([a, b, c, d])
small = y[0]
big = y[3]
middle = f"{y[1]:g} and {y[2]:g}"  

print()
print("processing...") 
sleep(2)
print()

print(f"The largest number is {big:g} .")
print(f"The middle numbers are {middle}")
print(f"The smallest number is {small:g} .")
print()
print()

print("Second form with if ")
print("Processing...")
sleep(1)
menor = a
if menor > b:
	menor = b
if menor > c:
	menor = c
if menor > d:
	menor = d
	
maior = a
if maior < b:
	maior = b
if maior < c:
	maior = c
if maior < d:
	maior = d
	
y.remove(menor)
y.remove(maior)

f = [f"{num:g}" for num in y]
ff = ", ".join(f)

print(f"The smallest number is {menor:g} .")
print(f"The middle numbers are {ff} .")
print(f"The largest number is {maior:g}")