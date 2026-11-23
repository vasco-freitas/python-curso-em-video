key = ["1","2","3","4"]
key_limpo = ",".join(key)

print('======== Lojas Vasco =========')

while True:
    try:
        price = float(input('Price of purchases: €'))
        if price <= 0:
            print("It cannot be a negative value or zero.")  
            continue
        break      
    except ValueError:
        print("Error. Enter a valid number.")
        
print("""PAYMENT METHODS
[ 1 ] Cash / Check (10% discount)
[ 2 ] Card view (5% discount)
[ 3 ] 2x on the Card (Normal price)     
[ 4 ] 3x or more on the Card (20% interest)""")

while True:
    option = input("What is the option? ")
    if not option in key:
        print(f"Option invalid! Enter the options {key_limpo}.")
    else:
        break
        
if option == "1":
    price = price - (price * 0.1)
    print(f"\nYou have a 10% discount.")
    print(f"Final price: {price:.2f}€")
    
elif option == "2":
    price = price - (price * 0.05)
    print(f'\nYou have a 5% discount.')
    print(f'Final price: {price:.2f}€')

elif option == "3":
    price2x = price / 2
    print(f'\nYour purchase will be split into 2 installments. You will play monthly: {price2x:.2f}€.')
    print(f'\nFinal price will not change: {price:.2f}€')   
    
else:
    while True:
        try:    
            installments = int(input("How many installments? "))
            if 2 >= installments:
                print('It must be greater than 2.')
                continue 
            break
        except ValueError:
            print("Option invalid.")
    
    final_price = price * 1.2
    price3x = final_price / installments 
    print(f'''\nPurchase in {installments} installments of {price3x:.2f}€ monthly.
Old price: \033[9m{price:.2f}€\033[0m
Final price including interest: {final_price:.2f}€.''')