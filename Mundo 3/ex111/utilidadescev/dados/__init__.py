def read_money(msg):
    while True:
        num= input (msg)
        numt = num.replace(' ', '').replace(',', '.')
        if numt.replace('.', '', 1).isnumeric():
            valor = float(numt)
            return valor
        else:
            print(f'Error! {numt} is an invalid price.')
    
#num = input('Enter a number: ')
#read_money(num)



'''def read_money(num):
    while True:
        msg = input(num)
        numd = msg.replace(' ', '').replace(',', '.')
        if numd.replace('.', '', 1).isnumeric():
            return float(numd)
            
        else:
            print('Error')'''