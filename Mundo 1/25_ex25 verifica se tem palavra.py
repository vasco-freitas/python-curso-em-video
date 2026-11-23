name = str(input("Enter your full name: ")).strip().title()

print(f"Your full name is: {name}")
print(f"Your name has Silva? {"Silva" in name}")  #verifica se silva esta na variavel name
if "Silva" in name: #verifica se silva esta na variavel name
    print(f'The name Silva appears in the index {name.find("Silva")+1}.') #encontra a posiçao onde começa a palavra silva, se nao encontrar retorna -1