cidade = str(input('In wich city where you born? ')).strip().title() #recebe o nome da cidade, transforma em str e remove espacos desnecessarios no inicio e no fim, e depois transforma a primeira letra de cada palavra em minuscula
print(f'Your city has the name Santo? {"Santo" in cidade}!') #verifica se a palavra Santo esta na str
print(f'Your city has the first word Santo? {"Santo" in cidade [:5]}!') #acessa os 5 primeiros caracteres da str
dividir = cidade.split() #divide a str em uma lista de palavras
print(f'Your city has the first word Santo? {"Santo" in dividir[0]}!') #acessa o primeiro elemento da lista dividir, que é o primeiro nome da cidade
print(f'The Word Santo starts in the index {cidade.find("Santo")+1}.') #encontra a posição onde começa a palvra santo, se nao encontrar retorna -1.ção d
print(f'Is there a city called Santo? {"Santo" in cidade}. And is the first word? {cidade[:5] == "Santo"}!') #verifica se a palavra Santo esta na str, e se sim, verifica se a primeira palavra da str é Santo