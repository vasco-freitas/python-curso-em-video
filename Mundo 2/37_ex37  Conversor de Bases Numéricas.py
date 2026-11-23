while True:
    try:
        NUM = int(input("Enter a number: "))
        break
    except ValueError:
        print('Error! You must write whole number.')      

print("""Choose one of the bases for conversion: 
[ 1 ] Convert to BINARY
[ 2 ] Convert to OCTAL
[ 3 ] Convert to hexadecimal lower
[ 4 ] Convert to HEXADECIMAL upper""")

OPTION = input("Choose your option: ")

if OPTION == "1":
    print(f"\n{NUM} converted to BINARY equals {NUM:b} !")
elif OPTION == "2":
    print(f"\n{NUM} converted to OCTAL equals {NUM:o} !")
elif OPTION == "3":
     print(f"\n{NUM} converted to hexadeciamal lower equals {NUM:x} !")
elif OPTION == "4":
    print(f"\n{NUM} converted to hexadeciamal upper equals {NUM:X} !")
        
else:
    print("Option invalid! You must type the options 1, 2, 3 or 4.")    

