num = int(input('Enter a number: ')) 
digitos = str(num) #trasnfroma o numero em str e assim coonta a quantidade de digitos usando a funçao len()
print(f'The number you entered is: {num} and has {len(digitos)} digits.')
print(f'Thousands digit: {num//1000%10}') #pega o numero e divide por 1000, ou seja, pegao digito das unidades de milhar, se o numero tiver menos de de 4 digitos retorna 0
print(f'Hundreds digit: {num//100%10}') #pega o numero e divide por 100, ou seja, pegao digito das unidades de centena, se o numero tiver menos de de 3 digitos retorna 0
print(f'Tens digit: {num//10%10}') #pega o numero e divide por 10, ou seja, pegao digito das unidades de dezena, se o numero tiver menos de de 2 digitos retorna 0
print(f'Units digit: {num%10}') #pega o numero e faz modulo por 10, ou seja, pegao digito das unidades, se o numero tiver menos de de 1 digito retorna 0

#outra forma de resolver
numm = int(input("Enter a number: "))
digito = str(numm).zfill(4) #trasnforme o numero em str e preencha com 0 se o numero tiver menos de 4 digitos
print(f'Thousand digit: {digito[0]}')
print(f'Hundreds digits: {digito[-3]}') 
print(f'Tens digits: {digito[-2]}') 
print(f'Units digits: {digito[-1]} ') #acessa o carater do indice 3 da str, se o numero tiver menos de 4 digitos retorna um erro de indice fora do alcance
