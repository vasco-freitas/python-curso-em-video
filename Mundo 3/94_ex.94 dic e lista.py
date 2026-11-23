data = []

while True:
    real = {}
    real["Name"] = input("Name: ").title().strip()
    while True:
        real["Gender"] = input("Gender[M/F]: ").title().strip()
        if real["Gender"] not in ["M","F"]:
            print("Plesa, enter M or F!")
            continue
        break    
    real["Age"] = int(input("Age: "))
      
    data.append(real)
    
    while True:
        sn = input("Want to continue?[S/N]: ").title().strip()
        if sn not in ["S","N"]:
            print("Please, enter S or N!")
            continue
        break    
    if sn in "N":
        break

regist = len(data)   

soma = sum(item['Age'] for item in data) / regist

fem = [n['Name'] if n['Gender'] == 'F' else 'none' for n in data ]

print('===--=='*6)
print(f'In total we has {regist} people registered!')
print(f'The average age is {soma:0g}.')
print(f'The women registered were {', '.join(fem)}.')
print('Above-average people:')
for n in data:
    if n['Age'] > soma:
        print(f'')
    
    