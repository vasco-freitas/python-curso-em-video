from unidecode import unidecode 
phrase = str(input("Enter a phrase: ")).strip().lower()
c = unidecode(phrase) #remove acentos da str gerando assim o resultado das letras ou palavras sem acentos
print(f'The letter "a" appears {c.count("a")} times in the phrase.')
print(f'The first letter "a" appears in the index {c.find("a")+1}.')
print(f'The last letter "a" appears in the index {c.rfind("a")+1}.') #rfind retorna a posicao da ultima ocorrencia

b = str(input("Enter a letter: ")).strip().lower()
print(f'The letter "{b}" appears {c.count(b)}.')
print(f'The first letter "{b}" appears in the index {c.find(b)+1}.')
print(f'The last letter "{b}" appears in the inex {c.rfind(b)+1}.') #rfind retorna a posicao da ultima ocorrencia