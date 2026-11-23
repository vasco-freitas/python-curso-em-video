name = str(input('What is your full name? ')).strip().title() #recebe o nome do usuario, transforma em str e remove espacos desnecessarios no inicio e no fim, e depois transforma a primeira letra de cada palavra em maiuscula
dividido = name.split()
join = "".join(name.split())
print(f'Your full name is: {name}.')
print(f'Your name in lowercase is: {(name.lower())}.')
print(f'Your name in uppercase is: {(name.upper())}.')
print(f'Your name without spaces is: {join}.')
print(f'Your full name has {len(join)} letters.')
print(f'Your first name is {dividido[0]} and it has {len(dividido[0])} letters.')
#print((name.find(""))) #encontra a posiçao do 1 espaco em branco, ou seja o final do primeiro nome, e retorna a posiçao do indice onde o espaco esta localizado, se nao encontrar retorna -1
print(f'Your middle names are: {dividido[1:-1]} and they have {len("".join(dividido[1:-1]))} letters.') #divide a str em uma lista de palavras  e depois imprime os elementos do indice 1 e -1 da lista, ou seja os nomes dos meio
print(f'Your last name is: {dividido[-1]} and it has {len(dividido[-1])} letters.') #acessa o ultimo elemento da lista dividido, que é o sobrenome, e depois conta a quantidade de letras do sobrenome usando a função len()