open = [] ; closed = []

express = input('Enter a expression: ')

for n in express:
    if n == '(':
        open.append(n)
    elif n == ')':
        closed.append(n)
        
if len(open) == len(closed):
    print('Your expression your correct!')
else:
    print('Your expression your wrong!')