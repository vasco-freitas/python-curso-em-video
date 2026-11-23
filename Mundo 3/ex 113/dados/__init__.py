def read_int(msg):
    """Esta funcao retorna a validação se é número inteiro.
    variavel = read_int("sua mensagemm")
    """
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(f"Error! Please, enter a valid integer.\n") 
              
def read_float(msg):
    """Esta funcao retorna a validação se é número float.
    variável = read_float("sua mensagemm") 
    """
    while True:
        try:
            num = input(msg).replace("," , ".")
            return float(num)
        except ValueError:  
            print(f"Error! Please, enter a real number.")
        except (KeyboardInterrupt):
            print("interrompido")    
            break
            
'''m = read_int("Enter an integer number: ")
b = read_float("Enter a real number: ")
        
print(f"The integer value entered was {m} and the real {b:g} ")'''

