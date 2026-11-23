def increase(num, rate, sit = False):
    """Aumento do numero: Deve colocar  num = float(input('mensagem '))  print(incresase(num, a taxa, True #formata dinheiro))"""
    inc = num + (num * rate / 100)
    if sit == True:
        return money_form(inc)
    return inc

def decreasing(num,rate, sit = False):
    """Diminuir o numero: Deve colocar  num = float(input('mensagem '))   print(incresase(num, a taxa, True #formata dinheiro)"""
    dec = num - (num * rate / 100)
    if sit == True:
        return money_form(dec)
    return dec


def double(num, sit = False):
    """Duplicar o valor: Deve colocar   num = float(input('mensagem '))   print(double(num, True #formata dinheiro))"""
    do = num * 2
    if sit == True:
        return money_form(do)
    return do

def half(num, sit = False):
    """Divide o valor: Deve colocar  num = float(input('mensagem '))  print(half(num, True #formata dinheiro))"""
    ha = num / 2
    if sit == True:
        return money_form(ha)
    return ha

def money_form(num):
    value = f'{num:.2f}€'
    return f'{value.replace('.',',')}'

def summary(num,rate, rated):
    """Lista organizada. como usar:
num = float(input('Enter the price: €'))
summary(num,23,24)"""
    data = {}
    data['Price analyzed'] = money_form(num)
    data['Double price'] = double(num,True)
    data['Half price'] = half(num,True)
    data[f'Increase {rate}%'] = increase(num,rate,True)
    data[f'Decreasing {rated}%'] = decreasing(num,rated,True)
    
    print(f"""{'-'*30}
{'VALUE SUMMARY'.center(30)}
{'-'*30}""")
    
    for key,val in data.items():
        print(f'{key + ':':<16} {str(val):>8}')
