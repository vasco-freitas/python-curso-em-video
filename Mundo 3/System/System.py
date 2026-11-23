from Menu import *
from Regist import *

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    print('File not found!') 

menu = main_menu("1 - See registered persons","2 - Registered new person","3 - Exit the system")
