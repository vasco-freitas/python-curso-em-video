#Condição: exemplos
carro = input("Enter the direction of the car: ")

if carro == "left": #se a variavel carro receber o valor left entao executa o camando print abaixo
    print("The car turns left.")
else: #se a variavel carro receber o valor right entao executa o camando print abaixo
    print("The car turns right.")
print("You have arrived at your destination.") #no fim executa este print



#forma mais simplificada(usando operador ternário na mesma linha)
print("The car turns left" if carro == "left" else"The car turns right") #se a variavel carro receber o valor left executa o comando 1 se nao executa o comando 2



#segundo exercicio
tempo = int(input("How old is your car? "))

if tempo <= 10: #se a variavel tempo for menor ou igual a 10 entao executa o camando print abaixo
    print("Your car is new!")
else: #se a variavel tempo for maior  que 10 entao executa o camando print abaixo
    print("Your car is old!")
print("---END---")


#terceiro exercicio
nome = str(input("What is your name? ")).strip().title()

if nome in ["Vasco","Tatiana"]:
    print(f"What a beautiful name, {nome}!")
else:
    print(f"Your name is not very nice, {nome}!")
print(f"Good day, {nome}")


#quarto exercicio
num = float(input("Enter the first note: "))
numm = float(input("Enter the second note: "))

media = (num+numm)/2
print(f'Your average is: {media:.1f}')
if media >= 14:
    print('Congralutions, you passed with good average!')
else: 
    print("Your average was low, study more!")
    
print(f'Congralutions!' if media >= 14 else "Study more!") #forma mais simplificada
    
