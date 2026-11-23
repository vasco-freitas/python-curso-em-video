trip = float(input('How far is your trip in km? '))
if trip <= 200: #se a variavel trip for menor ou igual a 200
    normal = trip * 0.40
    
else: #se a variavel trip for maior que 200
    normal = trip * 0.32
    
print(f'Your will take a trip from {trip}km. The cost will be {normal:.2f}€.')
print('Have a good trip!')