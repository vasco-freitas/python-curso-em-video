while True:
    try:
        WEIGHT = float(input("What is your weight? (kg) "))
        if 0 >= WEIGHT or WEIGHT > 300:
            print("The minimum weight is 0kg and the limit is 300kg.")
            continue
        break
    except ValueError:
        print("Option invalid. Write your weight!")   

while True:
    try:       
        CM = float(input("How tall are you? (cm) "))
        if CM.is_integer() or CM > 3.0:
            CM = CM / 100
        if 0 >= CM or CM >= 3.00:
            print("You don't exist. Between 0 a 300.")
            continue
        break
    except ValueError:
        print('Option invalid. Write your tall!')
        
IMC = WEIGHT / (CM**2)

print(f"\nThe person's IMC is {IMC:.1f}.")

if IMC < 18.5:
    print("Underweight!")
elif IMC < 25:
    print("Ideal wight!")   
elif IMC < 30:
    print("Overweight!")
elif IMC < 39:
    print("Obesity!")   
else:
    print("Morbid obesity!")