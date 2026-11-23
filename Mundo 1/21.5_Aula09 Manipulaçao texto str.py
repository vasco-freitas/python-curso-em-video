frase = 'Olá,tudo bem?'

print(frase[:]) #fatia a str, pega todos os carateres  da variavel frase
print(f'The character 3 is: {frase[2]}') #acessa o carater do indice 2 variavel frase
print(frase[2:4]) #fatia a string, pegando os caracteres do indice 2 ao 3 (o indice 4 não é incluido)
print(frase[2:]) #fatia a str, pegando os caracteres da variavel frase a partir do 2 ate o final da str
print(frase[:5]) #fatia str, pega os careteres da variavel do inicio até o indice 4(nao inclui o 5)
print(frase[3::2]) #fatia str, pega os carateres da variavel a partir do 3, pulando 2 em 2(podendo ser 1,2,3...)
print(frase[::3]) #fatia str, pega todos os carateres da variavel, pulando de 3 em 3
print(frase[::-1]) #fatia str, pega todos os carateres da variavel, pula 1 em 1, mas invertendo a ordem
print(frase[10:0:-1]) #fatia str, pega os carateres a partir do 10, pulando 1 em 1, inverte a ordem, e para no 0 (nao inclui 0)
print(frase[5:2:-2]) #fatia str, pega os carateres a partir do 5, pulando 2 em 2, inverte a ordem, e para no 2 (nao inclui o 2)
print(frase[-1:]) #fatia str, pega os carateres a partir do -1 (ultimo indice) até o final da str
print(frase[1:7:1]) #fatia a str, pega os carateres a partir do 1, pulando 1 em 1 e para no 7 (nao inclui o 7)
print()

#Ánalise da str frase = ´Olá, tudo bem?'
print(f'The phrase has {len(frase)} characters.') #conta a quanstidade de carateres dentro da variavel, inclui espaços
print(f'The phrase has {frase.count("á")} letters á.') #conta a quantidade de vezes que uma letra ou palavra aparece dentro da variavel
print(f'The phrase has {frase.upper().count("O")} letters "o and O".') #transforma a str em letras maiusculas e depois conta a quantidade de vezes que o "o" aparece, assim contando minusculo e maiusculo
print(f'The phrase has {frase.count("o", 0, 6)} letters "o" between indices 0 and 5.') #conta a quantidade de vezes que a letra aaparece, apenas entre os indices 0 a 5 (6 nao conta)
print(f'The expression "tudo" starts  in the index {frase.find("tudo")}') #encontra a posicao onde a palavra tudo começa, se a palavra nao for encontrada retorna -1
print(f'The exprresion "android" starts in the index {frase.find("android")}') #encontra a posicao da palavra android, se nao encontrar retorna -1
print(f'The last letter "a" appears in the index {frase.rfind("a")}.') #rfind retorna a posicao da ultima ocorrencia
print(f'The expression "Olá" is in the phrase: {"Olá" in frase}.') #verifica se a palavra "Olá" esta presente na frase, retorna True ou False
print(f'The expression "olá" is in the character: {frase.lower().find("olá")}') #transforma a str em letras minusculas e depois encontra a posicao da palavra "olá", se nao encontrar retorna -1
print()

#Transformação de str
print(frase.replace("bem","controlado")) #substitui a palavra "bem" por "controlado", mas sem trocar a variavel frase
print(frase) #a variavel frase continua a mesma, pois o comando replace nao altera a variavel, apenas retorna uma nova str com a substituição feita
print(f'Transforming the phrase into uppercase letters: {frase.upper()}') #transforma a str em letras Maiúsculas
print(f'Transforming the phrase into lowercase letters: {frase.lower()}') #transforma str em letras minusculas)
print(f'Trasnform the first letter to uppercase: {frase.capitalize()}') #Transforma a primeira letra da str em maisuscula e o restante em minuscula
print(f'Transform the first letter of all words to uppercase: {frase.title()}') #Trasnforma a primeira letra de cada palavra em maiuscula e o restante em minuscula
print()
phrase = "   vamos programar! "
print(f'Phrase with stripped whitespace: {phrase.strip()}.') #remove os espaços desnecessarios brancos no inicio e do fim da str, mas sem alterar a variavel
print(f'Phrase with stripped whitespace on the right: {phrase.rstrip()}') #remove os espacos desnecessarios brancos no fim da str
print(f'Phrase with stripped whitespace on the left: {phrase.lstrip()}') #remove os espacos brancos no inicio da str
print()

#Divisão e junção de str
print(frase.split()) #divide a str em uma lista de palavras, usando o espaço como separador
print(frase.split("o")) #divide a str em uma lista de palavras, usando a letra "o" como separador
print(frase.split("o",1)) #divide a str em uma lista de palavras usando a letra "o" como separador mas apenas na primeira ocorrencia
print(f'Joining the split phrase: {"-".join(frase.split())}') #Junta as palavras da lista gerada pelo split, usando o "-" como separador entre as palavras
print()

print("""O Lorem Ipsum é um texto padrão utilizado na indústria de design e impressão, criado a partir de uma obra clássica de Cícero. 
Ele é frequentemente usado para testar layouts e interfaces antes que o conteúdo final seja disponibilizado. Existem várias ferramentas online 
que podem gerar texto Lorem Ipsum, permitindo que designers e desenvolvedores testem diferentes estilos e layouts sem a necessidade de 
conteúdo real.""") #imprime um texto grande usando as aspas triplas que permitem a quebra de linha sem a necessidade de usar o comando \n para pular linha
print()

a = "eu gosto de ti"
a = a.replace("gosto","amo")
dividido = a.split()
print(a) #substitui a palavra "gosto" por "amo" e depois imprime a nova str, a variavel agora tem o valor "eu amo de ti"
print(dividido[0:2]) #divide a str em uma lista de palavras  e depois imprime os elementos do indice 0 e 1 da lista, ou seja eu e amo
print(dividido[2][1]) #acessa o elemnto do indice 2 da lista que é a palavra "de" depois acessa o caracter do indice 1 da palavra "de", imprime a letra "e"