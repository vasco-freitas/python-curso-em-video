num = float(input('Enter a numer: ')) #escreva um numero e trasnforma em decimal
a = f"{num:g}" #transforma o numero em str e retira as casas decimais com o :g
if num.is_integer() == False: #Verifica se a variavel a recebeu um numero inteiro, ou seja, sea  resposta for True executa este comando  e False executa o comando seguinte
    print(f"The number {a} is not valid. Apply even/odd numbers only to integers.")
    
elif num % 2 == 0: #verifica se  o numero é par com o operador % que retorna o resta da divisão
    print(f'The number {a} is even.')
    
else: #se nao for par entao é impar e retorna a seguinte mensagem
    print(f'The number {a} is odd.')