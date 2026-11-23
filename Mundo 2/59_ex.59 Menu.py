while True:
    try:
        num1 = float(input("Enter a number: "))
        break
    except ValueError:
        print("Option invalid! Please enter a number valid.")
        
while True:
    try:
        num2 = float(input("Enter other number: "))
        break
    except ValueError:
        print("Option invalid! Please enter a number valid.")    

choose = 0; other = ""
while choose != 5 and other != "N":
    print("""\nChoose one of the options
[ 1 ] Sum
[ 2 ] Multiplication
[ 3 ] New numbers
[ 4 ] smallest and largest number
[ 5 ] exit the program""")

    while True:
        try:
            choose = int(input("\nWhat is your option? "))
            if choose not in [1,2,3,4,5]:
                print("Option failed. Try again, please.")
                continue 
            break
        except ValueError:
            print("Option invalid!")

    if choose == 1:
        result = num1 + num2
        print(f"The sum of the numbers {num1:g} + {num2:g} is {result:g}!")
    elif choose == 2:
        result = num1 * num2
        print(f"The multiplication between {num1:g} × {num2:g} is {result:g}!")
    elif choose == 3:
        while True:
            try:
                num1 = float(input("\nEnter a number: "))
                break
            except ValueError:
                print("Option invalid! Please enter a number valid.")
        while True:
            try:        
                num2 = float(input("Enter other number: "))
                break
            except ValueError:
                print("Option invalid! Please enter a number valid.")     
    elif choose == 4:
        if num1 == num2:
            print("The numbers are equal.")
        elif num1 > num2:
            print(f"The number {num1:g} is greater than the number {num2:g}.")
        else:
            print(f"The number {num1:g} is less than the number {num2:g}.")         
    if choose in [1,2,3,4]:
        while True:
            other = input("\nDo you want to see any other options?[S/N] ").strip().title()
            if other not in ["S","N"]:
                print("Option invalid! write yes [S] or no [N].")
                continue
            break
            
print("Thank you! Until next time ;)")