'''PHRASE = str(input("Enter a phrase:\033[32m ")).strip().lower().replace(" ", "")
print('\33[m', end='')
REVERSE = (PHRASE[::-1])
print(f'The reverse of {PHRASE} is {REVERSE}')

if PHRASE == REVERSE:
    print('We have a palindromo!')
else:
    print('It is not a palindromo.')'''
    
phrase = str(input("Enter a phrase: ")).lower().replace(" ","")
reverse = "" #contador serve para adicionar as letras da frase na ordem contraria

for letter in phrase [::-1]:
    print(f"{letter}", end="")
    reverse += letter
    
if phrase == reverse:
    print("\n\nIt is the same!")   
else: 
    print("\n\nIt is different!")

