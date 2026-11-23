data = []

while True:
    real = {"Name": input("Player name: ").title().strip() , 
    "Goals": []}
    games = int(input(f"How many games did {real["Name"]} play? "))
    
    for n in range (1, games + 1):
        real["Goals"].append(int(input(f"How many goals were scored in  the match {n}? ")))
        
    real["Total"] = sum(real["Goals"])
    data.append(real)    
        
    sn = input("Want to continue[S/N]? ").title().strip()
    if sn in "N":
        break
 
print(f"""{"===--=="*5}
{"N°":<5} {"Name":<15} {"Goals":<8} {"Total":<8}""")       

for n, r in enumerate(data):
    lista = ", " .join(map(str, r["Goals"]))
    print(f"{n+1:<5} {r["Name"]:<15} {lista:<8} {r["Total"]:<8}", end="")
    print()
    
while True:
    print('----'*8)
    rvw = int(input("Which player is data is being displayed?[999 to exit] "))
    if rvw == 999:
        print('Come back always!')
        break
    elif 1 <= rvw <= len(data):
        player = data[rvw-1]['Name']
        print(f"--- Player {player}:")
        for n,j in enumerate(data[rvw-1]['Goals']):
            print(f'  In game {n+1} he scored {j} goals!')
    else:
        print(f'Error! There is no player with code {rvw}!')