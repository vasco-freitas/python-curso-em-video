from random import randint
b = randint(0,5) #gera um numero aleatorio entre 0 e 5
print("--==--"*10)
print('Thinking of a random number bettween 0 and 5... Try to guess!')
print("--==--"*10)

a = int(input("Enter your attempt: "))

if b == a: #se a variavel b for igual a variavel a
    print(f"You got it right a number {b}, congratulations!")
else:
    print(f"You got it wrong a number {b}, try again!")