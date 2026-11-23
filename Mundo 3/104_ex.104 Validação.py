def readint(num):
    """com este programa serve para certificar que o numero usado se é inteiro ou não
    """
    while True:
        try:
            n = int(input(f'{num}'))
            return n
        except ValueError:
            print('Error! Enter a whole number.')
    

n = readint('Enter a number: ')
print(f'You typed the number {n}.')

help(readint)