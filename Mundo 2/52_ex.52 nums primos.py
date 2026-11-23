colors = {"red":"\033[31m", 
          "green":"\033[32m",
          "yellow":"\033[33m",
          "reset":"\033[m"}

print("Enter a 0 to exit!\n")
while True: 
    num = int(input(f"Enter a number: {colors["green"]}"))
    print(colors["reset"],end="")
    total = 0
    
    if num < 0:
        print("Write a positive number.\n")
        continue
    elif num == 1 or num == 0:
        print("It is a neutral number.\n")
        if num == 0:
            break
        continue    

    for c in range (1,num+1):
         if num % c == 0:
             total = total + 1
             print(f'{colors["yellow"]}{c}{colors["reset"]}',end=" ")
         else:    
             print(f"{colors["red"]}{c}{colors["reset"]}",end=" ") 
             
    print(f"\nThe number {num} was divisible by {total}.")
    if total > 2:
        print("This is a composite number.\n")
    else: 
        print("This is a prime number.\n")