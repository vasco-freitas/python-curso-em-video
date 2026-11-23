from time import sleep

try:
	a = float(input("Enter your salary: "))
	
except ValueError:
	print("\n[erro] Oops! You can only type numbers and periods")
	exit()

if a  < 1250:
	discount = "25%"
	sum = (a * 0.25) + a

else:
	discount = "15%"
	sum = (a * 0.15) + a

print()
print("Processing...")
sleep(3)
print()
	
print(f"Being  your base salary {a:.2f}€, and with the increase of {discount},  your future salary will be {sum:.2f}€.")
print("We hope to make you happy!")