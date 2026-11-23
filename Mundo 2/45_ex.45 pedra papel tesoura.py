from random import choice
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

print("""==== Pedra, papel ou tesoura? ====

Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

while True:
    try:
        sua_opcao = int(input("Qual é a sua jogada? ")) #simplica e tranforma as 3 opcoes em numeros
        if sua_opcao < 0 or sua_opcao > 2:
            print("Jogada inválida. Verifique o menu de opções.")
            continue
        break
    except ValueError:    
        print("Opção inválida. Confirme menu")
    
escolhe = choice(lista)
    
sleep(1)

print(f"""{"=-"*14}
Jogador jogou {lista[sua_opcao]}
Computador jogou {escolhe}
{"=-"*14}""")

sleep(2)

if escolhe == lista[sua_opcao]:
    print("Vocês empataram")    
elif (escolhe == "Tesoura" and lista[sua_opcao] == "Papel") or \
(escolhe == "Papel" and lista[sua_opcao] == "Pedra") or \
(escolhe == "Pedra" and lista[sua_opcao] == "Tesoura"):
    print("Computador ganhou")
else: 
    print("Você venceu")