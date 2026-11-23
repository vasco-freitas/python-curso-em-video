def pyhelp():
    color = {'limpa': '\033[m',
        'branco': '\033[0;30;47m',
        'verde': '\033[0;30;42m',
        'vermelho': '\033[0;30;41m',
        'verdee': '\033[92m',       # Letras verdes
        'vermelhoo': '\033[91m'     # Letras vermelhas
        }
    while True:
        print(f'{color['verde']}PyHelp: HELP SYSTEM{color['limpa']}')
        quest = input(f'Function or Library:(End){color['verdee']} ').strip() 
        print(f'{color['branco']}',end='')
        if quest.lower() == 'end':
            print(f'{color['vermelho']}Good night :){color['limpa']}')
            break
        try:
            print(color['branco'])
            help(eval(quest))
            print(color['limpa'])
        except Exception:
            print(f'{color['vermelhoo']}Error! Command {quest} not found.{color['limpa']}')
        
        
pyhelp()