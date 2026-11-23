from time import sleep
from random import randint

print("=== EX029 === electronic radar === ")
#a = int(input("what is  the car is speed? "))

speed = randint(10,150) #gera um numero aleatorio entre 10 e 150

print(f"You passed the speed {speed} km/h")
print("Processing...")
sleep(3) #espera 3 segundos antes de executar o proximo comando

print()
#if  speed > 80:
#	fine = (speed - 80) * 4.99
	#diff = speed - 80 
#	print(f"FINED!! You exceeded the maximum speed limit of  80km/h by {diff}km/h!")
#	print(f"You must pay a fine of {fine:.2f}€")  
if speed > 80: #se a variavel speed for maior que 80
	diff = speed - 80 #a variavel diff recebe o valor da variavel speed, menos 80
	if diff <= 20: #cria uma condição dentro do if,se a variavel diff for menor ou igual a 20
		multiply = 3.99 #multiplica o valor da variavel multiply por 3.99
		fine = "minor misdemeanor" #a
		
	elif diff <= 40:
		multiply = 8.99
		fine = 'serious offense'
	else:
		multiply =  15
		fine = "very serious infraction"
		
	factorial = diff * multiply #multiplica o valor da variavel diff pela variavel multiply
	print('FINED!!!')
	print(f'Exceeded the maximum speed limit of 80 km/h by {diff}km/h. Which is a {fine}.')
	print('Processing the fine amount...')
	sleep(2) 
	print(f"You will have to pay {factorial:.2f}€ this week.")
	
	
elif speed < 40: #se a variavel speed for menor que 40 entao executa o camando print abaixo
	fine = (40 - speed) *3.49 #a variavel fine recebe o valor da variavel 40 menos a variavel speed vezes 3.49
	diff = 40 - speed #a variavel diff recebe o valor da variavel 40 menos a variavel speed
	print(f"FINED!! You exceeded the minimum speed of 40 km/h by {diff}km/h!")
	print(f"You must pay a fine of {fine:.2f}€")
		
else: #se a variavel speed for maior que 39 e menor que 81 entao executa o camando print abaixo
	print("Very good!")

print("")
print("Have a good day! Drive safely!")